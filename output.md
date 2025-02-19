![AWS SAM を使ってテンプレートからサーバーレスな環境を構築するハンズオンをやってみた](https://devio2023-media.developers.io/wp-content/uploads/2019/11/aws-eyecatch.png)

AWS SAM を使ってテンプレートからサーバーレスな環境を構築するハンズオンをやってみた
=============================================

[#ハンズオン](/tags/hands-on/)[#AWS SAM](/tags/aws-sam/)[#AWS SAM CLI](/tags/aws-sam-cli/)[#AWS](/tags/aws/)[![大村 保貴](https://devio2023-media.developers.io/wp-content/uploads/devio_thumbnail/2024-06/ohmura-yasutaka.png)

大村 保貴](/author/ohmura-yasutaka/)[![facebook logo](/img/sns/facebook.svg)](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fdev.classmethod.jp%2Farticles%2Faws-hands-on-for-beginners-serverless2%2F&t=AWS%20SAM%20%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E3%83%86%E3%83%B3%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88%E3%81%8B%E3%82%89%E3%82%B5%E3%83%BC%E3%83%90%E3%83%BC%E3%83%AC%E3%82%B9%E3%81%AA%E7%92%B0%E5%A2%83%E3%82%92%E6%A7%8B%E7%AF%89%E3%81%99%E3%82%8B%E3%83%8F%E3%83%B3%E3%82%BA%E3%82%AA%E3%83%B3%E3%82%92%E3%82%84%E3%81%A3%E3%81%A6%E3%81%BF%E3%81%9F%20%7C%20DevelopersIOhttps%3A%2F%2Fdev.classmethod.jp%2Farticles%2Faws-hands-on-for-beginners-serverless2%2F&t=AWS%20SAM%20%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E3%83%86%E3%83%B3%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88%E3%81%8B%E3%82%89%E3%82%B5%E3%83%BC%E3%83%90%E3%83%BC%E3%83%AC%E3%82%B9%E3%81%AA%E7%92%B0%E5%A2%83%E3%82%92%E6%A7%8B%E7%AF%89%E3%81%99%E3%82%8B%E3%83%8F%E3%83%B3%E3%82%BA%E3%82%AA%E3%83%B3%E3%82%92%E3%82%84%E3%81%A3%E3%81%A6%E3%81%BF%E3%81%9F%20%7C%20DevelopersIO)[![hatena logo](/img/sns/hatena.svg)](https://b.hatena.ne.jp/add?mode=confirm&url=https%3A%2F%2Fdev.classmethod.jp%2Farticles%2Faws-hands-on-for-beginners-serverless2%2F&title=AWS%20SAM%20%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E3%83%86%E3%83%B3%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88%E3%81%8B%E3%82%89%E3%82%B5%E3%83%BC%E3%83%90%E3%83%BC%E3%83%AC%E3%82%B9%E3%81%AA%E7%92%B0%E5%A2%83%E3%82%92%E6%A7%8B%E7%AF%89%E3%81%99%E3%82%8B%E3%83%8F%E3%83%B3%E3%82%BA%E3%82%AA%E3%83%B3%E3%82%92%E3%82%84%E3%81%A3%E3%81%A6%E3%81%BF%E3%81%9F%20%7C%20DevelopersIOhttps%3A%2F%2Fdev.classmethod.jp%2Farticles%2Faws-hands-on-for-beginners-serverless2%2F&t=AWS%20SAM%20%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E3%83%86%E3%83%B3%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88%E3%81%8B%E3%82%89%E3%82%B5%E3%83%BC%E3%83%90%E3%83%BC%E3%83%AC%E3%82%B9%E3%81%AA%E7%92%B0%E5%A2%83%E3%82%92%E6%A7%8B%E7%AF%89%E3%81%99%E3%82%8B%E3%83%8F%E3%83%B3%E3%82%BA%E3%82%AA%E3%83%B3%E3%82%92%E3%82%84%E3%81%A3%E3%81%A6%E3%81%BF%E3%81%9F%20%7C%20DevelopersIO)[![twitter logo](/img/sns/twitter.svg)](https://twitter.com/intent/tweet?original_referer=https://dev.classmethod.jp/articles/aws-hands-on-for-beginners-serverless2/&text=%23DevelopersIO%20AWS%20SAM%20%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E3%83%86%E3%83%B3%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88%E3%81%8B%E3%82%89%E3%82%B5%E3%83%BC%E3%83%90%E3%83%BC%E3%83%AC%E3%82%B9%E3%81%AA%E7%92%B0%E5%A2%83%E3%82%92%E6%A7%8B%E7%AF%89%E3%81%99%E3%82%8B%E3%83%8F%E3%83%B3%E3%82%BA%E3%82%AA%E3%83%B3%E3%82%92%E3%82%84%E3%81%A3%E3%81%A6%E3%81%BF%E3%81%9F%20https%3A%2F%2Fdev.classmethod.jp%2Farticles%2Faws-hands-on-for-beginners-serverless2%2F&t=%23DevelopersIO%20AWS%20SAM%20%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E3%83%86%E3%83%B3%E3%83%97%E3%83%AC%E3%83%BC%E3%83%88%E3%81%8B%E3%82%89%E3%82%B5%E3%83%BC%E3%83%90%E3%83%BC%E3%83%AC%E3%82%B9%E3%81%AA%E7%92%B0%E5%A2%83%E3%82%92%E6%A7%8B%E7%AF%89%E3%81%99%E3%82%8B%E3%83%8F%E3%83%B3%E3%82%BA%E3%82%AA%E3%83%B3%E3%82%92%E3%82%84%E3%81%A3%E3%81%A6%E3%81%BF%E3%81%9F%20)![Clock Icon](/img/clock.svg)2021.11.16

この記事は公開されてから1年以上経過しています。情報が古い可能性がありますので、ご注意ください。

前回の[サーバーレスアーキテクチャで翻訳 Web API を構築するハンズオンをやってみた](https://dev.classmethod.jp/articles/aws-hands-on-for-beginners-serverless1/)に引き続き**初心者向けのハンズオンをやってみました。**

以下の構成をSAM（Serverless Application Model）を使って構築します。前回のハンズオン（AWS Hands-on for Beginners Serverless #1）で手作業で構築した内容を第2段では**SAMを使ってモダンで便利な構築方法を体験しよう**といった内容でした。

[![](https://devio2023-media.developers.io/wp-content/uploads/2021/11/2021-11-16-20-49-01.png)](https://dev.classmethod.jp/wp-content/uploads/2021/11/2021-11-16-20-49-01.png)

画像引用: ハンズオンのアンケート回答後にダウンロードできる資料より

やってみた感想
-------

* SAMを体験したい**だけ**なら1回目のハンズオンを実施しなくても問題なく進められる内容でした
* 1回目のハンズオンは手作業によるデプロイなので**「SAMって、あぁ便利だなぁ」をより味わうためにも1回目のハンズオンするのがオススメです**
* API Gateway + Lambda + Transrate + DynamoDBの連携については1回目のハンズオンで詳しく説明されています
* AWS SAM CLIがGeneral Availableする前の収録のこともあり、バージョンの違いによる多少の差はありますが作業には支障ありませんでした（SAM CLI 1.35.0で動作確認）
  + オプションとなっている最後のパートでしか使いません
* ハンズオンを完走するまでの所要時間は約2時間でした。私はいじって遊んで寄り道しながら進めました。もっと早く終わるはずです。

**ハンズオン記事のリンク**

* [AWS Hands-on for Beginners Serverless #2](https://pages.awscloud.com/event_JAPAN_Ondemand_Hands-on-for-Beginners-Serverless-2_LP.html?trk=aws_introduction_page)

**ハンズオン1回目のやってみた記事**

AWS Hands-on for Beginners とは
-----------------------------

ハンズオン動画を見ながら**実際に手を動かして**学ぶAWSが提供しているコンテンツです。

**AWS Hands-on for Beginners シリーズのリンク**

* [ハンズオン資料 | AWS クラウドサービス活用資料集](https://aws.amazon.com/jp/aws-jp-introduction/aws-jp-webinar-hands-on/?trk=aws_blog)

AWS Hands-on for Beginners Serverless #2
----------------------------------------

本テーマの「AWS SAM を使ってテンプレートからサーバーレスな環境を構築する」は座学パートと、ハンズオンパートで構成されています。ハンズオンパートの内容をアレンジして学びました。arm64（Graviton2）のLambdaにしたり、DynamoDBをオンデマンドに変更したりしたので変更した内容を残しておきます。ちょうど同じ箇所を変更したいという方がいましたら参考になるかと思います。

* [AWS Lambdaがarm64アーキテクチャをサポートしました | DevelopersIO](https://dev.classmethod.jp/articles/aws-lambda-graviton2/)

座学パート
-----

動画を見て丁寧な説明を聞きます。

1 前回のハンズオンの復習と今回のハンズオンの概要

2 AWS SAM の紹介と AWS Cloud9 の紹介

ハンズオンパート
--------

### 3. Cloud9 のセットアップ + [Option] Cloud9 で簡単な Lambda 関数を作成する

Cloud9のセットアップします。私はローカル端末で進めたいのでほぼスキップ。以下ハンズオン時のローカル環境です。

| 項目 | 値 |
| --- | --- |
| macOS | 11.6 |
| aws cli | 2.3.0 |
| SAM CLI | 1.35.0 |

### 4.　SAM で Lambda 関数を作成する ①

ここからが本題のSAMの利用です。シンプルなLambdaの作成とSAMでデプロイまでします。

ハンズオンで利用していくS3バケットを作成。

```

$ aws s3 mb s3://hands-on-serverless-2-ohmura

```

Python3.9に変更したり、arm64（Graviton2）にしてみたりと設定変更、追加してみました。

```

AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Description: AWS Hands-on for Beginners - Serverless 2
Resources:
  TranslateLambda:
    Type: AWS::Serverless::Function
    Properties:
      FunctionName: translate-function-2
      CodeUri: ./translate-function
      Handler: translate-function.lambda_handler
      Runtime: python3.9
      Architectures: [ arm64 ]
      Timeout: 5
      MemorySize: 256

```

ローカルにあるファイル郡をパッケージングします。

```

$ aws cloudformation package \
      --template-file template.yaml \
      --s3-bucket hands-on-serverless-2-ohmura \
      --output-template-file packaged-template.yaml

Uploading to 87fc21625bbc38bd7d637bd60d942b51  310 / 310.0  (100.00%)
Successfully packaged artifacts and wrote output template to file packaged-template.yaml.
Execute the following command to deploy the packaged template

```

S3バケットにファイルが生成されました。

```

$ s3-tree hands-on-serverless-2-ohmura
hands-on-serverless-2-ohmura
└── 87fc21625bbc38bd7d637bd60d942b51

0 directories, 1 file

```

ローカルの同ディレクトリ内には新たに生成された`packaged-template.yaml`があります。`template.yaml`の内容から`CodeUri`の参照先がS3バケット上のファイル名が変更された様なファイルです。その他には**Architectures:**の設定値が`template.yaml`で設定したリスト形式と異なる書式に変換されていました。

```

AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Description: AWS Hands-on for Beginners - Serverless 2
Resources:
  TranslateLambda:
    Type: AWS::Serverless::Function
    Properties:
      FunctionName: translate-function-2
      CodeUri: s3://hands-on-serverless-2-ohmura/87fc21625bbc38bd7d637bd60d942b51
      Handler: translate-function.lambda_handler
      Runtime: python3.9
      Architectures:
      - arm64
      Timeout: 5
      MemorySize: 256

```

デプロイします。約3分でデプロイ完了しました。

```

$ aws cloudformation deploy \
     --template-file ./packaged-template.yaml \
     --stack-name hands-on-serverless-2 \
     --capabilities CAPABILITY_IAM

```

デプロイされたLambda関数を確認してみます。

```

$ aws lambda get-function --function-name translate-function-2

```

設定追加した設定値も含めデプロイできています。

```

{
    "Configuration": {
        "FunctionName": "translate-function-2",
        "FunctionArn": "arn:aws:lambda:ap-northeast-112345679012:function:translate-function-2",
        "Runtime": "python3.9",
        "Role": "arn:aws:iam:12345679012:role/hands-on-serverless-2-TranslateLambdaRole-1F8ZWSEW25E4E",
        "Handler": "translate-function.lambda_handler",
        "CodeSize": 310,
        "Description": "",
        "Timeout": 5,
        "MemorySize": 256,
        "LastModified": "2021-11-14T12:56:52.289+0000",
        "CodeSha256": "IEgPx+U6c61402Tl7pT01nuov8sdyEAmjc87AVbtzKM=",
        "Version": "$LATEST",
        "TracingConfig": {
            "Mode": "PassThrough"
        },
        "RevisionId": "c14ac138-be47-43c3-ba45-2c78c039e799",
        "State": "Active",
        "LastUpdateStatus": "Successful",
        "PackageType": "Zip",
        "Architectures": [
            "arm64"
        ]
    },
    "Code": {
        "RepositoryType": "S3",
        "Location": "https://awslambda-ap-ne-1-tasks.s3.ap-northeast-1.amazonaws.com/snapshots/060238338506/translate-function-2-1d8a32b2-b460-4d7b-9f77-fd0bf163929c?versionId=mBAHU4_cM2FBcJCN63TGOL_sh_IfD3XQ&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaDmFwLW5vcnRoZWFzdC0xIkgwRgIhAL168IEYC32KzhRpWhaZePn3o6eiSVf1ITsDXXf6%2BIVlAiEAinde3yPE%2F27NS1qzfGF2tDQCD4y%2Fn1KyWjSqjEzWT1MqhAQIXhACGgw5MTk5ODA5MjUxMzkiDN5dJ6BrtiFEtPwHMCrhA7DS0M4CV35esnN2TPKCaz56ClDuL%2Bs%2FBkrJMV2fJtyAvevZ%2Bn
%2FO8bsKJgb3RjZgWtIm8mriP%2FY17PKfP1kZr0p4ECtuteEJbp5nNY5boUr65Wn4IGnW0zqafcJStki04F4q%2BoCsadW7AkFPfgDow6NGegScSm2RehNt9AVoUQeLmshWxq5cJjefZEEGtxKWUCtj64VSV4H3zQB9IAMcWLWybSjr0CsGF7zBBtsuMMdlgGEHMnqjzM8IMQO8MAQxtS7Lwzl7Jx5qdxFgwbTrFBNwdyk2jKixC70C6Eodl3O6gTM%2B%2FKZCqOhZ3ERjZ08c8GycDfz82XlRIMLhDK3QQc2mvPU2hOL0Vw7OjhWFrqQJOJNJtzO57EEuVGdvRJ47mTvVx0TTqQ311OdUpfiwc0ndpy6VKkwDshxCGrw%2FCggdWuY5L4DkyVEMxGqDtS6QmIqE28lwS03sx0QbW%2BFI5wv%2FRM6WCNm%2F2G7gKywu2IBhz5PsKBWGMiTk0Azk8UUrVAittUhZvrF%2BMrnhqPr%2B7Sap4mZlSnRVjrA%2BvTTq7FWtjSIpDj1YCv1hD%2FZEHpSP7qgjlaUCFcvkuOHiVHAyq6n5o5bi426tGRtje9itL1Nq1AA3oLnu6CCGe4deRZk2S%2Bow%2FIDEjAY6pAEPq2zrbmvjQ%2FdMuJfl%2BigqSIBpWlOrqcd4zbyJRdv98ATQcrXAdbekwRt5xxQ%2FxJI6qtqkicuX42NOZoqy3Oh5G3D2qfHMZbm1wNC0oYh65Cy3h83xSxlR4QkwegkOmNeyg3KkDyAbTs3L%2FeZ69efiofPYyHHUxEH2ryGGdNXgaxuuv%2FsotveHbzE%2Fo0mxQ%2FRxFyc65h6VpRAqcS662td5Cryd0w%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20211114T130619Z&X-Amz-SignedHeaders=host&X-Amz-Expires=600&X-Amz-Credential=ASIA5MMZC4DJZCTDCD7R%2F20211114%2Fap-northeast-1%2Fs3%2Faws4_request&X-Amz-Signature=15651246675fe1f955f36a316bac0789f95b6a8992368fa125c67fe78049c5af"
    },
    "Tags": {
        "aws:cloudformation:stack-name": "hands-on-serverless-2",
        "lambda:createdBy": "SAM",
        "aws:cloudformation:stack-id": "arn:aws:cloudformation:ap-northeast-112345679012:stack/hands-on-serverless-2/8a87d690-4549-11ec-a6b6-0aafff1b4c1f",
        "aws:cloudformation:logical-id": "TranslateLambda"
    }
}

```

テスト実行し無事成功。

[![](https://devio2023-media.developers.io/wp-content/uploads/2021/11/2021-11-14-22-34-531.png)](https://dev.classmethod.jp/wp-content/uploads/2021/11/2021-11-14-22-34-531.png)

```

{
  "statusCode": 200,
  "body": "\"Hello Hands on world!\""
}

```
### 5. SAM で Lambda 関数を作成する ②

LambdaとTranslateを連携させる章です。SAMでデプロイします。

`arm64`のリスト表記を変更してみました。

```

AWSTemplateFormatVersion: "2010-09-09"
Transform: AWS::Serverless-2016-10-31
Description: AWS Hands-on for Beginners - Serverless 2
Resources:
  TranslateLambda:
    Type: AWS::Serverless::Function
    Properties:
      FunctionName: translate-function-2
      CodeUri: ./translate-function
      Handler: translate-function.lambda_handler
      Runtime: python3.9
      Architectures:
        - arm64
      Timeout: 5
      MemorySize: 256
      Policies:
        - TranslateFullAccess


```

パッケージングします。

```

$ aws cloudformation package \
      --template-file template.yaml \
      --s3-bucket hands-on-serverless-2-ohmura \
      --output-template-file packaged-template.yaml

```

生成された`packaged-template.yaml`はそのままでした。気になったところはリスト表記していた箇所のインデントが上がって、左にシフトしてます。`Policies:`で指定したIAMポリシーも同様です。

```

AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Description: AWS Hands-on for Beginners - Serverless 2
Resources:
  TranslateLambda:
    Type: AWS::Serverless::Function
    Properties:
      FunctionName: translate-function-2
      CodeUri: s3://hands-on-serverless-2-ohmura/ed6b5890ac5124ee2c4b84290198df81
      Handler: translate-function.lambda_handler
      Runtime: python3.9
      Architectures:
      - arm64
      Timeout: 5
      MemorySize: 256
      Policies:
      - TranslateFullAccess


```
### 6. SAM で API Gateway のリソースを作成し、Lambda 関数と連携させる

SAMでAPI Gatewayも作成し、前の章で作成したLambda + Tranlateと連携します。

今回も`arm64`と`Python 3.9`に変更、追加した`temlate.yaml`を載せておきます。

```

AWSTemplateFormatVersion: "2010-09-09"
Transform: AWS::Serverless-2016-10-31
Description: AWS Hands-on for Beginners - Serverless 2
Resources:
  TranslateLambda:
    Type: AWS::Serverless::Function
    Properties:
      FunctionName: translate-function-2
      CodeUri: ./translate-function
      Handler: translate-function.lambda_handler
      Runtime: python3.9
      Architectures:
        - arm64
      Timeout: 5
      MemorySize: 256
      Policies:
        - TranslateFullAccess
      Events:
        GetApi:
          Type: Api
          Properties:
            Path: /translate
            Method: get
            RestApiId: !Ref TranslateAPI
  TranslateAPI:
    Type: AWS::Serverless::Api
    Properties:
      Name: translate-api-2
      StageName: dev
      EndpointConfiguration: REGIONAL


```
### 7. SAM で DynamoDB TBL を作成し、Lambda 関数を連携させる

ハンズオン通りに実装しSAMでデプロイすると、WebブラウザからAPI GatewayのURLにクエリパラメータを渡すと翻訳してくれます。

[![](https://devio2023-media.developers.io/wp-content/uploads/2021/11/2021-11-15-21-37-071.png)](https://dev.classmethod.jp/wp-content/uploads/2021/11/2021-11-15-21-37-071.png)

試しやすいようにGETメソッドで実装していると1回目のハンズオンで説明されていました。
勉強かねてPOSTメソッドに変更しSAMでデプロイしてみます。ついでにDynamoDBの設定をプロビジョニングからオンデマンドに変更し、Python3.9とarm64（Graviton2）仕様にします。

* [DynamoDBのオンデマンドとプロビジョニングの料金を比較をしてみた #reinvent | DevelopersIO](https://dev.classmethod.jp/articles/reinvent2018-compare-dynamodb-on-demand-price-with-provisioned-price/)

```

AWSTemplateFormatVersion: "2010-09-09"
Transform: AWS::Serverless-2016-10-31
Description: AWS Hands-on for Beginners - Serverless 2
Resources:
  TranslateLambda:
    Type: AWS::Serverless::Function
    Properties:
      FunctionName: translate-function-2
      CodeUri: ./translate-function
      Handler: translate-function.lambda_handler
      Runtime: python3.9
      Architectures:
        - arm64
      Timeout: 5
      MemorySize: 256
      Policies:
        - TranslateFullAccess
        - AmazonDynamoDBFullAccess
      Events:
        PostApi:
          Type: Api
          Properties:
            Path: /translate
            Method: post
            RestApiId: !Ref TranslateAPI
  TranslateAPI:
    Type: AWS::Serverless::Api
    Properties:
      Name: translate-api-2
      StageName: dev
      EndpointConfiguration: REGIONAL
  TranslateDynamoDbTbl:
    Type: AWS::DynamoDB::Table
    Properties:
      BillingMode: PAY_PER_REQUEST
      TableName: translate-history-2
      AttributeDefinitions:
        - AttributeName: timestamp
          AttributeType: S
      KeySchema:
        - AttributeName: timestamp
          KeyType: HASH

```

DynamoDBは記述が大きく異るため比較をのせておきます。

```

# プロビジョニング（ハンズオンのオリジナルの記述）
  TranslateDynamoDbTbl:
    Type: AWS::Serverless::SimpleTable
    Properties:
      TableName: translate-history-2
      PrimaryKey:
        Name: timestamp
        Type: String
      ProvisionedThroughput:
        ReadCapacityUnits: 1
        WriteCapacityUnits: 1

# オンデマンドへ変更
  TranslateDynamoDbTbl:
    Type: AWS::DynamoDB::Table
    Properties:
      BillingMode: PAY_PER_REQUEST
      TableName: translate-history-2
      AttributeDefinitions:
        - AttributeName: timestamp
          AttributeType: S
      KeySchema:
        - AttributeName: timestamp
          KeyType: HASH

```

Lambdaの関数は`body`をそのまま`input_text`に入れるように修正しました。

```

import json
import boto3
import datetime

translate = boto3.client(service_name='translate')

dynamodb_translate_history_tbl = boto3.resource(
    'dynamodb').Table('translate-history-2')


def lambda_handler(event, context):

    input_text = event['body']

    response = translate.translate_text(
        Text=input_text,
        SourceLanguageCode="ja",
        TargetLanguageCode="en"
    )

    output_text = response.get('TranslatedText')

    dynamodb_translate_history_tbl.put_item(
        Item={
            "timestamp": datetime.datetime.now().strftime("%Y%m%d%H%M%S"),
            "input": input_text,
            "output": output_text
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps({
            'output_text': output_text
        }),
        'isBase64Encoded': False,
        'headers': {}
    }


```

`curl`コマンドでデータを送った結果、翻訳されて返ってきました。

```

$ curl -XPOST -d '私は網走で育ちました' https://aowtjke6s8.execute-api.ap-northeast-1.amazonaws.com/dev/translate
{"output_text": "I grew up in Abashiri"}

```
### [Option] SAM CLI を使ってみる ①

SAMのインストールと、以下のコマンドを試しました。

* sam init
* sam build
* sam vlidate

### [Option] SAM CLI を使ってみる ②

対話形式でデプロイしました。

* sam deploy --guided

ローカル環境でLambdaの実行テストしたいときの方法を紹介。

* sam local start-lambda
* sam local start-api

### クリーンアップ & 落ち穂拾い & まとめ

* 作成してきたリソースのお片付け
* 今回設定したSAMの`template.yamll`の補足説明。

おわりに
----

AWS Hands-on for Beginners Serverless #1に引き続き行き詰まる要素はなくスムーズに進めることができました。SAMって聞いたことあるけど使ったことないという方にはサクッと体験できるのでオススメです。もちろん「SAMってなにそれ？」の方でもつまづくことなく体験できて、便利だから今度使ってみようかなという気にさせてくれます。

SAMの新しい機能は私もまだ試したことがないのですが、ご興味ある方はハンズオン後に応用でいかがでしょうか。

参考
--

* [AWS Lambda の Arm64 対応試してみた](https://shogo82148.github.io/blog/2021/10/01/arm64-in-aws-lambda/)
