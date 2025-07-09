# ローカルLLMを利用したAIコードアシスタントのすすめ

本投稿は  [TECOTEC Advent Calendar 2024](https://qiita.com/advent-calendar/2024/tecotec) の20日目の記事です。

次世代デジタル基盤開発事業部の椎葉です。最近はエンジニアとしてGoやNext.jsを使用したWebアプリケーションの設計開発に関わっています。

---

さて、昨今は業務でも生成AIサービスの活用が当たり前になってきました。直近のプロジェクトも生成AIの利用が好まれる土壌で、コーディングやコードレビュー、テストケースや資料作成など様々な工程に生成AIサービスを利用しています。

![](https://cdn-ak.f.st-hatena.com/images/fotolife/t/teco_tshiiba/20241201/20241201182316.png)

ですが一方で、ChatGPTを始めとした外部Webサービスは、コンプライアンスなどの観点から利用が難しい場合もあります。

例として、ChatGPTやClaudeは会話内容などを必要に応じて取得・利用する規約となっており、
業務で利用する場合は機密情報やセキュリティリスクとなる内容を送信しないよう注意が必要です。

* <https://openai.com/policies/row-privacy-policy/>

```
User Content: We collect Personal Data that you provide in the input to our Services (“Content”), including your prompts and other content you upload, such as files⁠(opens in a new window), images⁠(opens in a new window), and audio⁠(opens in a new window), depending on the features you use.
(引用 : 2024-11-29)
```

* <https://www.anthropic.com/legal/privacy>

```
Inputs and Outputs: Our AI services allow you to prompt the Services in a variety of media including but not limited to the format of text, files and documents, photos and images, and other materials along with the metadata and other information contained therein (“Prompts” or "Inputs"), which generate responses (“Outputs” or “Completions”) based on your Inputs. If you include personal data in your Inputs, we will collect that information and this information may be reproduced in your Outputs.
(引用 : 2024-11-29)
```

もっとも、チャットならプロンプトに機密情報を含めないよう慎重に利用すればよいですが、[GitHub Copilot](https://github.com/features/copilot)を始めとしたコードアシスタントなど、AIが能動的にデータを読み取るサービスでは、“気をつけて利用する”という運用は現実的ではありません。

個々の作業者のワークスペースから読み取られる都合上、システム管理者が統括して機密性を担保することも困難です。[\*1](#f-ab1d5b33 "GitHub Cpilotで使用可能なコンテンツの除外設定 : https://docs.github.com/enterprise-cloud@latest/copilot/managing-copilot/configuring-and-auditing-content-exclusion/excluding-content-from-github-copilot")

そこで有用なのが、**ローカルLLMを利用したコードアシスタント環境の構築**です。

![](https://cdn-ak.f.st-hatena.com/images/fotolife/t/teco_tshiiba/20241201/20241201182025.png)

LLMについて
-------

LLM（大規模言語モデル）とは、自然言語処理を中核とした機械学習モデルのことです。
OpenAIやAnthropicの提供するWebサービスもまた、独自のLLMを用いて構築されています。

それら外部Webサービスを使うのではなく、LLM自体を使って自前のローカル環境を構築すれば、
コンプライアンスやセキュリティリスクを抑えて生成AIを活用できるようになります。

それどころか、自前の環境であれば機密情報（を含むデータ）をAIに読ませる前提での運用も可能となり、さらなる業務効率の改善が期待できます。

---

…とはいえ、一口にローカル環境でLLMを利用すると言っても、
現実には個人レベルの実行環境でClaudeやChatGPTのような大規模汎用モデルを扱う事はまず不可能です。

そこで最近のローカルLLM界隈では、限定的な機能を持ったLLMを作ることで、省サイズと性能の両立を目指そうとする動きが強いです。

* 例 : WebページをMarkdown形式で要約する事に特化したLLM（0.5B, 1.5B）
  + [jina.ai](https://jina.ai/news/reader-lm-small-language-models-for-cleaning-and-converting-html-to-markdown/)

コーディング用途に特化したLLMも、今年に入ってから次々と実用レベルのモデルが公開され、
今では初期のGitHub Copilot(GPT-3.5 Turbo)を凌ぐレベルのコードアシスタントをローカルで構築可能になっています。

---

注意点として、生成AIの処理速度は現状ほとんどGPUに依存しており、
特にモデルデータをVRAMにどれだけ載せられるかに強く依存します。
よって実際に利用する際は、モデル全体がVRAMに収まるものを選択するのが望ましいです。

例として、パラメータ数が7B（70億個）のモデルを4bit量子化すると、VRAMが6～8GB程度あればモデル全体が収まります。
一方、32Bのモデルになると、同じ4bit量子化でも24GB程度のVRAMが必要になります。

主要なコーディング向けモデル
--------------

記事執筆現在、コーディング支援用途では以下のようなモデルが主流となっています。
いずれも2024年後半に新しく登場したモデルで、サイズに対する性能が向上し続けているため、
新しいモデルを積極的に試していくのがおすすめです。

なお、商用利用やファインチューニングについての制限を設けている場合もあるため、適宜ライセンスを確認して下さい。

### Qwen2.5-Coder

[huggingface.co](https://huggingface.co/collections/Qwen/qwen25-coder-66eaa22e6f99801bf65b0c2f)

* 公式サイト : <https://qwenlm.github.io/>
* 人気のコーディング向けLLMで、特に32Bモデルは複数のコーディングテストでChatGPT4oを超える性能が示されています
* 新しい推論モデルの開発も進められており、プレビュー版が公開されています
  + <https://huggingface.co/Qwen/QwQ-32B-Preview>

### DeepSeek-Coder-V2

[huggingface.co](https://huggingface.co/collections/deepseek-ai/deepseekcoder-v2-666bf4b274a5f556827ceeca)

* 公式サイト : <https://www.deepseek.com/>
* Qwen-Coderシリーズと並んで人気のあるコーディング向けLLMです
* 新たな推論モデルを調整しているとのことで、ChatGPT o1-previewを上回るという主張もあります
  + <https://x.com/deepseek_ai/status/1859200141355536422>

### StarCoder2

[huggingface.co](https://huggingface.co/bigcode)

* 公式サイト : <https://www.bigcode-project.org/>
* ServiceNow、Hugging Face、NVIDIAが共同開発したモデルです

### Pixtral Large

[huggingface.co](https://huggingface.co/mistralai/Pixtral-Large-Instruct-2411)

* 公式サイト : <https://mistral.ai/>
* コーディング特化モデルではありませんが、前モデルの頃からコーディング性能の高さが注目されていました

### Llama 3.3 (3.x)

[huggingface.co](https://huggingface.co/meta-llama)

* 公式サイト : <https://www.llama.com/>
* コーディング特化モデルではありませんが、有名な高性能LLMとしてよく比較対象になります

---

利用手段
----

ローカルLLMを利用できるアプリや拡張機能としては、主に以下のようなものがあります。

### 実行環境

#### LM Studio

[lmstudio.ai](https://lmstudio.ai/)

HuggingFaceでのモデル検索・ダウンロード・管理、チャットUI、外部APIサーバーなど、
基本的な機能を全てGUIで備えた統合アプリケーションです。

起動して数クリックで簡単にモデルをロードし、チャットウィンドウで会話できるため、初めての利用にオススメです。
様々なモデルの比較を行う際にも、プロンプトのテンプレートをGUIで簡単に設定できるなど便利です。

### Ollama

[ollama.com](https://ollama.com/)

LLM実行環境として最も標準的なソフトウェアです。
シンプルなコマンドライン操作で扱い易く、他のツールと連携するためのAPIサーバーを素早く起動できます。

機能的にシンプルで安定しているため、他のアプリケーションと連携するバックエンドサーバーとして常駐させる場合にオススメです。

アプリ・拡張機能
--------

### Continue

[www.continue.dev](https://www.continue.dev/)

主要なコードアシスタント機能を提供するIDE拡張機能で、
現在のところコーディング支援にローカルLLMを利用する場合の最も有力な選択肢です。

前述したローカルLLM実行環境と連携して使用し、

* 入力中のコードのサジェスト（オートコンプリート）
* ファイルや選択範囲の修正提案
* チャットウィンドウでの会話

などの機能を提供します。

機能や操作方法など[GitHub Copilot](https://github.com/features/copilot)と似た部分が多く、
GitHub Copilotユーザーは比較的移行しやすいと思います。

全ての機能をローカルLLMで実行可能ですが、
[Claude API](https://www.anthropic.com/api)や[OpenAI API](https://openai.com/index/openai-api/)を利用する事も可能なため、
必要に応じて接続先を切り替え、より優れた回答を生成することも出来ます。

### Aider

[aider.chat](https://aider.chat/)

AIが主体となってプロジェクトの開発を行い、人間はAIの生成物をレビューする立場という、
ローカルLLMを利用可能なものの中では新しいアプローチのペアプログラミングアプリです。

プロジェクトの作成から開発、テスト、レポジトリへのコミットまで全てAI側で行い、
人間側の操作が全てCUI上で完結するため、Vimmerからの支持も厚いようです。

なお、実行にはClaude APIまたはGPT-4oが推奨されており、現時点ではローカルLLMだと動作が不安定な場合があります。

VSCodeなどのIDE拡張機能も存在しますが、
それらは公式ではなく、Aiderユーザーが独自に公開しているものになります。

* <https://github.com/Aider-AI/aider/issues/68#issuecomment-1826916628>

また、Aiderは主要LLMのコーディング性能について評価したリーダーボードを公開しており、新しいモデルの比較にも有用です。

* <https://aider.chat/docs/leaderboards/>

### Cline

[github.com](https://github.com/cline/cline)

AI主体で開発することを目的としたVSCode拡張機能です。
プロジェクトの作成から実行テストや評価、修正提案など、
一連の作業をAI側が主体となって自動的に実行します。

特に、[Claude APIのコンピュータ操作機能](https://www.anthropic.com/news/3-5-models-and-computer-use)にいち早く対応し、
E2Eテストケースを自分で考え、直接的なカーソル操作・キーボード入力によってテストを実行する機能に注目が集まっています。

* <https://x.com/sdrzn/status/1850880547825823989>

元々Claude-devという名称で開発されており、Claude APIの利用が想定されていたため、
今のところローカルLLM環境ではフル機能を利用することが出来ません。
ローカルLLMへの対応拡充も進められており、今後が期待されます。

---

### 補足

ローカルLLMに対応したツールの多くは[Claude API](https://www.anthropic.com/api)や[OpenAI API](https://openai.com/index/openai-api/)を利用した方が安定動作する傾向にあり、
ローカルLLMの利用は安全性と動作安定性のトレードオフになっている側面もあります。

ただし、Claude APIなどの優れたAPIはどうしても高額になるため、
個人的な用途であってもコスト面からローカルLLM環境を検討する価値はありそうです。

また、ここで挙げたツールはいずれも１操作で接続先を切り替え可能なため、併用するのも１つの手です。
筆者はサジェストや修正提案など自動でコードを読み取る機能にはローカルLLMを、
チャットでの質問にはClaudeなどの強力なWebサービスを使うことが多いです。

後書き
---

今年はNPU搭載を前提としたCopilot+ PCをMicrosoftが提唱するなどあり、
小さな特化型LLMを利用しやすい環境が普及する兆しも見え始めています。

ほんの１～２年前までは、個人PCで扱えるオープンLLMはおよそ実用レベルでなかったことを考えるとめざましい変化といえ、
今後の動向にも注目していきたい所です。

### テコテックの採用活動について

テコテックでは新卒採用、中途採用共に積極的に募集をしています。  

採用サイトにて会社の雰囲気や福利厚生、募集内容をご確認いただけます。  

ご興味を持っていただけましたら是非ご覧ください。
[tecotec.co.jp](https://tecotec.co.jp/recruit/)

[\*1](#fn-ab1d5b33):GitHub Cpilotで使用可能なコンテンツの除外設定 : <https://docs.github.com/enterprise-cloud@latest/copilot/managing-copilot/configuring-and-auditing-content-exclusion/excluding-content-from-github-copilot>


