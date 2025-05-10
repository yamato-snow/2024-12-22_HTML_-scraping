[![](https://storage.googleapis.com/zenn-user-upload/topics/23eef6d9d7.png)AI](/topics/ai)[![](https://zenn.dev/images/topic.png)LLM](/topics/llm)[![](https://storage.googleapis.com/zenn-user-upload/topics/0929aebbc1.png)Devin](/topics/devin)[![](https://zenn.dev/images/topic.png)AIエージェント](/topics/ai%E3%82%A8%E3%83%BC%E3%82%B8%E3%82%A7%E3%83%B3%E3%83%88)[![](https://static.zenn.studio/images/drawing/tech-icon.svg)tech](/tech-or-idea)

Devinとは、ソフトウェア開発におけるタスクを自動化・効率化してくれるAIエージェントです。2024年12月に正式リリースされました。 私が所属しているUbieにも先日導入されました。様々な作業ができますが、あるリポジトリで不足しているテストを書いてもらったところ、その便利さに感動して椅子から転げ落ちました。

<https://devin.ai/>

本記事では、Devinの実際の使い方と、利用する上でのポイントを紹介します。

<https://x.com/tonkotsuboy_com/status/1871777460330938846>

1. テストの作成をSlackで依頼する
--------------------

Slackで「これこれのテストを書いてほしい」と依頼すると、Devinがテストコードを生成し、GitHubに新しいPRを作ってくれます。

依頼例は次のとおりです。

```
こんにちは、 @Devin 以下の仕事をして

- ubie-inc/リポジトリ名 repo にアクセスして
- （テスト対象のパス） のテストを書いて
- 次のテストの書き方を参考にして
  - foo/index.test.tsx
  - bar/index.test.tsx
- 実装追加した変更で PR を作って。
- PRのタイトルとサマリは日本語にして。
- ブランチ名は、testから始まるようにして
- コミットメッセージに Co-Authored-By: GitHubアカウント名 <メールアドレス> を含めて
- CIの「Lint and Test 」では、warningも出ないように修正して
- import '@testing-library/jest-native/extend-expect'; は含めないで
- import React from 'react'; は含めないで
- PRはdraftで作って

```

実際にSlackに依頼した例

![](https://res.cloudinary.com/zenn/image/fetch/s--aL1VBltt--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://storage.googleapis.com/zenn-user-upload/deployed-images/52fc72622ac1f839806cfa69.png%3Fsha%3D63f93b6709477e62874ea21dafbe5757d785920a)

### 依頼する際のポイント

プロジェクト内のお作法がわかるようなテスト事例をいくつか渡してあげるとスムーズです。事例が無い場合、ゼロから作ってもらうことも可能ですが、Devinとのやりとりに時間がかかってしまうので、最初の1, 2個目のテストは自前で作ってしまう方が早いです。

オススメはVS Codeの[GitHub Copilot拡張機能](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot)、[Cursor](https://www.cursor.com/)、[JetBrains AI Assistant](https://plugins.jetbrains.com/plugin/22282-jetbrains-ai-assistant)などを使い、プロジェクト全体を解読してもらいながらテストを書いてもらうことです。ちなみに筆者はDevinがない時代はこの手法でテストを構築しています。

2. 作業が開始するので更新を待つ
-----------------

Devinの作業が開始します。更新をしばらくまちます。

![](https://res.cloudinary.com/zenn/image/fetch/s--rcf5qNOY--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://storage.googleapis.com/zenn-user-upload/deployed-images/d3776d05e099983ec3fa76d3.png%3Fsha%3D76db4947932fc68e4e51e0a37585112ac94fe655)

3. CIの失敗は自動で修正してくれる
-------------------

個人的に激アツなのは、CIが失敗したときに成功するまで自動的に修正してくれるところです。これにより、わざわざ「CIが落ちているので修正して」といった追加の依頼をする必要はありません。

![](https://res.cloudinary.com/zenn/image/fetch/s--elDk9vCD--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://storage.googleapis.com/zenn-user-upload/deployed-images/b64ec7d78cab9a22bd0e17be.png%3Fsha%3Df410d12954ae5b0aec4da4de35de233f2b1206c6)  

*CIの失敗を検知し、自動で修正してくれる様子*

また、状況によっては失敗するCIをあえて無視したいケースもあるでしょう。そういった場合には、「◯◯のCIが落ちるのは無視して」とSlack上やDevin上でコメントすれば、該当のCIの失敗だけを無視してくれるようになります。

4. 追加の作業依頼を行う
-------------

作業が終わると実際にPRができますが、Devinの作業中やPRの作成後に追加の作業依頼をできます。依頼方法はいくつかあります。

### 方法① Slackのコメントから依頼する

最も手軽なのは、Slackのコメントから修正を依頼する方法です。例えば次の例では、不要な `import`文を削除してもらうよう依頼しています。Devinがコメントを拾って、作業を開始してくれます。

![](https://res.cloudinary.com/zenn/image/fetch/s--WVMK84B2--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://storage.googleapis.com/zenn-user-upload/deployed-images/b462ec0423d21dbe63e2d6eb.png%3Fsha%3D9ecd27583585fef3e94a806e8168fa83fcdd5619)

個人的にはこれがとても便利で、例えば私はリビングでテレビを見ながら、iPhoneのSlackでDevinに作業修正を依頼していました。

### 方法② GitHubのPR上から依頼する

GitHubのPR上から作業を依頼する方法です。PRの差分箇所に作業依頼をコメントすると、これもDevinが拾って作業をしてくれます。

![](https://res.cloudinary.com/zenn/image/fetch/s--8gU3z9tF--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://storage.googleapis.com/zenn-user-upload/deployed-images/7a2b4b0d35c2c758b92ba063.png%3Fsha%3Dace0591e84307bc740e83a9b8f7da416000e378a)

### 方法③ DevinのUI上から依頼する

DevinのUI上から作業を依頼する方法です。Devinが作業を開始するとセッションが発行され、 `https://app.devin.ai/sessions/セッションID` でアクセスできます。Editorタブでエディターを開けるので、編集をしたい箇所をDevin上で参照して作業依頼を追加できます。次の例では、テストのモック方法の修正を依頼しています。

![](https://res.cloudinary.com/zenn/image/fetch/s--9BqkeA-p--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://storage.googleapis.com/zenn-user-upload/deployed-images/f6f74c8c868851ffff28de2f.png%3Fsha%3D37bfbf07c08b3390b6744b49b4244150b905d6f8)

フィードバックの知見が溜まる
==============

大変便利なのが、各種作業依頼のフィードバックをDevinが学習して覚えてくれていることです。例えば、「モックの際は`jest.spyOn()`を優先的に使ってください」と指定していたとします。すると、その命令をDevinが「Knowledge」として保存し、次回もその内容を使うかどうかを選択できます。そのまま採用・不採用もできますし、よりよい指示に編集して保存することもできます。

![](https://res.cloudinary.com/zenn/image/fetch/s--kFSz2y60--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://storage.googleapis.com/zenn-user-upload/deployed-images/bf1b33087aeb9cf1cd66ad9d.png%3Fsha%3D6a076c7dc7ec232f0d0e59d727d716ec63ad7081)  

*指摘した指示をKnowledgeとして保存するかを提案している様子*

保存したKnowledgeはリポジトリごとに保存され、次回の作業時に使ってくれます。

![](https://res.cloudinary.com/zenn/image/fetch/s--sFKPuNB1--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://storage.googleapis.com/zenn-user-upload/deployed-images/49c1c263e00df8586327d445.png%3Fsha%3D6dce233c0e64a99b183e8f4fcb0db9c1af937c44)

Knowledgeは自由に追加・修正・削除が可能なので、毎回長ったらしいプロンプトを書く手間が省けますし、リポジトリごとのコードの方針も統一ができます。

<https://docs.devin.ai/onboard-devin/knowledge>

もっと改善されると嬉しいところ
===============

テストの内容が正しいかどうか、ドメイン知識や最終チェックにはエンジニアがPRをチェックする必要があります。当初、非エンジニアに不足しているテストを追加・量産してもらい、リリースまで実施してもらおうとしていたのですが、成果物の内容的にはまだ厳しいと言わざるを得ない場面がありました。とは言え、うまく行ってないところを修正すればいいだけなので、ゼロからテストを書くよりは格段にラクです。

作業速度についても、もっと改善されると嬉しいなとは感じました。文中でも書いたように、ゼロから複雑な作業を依頼するよりは、ある程度の事例や指示を明確に出した方が、最終的な仕上がりは早くなる印象です。

テストはほんの一部。やってくれることは無限大
======================

本記事で紹介したのは、筆者が一番やってほしいと思っていたテストの自動生成ですが、やってくれることは無限にあります。

例えば実例として、我々のチームでは次のようなことをやってもらいました。

* いつかやらなきゃと思っていたリファクタリング
* エラーハンドリングを追加する
* ローカルストレージにデータを保存していた設定をDBに移行する
* package.jsonから不要なnode\_modulesを削除する
* 特定条件で画面が崩れるバグの修正
* ドキュメントの作成
* いつか作らなきゃと思っていたCI/CDを作ってもらう
* 他多数

値段について
======

一月あたり従量課金で$500〜です。高いか安いかはチームの事情によるとは思いますが、24時間働いてくれるフルスタックエンジニアが月$500〜というのは、個人的にはリーズナブルだと思います。 たとえば単価5,000円のエンジニアに20日稼働してもらったら80万円、単価10,000円なら160万円くらいですからね。ぜひチームのメンバーと相談してみましょう。

<https://devin.ai/pricing>

リファラルでチケットをもらえます
----------------

次のリンクからDevinを使うと、100ACU（200ドル分）のチケットをもらえるのでぜひご活用ください！

<https://app.devin.ai/invite/KPRRa4OgmXVHYgp1>

面倒なテストはAIに任せよう
==============

GitHub上のコードを解析して、勝手にテストコードを書いて、CIがパスするまで作業して、追加の作業依頼もしてくれるAIというのは、ずっと求めていた夢でした 。

なお、ローカルでDevinのようなAIエージェントを試す場合は、ClineやCursor Yoloがオススメです。弊社 @syucream が書いた記事がわかりやすいです。

<https://zenn.dev/ubie_dev/articles/624c9034cc9b43>

また、DevinやCursorの使い分けについては、 @empitsu88 が書いた記事に詳しいです。

<https://zenn.dev/ubie_dev/articles/e9682c9c6487c8>

私の所属しているUbieは、Devinのような新しい生成AIを実務に取り入れています。社内LLM「dev爺」では各種最新LLMモデルが使い放題になっているため、金銭的な負担もなく好きなだけAIを試せます。

<https://x.com/tonkotsuboy_com/status/1872192017314594864>

興味のある人は、ぜひUbieで一緒に楽しい開発をしていきましょう。

<https://recruit.ubie.life/>

[GitHubで編集を提案](https://github.com/tonkotsuboy/zenn-articles/blob/main/articles/devin-for-test.md)[![鹿野 壮](https://lh3.googleusercontent.com/a-/AOh14GhpEC1mKcV6l_MeOdz7Slz95ItxYFhb0v-3Nw3cWw=s250-c)](/tonkotsuboy_com)[鹿野 壮](/tonkotsuboy_com)

Ubie / フロントエンド&バックエンド&アプリ開発&AIエージェント / 九州大学芸工音響設計学科卒 / JavaScriptコードレシピ集の著者 / CSSNite ベストセッション / TechFeed公認エキスパート / お仕事依頼はDMへ

[![Ubie テックブログ](https://storage.googleapis.com/zenn-user-upload/avatar/ee9c31da83.jpeg)](/p/ubie_dev)[Ubie テックブログ](/p/ubie_dev)[Publication](/faq#what-is-publication)

Ubie株式会社のテックブログです。
採用情報：[recruit.ubie.life/engineer](https://recruit.ubie.life/engineer)

バッジを贈って著者を応援しよう

バッジを受け取った著者にはZennから現金やAmazonギフトカードが還元されます。

バッジを贈る