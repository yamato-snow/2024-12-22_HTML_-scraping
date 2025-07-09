[![](https://storage.googleapis.com/zenn-user-upload/topics/dc1922748b.png)AWS](/topics/aws)[![](https://storage.googleapis.com/zenn-user-upload/topics/8b069b1a3d.png)DynamoDB](/topics/dynamodb)[![](https://storage.googleapis.com/zenn-user-upload/topics/4aca6a70a6.png)Bedrock](/topics/bedrock)[![](https://zenn.dev/images/topic.png)LLM](/topics/llm)[![](https://static.zenn.studio/images/drawing/tech-icon.svg)tech](/tech-or-idea)

こんにちは。[シンプルフォーム株式会社](https://www.simpleform.co.jp/) にてインフラエンジニアをしています、山岸です。

最近、普段の業務とは少し離れた取り組みとして、社内の何人かのメンバーと一緒に LLM を業務オペレーションに組み込む PoC を行っています。価値検証はこれからですが、システム開発の部分はある程度形になってきたため、今回はその内容についてご紹介したいと思います。

DynamoDB Streams を利用したバッチ処理プロセスの非同期化や、プロンプトのバージョン管理など、運用に組み込む上での工夫点なども書いているので、参考になるものがあれば幸いです。

!

本記事は LLM に関するものではありますが、具体的な利用方法としては Amazon Bedrock の基盤モデルを Lambda 関数から呼び出すという一般的なものになります。RAG や Fine-Tuning などの話は出てこないので、あらかじめご了承ください。

PoC 発足の経緯
=========

Amazon Bedrock Prototyping Camp について
------------------------------------

以前、『Amazon Bedrock Prototyping Camp』という AWS Japan 主催の 1 Day ワークショップにご招待頂き、今年 2/6 (火) の回にエンジニアメンバー 3 名で参加させて頂きました。

ワークショップの内容としては、午前に Amazon Bedrock に関する座学やハンズオン、午後に会社毎のグループに分かれてのプロトタイピングといった感じでした。筆者自身は、「Amazon Bedrock という AWS の生成 AI サービスがあるらしい」くらいの知識で臨みましたが、Amazon OpenSearch Service を用いた [RAG](https://aws.amazon.com/jp/what-is/retrieval-augmented-generation/) の実装方法など、かなり実践的な内容についても効率よくキャッチアップでき、参加意義はとても大きかったと思います。もし機会がありましたら、是非参加してみることをおすすめします。

ユースケース検討
--------

ワークショップの中で、当社における具体的な活用方法について一緒に参加したメンバーと議論してみた結果、社内の調査オペレーション（調査Ops）業務と相性が良いのではないかという話になりました。

調査 Ops の業務内容については以下の note 記事で詳しく紹介されていますが、様々なデータソースから収集したデータを整備（正規化・クレンジング）する工程が存在します。

<https://note.com/simpleform/n/nc87f4797ca9f>

データの品質はデータソースによって様々で、これらをあるべき状態に整備する作業は大変な労力を伴うものです。中にはパターン化して機械的に処理できるものもありますが、パターン化が難しく人による作業・確認が必要なものはどうしても残ってしまいます。

LLM の出番としては、「人間にとっては処理結果が明らかだが、パターン化が難しく機械的に処理しづらかったデータ」をある程度正しく処理する部分だと考えました。LLM の挙動も確率的なものなので最終的には人による目視検査は必要ですが、それでもかなりの工数を削減できる見込みがあったため、今回 PoC として取り組んでみることにしました。

!

少し宣伝になってしまいますが、当社の Ops スタッフメンバーの皆さんによる note 記事が公開されていますので、もしご興味があれば併せてご覧頂けますと幸いです。

* [地方在住✕フルリモートのリーダーが考えるチーム作り](https://note.com/simpleform/n/n9c0e5b431639)
* [リーダー初挑戦の私が意識していること](https://note.com/simpleform/n/n7e195224d9d7)
* [転勤族でも大丈夫。リモートで目指すキャリアアップ](https://note.com/simpleform/n/nd2b7e6f0dae7)
* [ブランクからの再出発、望み通りの働き方を実現](https://note.com/simpleform/n/n999b8b94b076)
* [家族の応援を力に、経験と縁が紡ぐ新しいキャリア](https://note.com/simpleform/n/ndcfefb130e18)

アーキテクチャ
=======

実装したアーキテクチャは以下の通りです。

正規化対象となる生データは Google スプレッドシート上に存在することを想定していますが、ECS タスク等で DynamoDB テーブルに処理内容・処理対象データを書き込めれば保存場所はどこでも問題ありません。スプレッドシートの場合は Google Apps Script (GAS) 操作を起点に ECS タスクを起動し、DynamoDB テーブル (executions, requests) に書き込みます。

requests テーブルに処理対象レコードが書き込まれると、DynamoDB Streams によってリクエスト処理用の Lambda 関数が呼び出されます。Lambda 関数では実行情報などからプロンプトを生成し、Amazon Bedrock の基盤モデルを Boto3 で呼び出します。一連の処理に関するメタ情報や処理結果などは、後で Athena 等で分析しやすいよう、S3 に JSON 形式で保存します。

![](https://res.cloudinary.com/zenn/image/fetch/s--yZTlQZk1--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://storage.googleapis.com/zenn-user-upload/deployed-images/4a6b72784ab00c8e5d1ad2c2.png%3Fsha%3D13295712d1e80ec08b0ac78bea9f6c413386d632)

使用する基盤モデルについて
=============

本記事で紹介するアーキテクチャは、特定の基盤モデルに依存しない汎用的なものではありますが、今回の PoC では [Anthropic](https://www.anthropic.com/) 社が提供する [Claude](https://www.anthropic.com/claude) というモデルを使用しています。理由としては、基盤モデル呼び出しにかかるコストが比較的安く、日本語を扱う場合の精度も良いからというものです。今回の取り組みの目的がオペレーション業務効率化による人的コストの削減であったため、精度を追い求めるというよりはコストを安く抑えられることを重視しました。

モデルの選択も重要ですが、基盤モデル呼び出しでは入出力トークン数がコストに跳ねてくるため、なるべく不要なプロンプト指示文は入れない、余計な出力結果は生成させない、といったプロンプト上の工夫も必要になります。

プロンプトの中身について詳細には立ち入りませんが、実際に Anthropic Claude モデルへのプロンプトを考える上で以下の記事をかなり参考にさせて頂いたので、併せて紹介させて頂きます。

<https://qiita.com/kiiwami/items/4a62a3dcbedeb141e605>

DynamoDB テーブル設計
===============

上記のアーキテクチャで登場する 3 つの DynamoDB テーブルについて以下に説明します。

* **executions** テーブル
* **requests** テーブル
* **prompt\_templates** テーブル

ER 図で表現すると、以下のようになります。各テーブルカラムの 2 列目、3 列目はそれぞれ型、キーの種類を示しています。

![](https://res.cloudinary.com/zenn/image/fetch/s--jjM82GKJ--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://storage.googleapis.com/zenn-user-upload/deployed-images/9c1b6ae4c39a1b46f24b3f92.png%3Fsha%3Df01eb4f10fa928c69bb93053d6f53344ec2919cc)

prompt\_templates テーブル
----------------------

プロンプトの Jinja テンプレートを保存・管理するテーブルです。タスク名とプロンプトバージョンを指定すると、テンプレートの中身が一意に定ります。後述の requests テーブルから取得したリクエストに含まれる `input_value` を埋め込んでレンダリングします。

| カラム名 | 型 | キー | 説明 |
| --- | --- | --- | --- |
| **task\_name** | S | PK | LLM に解かせるタスクの名称 |
| **prompt\_version** | S | SK | プロンプトバージョン |
| **prompt\_template** | S | - | プロンプトの Jinja テンプレート |

executions テーブル
---------------

特定のレコードセット全体に対する処理実行のメタ情報を格納するテーブルです。実行 ID を指定すると、各実行の処理内容を決定するメタ情報である Payload が一意に定ります。Payload には、タスク名・プロンプトバージョン、および呼び出し対象となる基盤モデル ID を持たせます。

| カラム名 | 型 | キー | 説明 |
| --- | --- | --- | --- |
| **execution\_id** | S | PK | 実行 ID |
| **payload** | M | - | 各実行の処理内容を決定するメタ情報 |

requests テーブル
-------------

基盤モデル呼び出しのリクエスト単位を格納するテーブルです。処理実行毎のレコードと 1:1 の関係になります。実行 ID を辿ってプロンプトテンプレートを取得し、入力値を埋め込むことで、基盤モデル呼び出し時のリクエスト内容を決定できます。

| カラム名 | 型 | キー | 説明 |
| --- | --- | --- | --- |
| **request\_id** | S | PK | リクエスト ID |
| **execution\_id** | S | - | 実行 ID |
| **record\_id** | S | - | レコード ID |
| **input\_value** | S | - | 基盤モデルへの入力値 |

また、requests テーブルには [DynamoDB Streams](https://docs.aws.amazon.com/ja_jp/amazondynamodb/latest/developerguide/Streams.html) を設定して、INSERT イベントが発生する度にリクエスト処理用の Lambda 関数を呼び出すようにしています。DynamoDB Streams に関しては以下の記事でも解説しているため、もし良ければ併せてご覧ください。

<https://zenn.dev/simpleform_blog/articles/20240427-01-dynamodb-streams-with-terraform>

プロンプトのバージョン管理について
=================

本記事のアーキテクチャにおいて、基盤モデルへの呼び出しを行うのは Lambda 関数であるため、Lambda 関数のソースコードにプロンプト文字列もハードコードするのが一番簡単ではありますが、プロンプト変更のためだけに Lambda 関数を毎回デプロイし直すのは運用効率が良くありません。また、LLM で実現したいことは同じでも、プロンプトを少しずつ変えて出力結果の精度を比較したいということもあるかもしれません。

そこで、プロンプトはバージョン情報とともに、Lambda 関数のスクリプトとは切り離して管理することにしました。保存・管理する場所として今回は DynamoDB テーブルを使用しており、これが先述の prompt\_templates テーブルです。

![](https://res.cloudinary.com/zenn/image/fetch/s--NxkYKQqx--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://storage.googleapis.com/zenn-user-upload/deployed-images/6d78e7d5803c03e00b33853e.png%3Fsha%3D264654bc532bb8e540b1bee159df1788a090d7ab)

ハードコードする場合であれば Python スクリプト内の f-strings で動的なプロンプト生成ができますが、外部で管理する場合は文字列として取得してしまうので、Python テンプレートエンジンである [Jinja](https://jinja.palletsprojects.com/en/) を使用して動的な生成を実現します。

Lambda 関数の実装
============

ここからは実際に基盤モデルの呼び出しを行う、リクエスト処理用 Lambda 関数の実装について説明します。

以下はハンドラスクリプトの全体像です。各処理について以降で説明していきます。

Lambda 関数ハンドラスクリプト
main.py
```
from .modules.models import (
    Request,
    Result,
)
from .modules.utils import (
    get_execution_payload,
    get_prompt_template,
    render_prompt_template,
    invoke_model,
    upload_result_to_s3,
)

def handler(event, context):
    records = event.get("Records", [])

    results = []
    for record in records:
        # DynamoDB Streams におけるイベントが INSERT でない場合は処理をスキップ
        if record.get("eventName") != "INSERT":
            continue

        # 1. リクエスト情報および実行ペイロードの取得
        new_image = record.get("dynamodb", {}).get("NewImage")
        request_id = new_image.get("request_id", {}).get("S")
        execution_id = new_image.get("execution_id", {}).get("S")
        record_id = new_image.get("record_id", {}).get("S")
        input_value = new_image.get("input_value", {}).get("S")

        if isinstance(input_value, tuple):
            input_value = input_value[0]
        
        execution_payload = get_execution_payload(
            execution_id=execution_id
        )

        # 2. プロンプト生成
        prompt_template = get_prompt_template(
            task_name=execution_payload.task_name,
            prompt_version=execution_payload.prompt_version,
        )
        prompt = render_prompt_template(
            prompt_template=prompt_template,
            input_value=input_value,
        )

        # 3. 基盤モデル呼び出し
        request = Request(
            request_id=request_id,
            foundation_model_id=execution_payload.foundation_model_id,
            prompt=prompt,
        )
        response = invoke_model(request=request)

        # 4. 結果レコードの生成・保存
        result = Result(
            request_id=request_id,
            record_id=record_id,
            task_name=execution_payload.task_name,
            prompt_version=execution_payload.prompt_version,
            input_value=input_value,
            response=response,
        )
        results.append(result.model_dump())

        upload_result_to_s3(
            result=result,
            exexution_id=execution_id,
            request_id=request_id,
        )

    return {
        "statusCode": 200,
        "body": {
            "Records": records,
            "Results": results,
        }
    }


```

!

簡単のため、基盤モデル呼び出し以外のエラーハンドラリング実装は割愛していますので、必要に応じて追加頂ければと思います。

1. リクエスト情報および実行ペイロードの取得
-----------------------

DynamoDB Streams から流れてくるストリームレコードを for 文でそれぞれ処理します。NewImage からリクエスト情報を取得します。リクエスト情報に含まれる `execution_id` を使用して、executions テーブルから実行 Payload を取得します。

main.py
```
# リクエスト情報の取得
new_image = record.get("dynamodb", {}).get("NewImage")
request_id = new_image.get("request_id", {}).get("S")
execution_id = new_image.get("execution_id", {}).get("S")
record_id = new_image.get("record_id", {}).get("S")
input_value = new_image.get("input_value", {}).get("S")

if isinstance(input_value, tuple):
    input_value = input_value[0]

# 実行 Payload の取得
execution_payload = get_execution_payload(
    execution_id=execution_id
)

```
modules / utils.py
modules/utils.py
```
import os
import boto3

dynamodb_client = boto3.client(service_name="dynamodb")

def get_execution_payload(execution_id: str, table_name: str) -> ExecutionPayload:
    response = dynamodb_client.get_item(
        TableName=os.environ["EXECUTIONS_TABLE_NAME"],
        Key={"execution_id": {"S": execution_id}}
    )
    payload_map = response["Item"]["Payload"]["M"]
    logger.info(payload_map)
    execution_payload = ExecutionPayload(
        task_name=payload_map["task_name"]["S"],
        prompt_version=payload_map["prompt_version"]["S"],
        foundation_model_id=payload_map["foundation_model_id"]["S"]
    )
    return execution_payload

```

modules / models.py
modules/models.py
```
from pydantic import BaseModel

class ExecutionPayload(BaseModel):
    task_name: str
    prompt_version: str
    foundation_model_id: str

```

2. プロンプト生成
----------

実行 Payload に含まれるタスク名とプロンプトバージョンを使用して、prompt\_templates テーブルからプロンプトテンプレートを取得します。取得した Jinja テンプレートに、処理対象レコードの `input_value` の値を組み込んでレンダリングし、プロンプトを生成します。

main.py
```
prompt_template = get_prompt_template(
    task_name=execution_payload.task_name,
    prompt_version=execution_payload.prompt_version,
)
prompt = render_prompt_template(
    prompt_template=prompt_template,
    input_value=input_value,
)

```
modules / utils.py
modules/utils.py
```
import os
import boto3
from jinja2 import Template

dynamodb_client = boto3.client(service_name="dynamodb")

def get_prompt_template(task_name: str, prompt_version: str, table_name: str) -> Template:
    response = dynamodb_client.get_item(
        TableName=os.environ["PROMPT_TEMPLATES_TABLE_NAME"],
        Key={
            "task_name": {"S": task_name},
            "prompt_version": {"S": prompt_version},
        }
    )
    prompt_template_source = response["Item"]["prompt_template"]["S"]
    return Template(source=prompt_template_source)

def render_prompt_template(prompt_template: Template, input_value: str) -> str:
    return prompt_template.render({"input_value": input_value})

```

3. 基盤モデル呼び出し
------------

基盤モデルへの呼び出し時に使用する request オブジェクトをインスタンス化します。これを使用して基盤モデルへの呼び出しを実行します。

main.py
```
request = Request(
    request_id=request_id,
    foundation_model_id=execution_payload.foundation_model_id,
    prompt=prompt,
)
response = invoke_model(request=request)

```
modules / models.py
modules/models.py
```
from pydantic import BaseModel

class Request(BaseModel):
    request_id: str
    foundation_model_id: str
    prompt: str

```

modules / utils.py
modules/utils.py
```
import json
import boto3

bedrock_client = boto3.client(service_name="bedrock-runtime", region_name="us-east-1")


def invoke_model(request: Request) -> str:
    body = json.dumps({
        "prompt": request.prompt,
        "max_tokens_to_sample": 1000,
    })
    response = bedrock_client.invoke_model(
        modelId=request.foundation_model_id,
        accept="application/json",
        contentType="application/json",
        body=body
    )
    response_body = json.loads(response.get('body').read())
    completion = response_body.get('completion')

    try:
        output_text = completion.split("<output>")[1].split("</output>")[0]
        output_data = json.loads(output_text)
        return {
            "statusCode": 200,
            "body": {"OutputData": output_data}
        }

    except Exception as e:
        logger.error(e)
        return {
            "statusCode": 500,
            "body": {
                "Error": str(e),
                "Completion": completion
            }
        }

```

上記の utils.py に含まれる `invoke_model()` 関数実装のうち、以下が Amazon Bedrock 基盤モデルを直接的に呼び出している部分です。出力結果が安定しないことも考慮して、エラーハンドリングの中で処理できなかった場合でもステータスコードやエラー内容、出力結果を response として返却しています。

```
body = json.dumps({"prompt": request.prompt, "max_tokens_to_sample": 1000})

response = bedrock_client.invoke_model(
    modelId=request.foundation_model_id,
    accept="application/json",
    contentType="application/json",
    body=body
)

```

4. 結果レコードの生成・保存
---------------

一連の基盤モデル呼び出し処理に関する情報を、結果レコードとして保存します。処理結果を含む response とともに、result オブジェクトをインスタンス化し、スプレッドシートへの処理結果の書き戻しとは別に、Athena 等で分析しやすいよう S3 にも結果レコードを保存してます。

main.py
```
result = Result(
    request_id=request_id,
    record_id=record_id,
    task_name=execution_payload.task_name,
    prompt_version=execution_payload.prompt_version,
    foundation_model_id=execution_payload.foundation_model_id,
    input_value=input_value,
    response=response,
)
results.append(result.model_dump())

upload_result_to_s3(
    result=result,
    exexution_id=execution_id,
    request_id=request_id,
)

```
modules / models.py
modules/models.py
```
from pydantic import BaseModel

class Response(BaseModel):
    statusCode: int
    body: dict

class Result(BaseModel):
    request_id: str
    record_id: str
    task_name: str
    prompt_version: str
    foundation_model_id: str
    input_value: str
    response: Response

```

modules / utils.py
modules/utils.py
```
import os
import boto3

BUCKET_NAME = os.environ["BUCKET_NAME"]

def upload_result_to_s3(result: Result, exexution_id: str, request_id: str, bucket_name: str:
    result_json_string = json.dumps(result.model_dump(), ensure_ascii=False)
    result_json_bytes = result_json_string.encode("utf-8")
    result_s3_key = os.path.join(
        "results",
        f"exexution_id={exexution_id}",
        f"{request_id}.json"
    )
    # Upload to S3
    s3_client.put_object(Bucket=BUCKET_NAME, Key=result_s3_key, Body=result_json_bytes)
    return

```

実装についての説明は以上です。

さいごに
====

Amazon Bedrock を業務オペレーションに組み込んでみる PoC についてご紹介してみました。いかがでしたでしょうか。

以前の [Neptune ML の記事](https://zenn.dev/simpleform_blog/articles/20240304-01-neptune-ml-recommendation) の結びでも書きましたが、AI/ML の専門知識がなくてもこれらの技術を簡単に始められるのはクラウドサービスならではという感じがします。

PoC の価値検証はこれからですが、LLM 処理結果の目視による校正履歴などの情報を活用すれば、プロンプトの継続的な改善などに活かせそうです。しばらく試運転してみて知見など溜まってきたらまたアウトプットしてみたいと思います。

最後まで読んで頂き、ありがとうございました。

[![](https://storage.googleapis.com/zenn-user-upload/avatar/e6a6f4218e.jpeg)](/p/simpleform_blog)SimpleForm Tech Blog により固定

シンプルフォームでは、新しい技術開発にスピーディに挑戦し続けています。積極採用中ですので、少しでも興味を持っていただいた方は、ぜひカジュアルにお話させてください！

* [シンプルフォーム株式会社の求人一覧](https://herp.careers/v1/simpleform)
* [SimpleFormカジュアル面談お申込みフォーム](https://docs.google.com/forms/d/e/1FAIpQLSdhna6Rz0VgXEH1sKOgduHnddWxBb4utLKfWrtSAKIPNbatYQ/viewform)
[![Hiroki Yamagishi / 山岸 裕樹](https://storage.googleapis.com/zenn-user-upload/avatar/72dd3e5170.jpeg)](/yamagishihrd)[Hiroki Yamagishi / 山岸 裕樹](/yamagishihrd)

インフラエンジニア @SimpleForm\_Inc ← NTT Data ／ Snowflake Squad 2024 ❄️ ／ AWS 認定 14 冠 ／ 本アカウントでの発信は、所属する組織を代表するものではありません。

[![SimpleForm Tech Blog](https://storage.googleapis.com/zenn-user-upload/avatar/e6a6f4218e.jpeg)](/p/simpleform_blog)[SimpleForm Tech Blog](/p/simpleform_blog)[Publication](/faq#what-is-publication)

リアルタイム法人調査システム「SimpleCheck」を開発・運営するシンプルフォーム株式会社の開発チームのメンバーが、日々の開発で得た知見や試してみた技術などについて発信していきます。
Publication 運用への移行前の記事は [zenn.dev/simpleform](https://zenn.dev/simpleform) からご覧ください。

バッジを贈って著者を応援しよう

バッジを受け取った著者にはZennから現金やAmazonギフトカードが還元されます。

バッジを贈る