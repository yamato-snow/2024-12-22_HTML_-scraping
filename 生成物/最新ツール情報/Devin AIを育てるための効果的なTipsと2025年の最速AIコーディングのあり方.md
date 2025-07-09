[![](https://storage.googleapis.com/zenn-user-upload/topics/23eef6d9d7.png)AI](/topics/ai)[![](https://storage.googleapis.com/zenn-user-upload/topics/cfd34a2747.png)Tips](/topics/tips)[![](https://zenn.dev/images/topic.png)LLM](/topics/llm)[![](https://zenn.dev/images/topic.png)生成 AI](/topics/%E7%94%9F%E6%88%90ai)[![](https://storage.googleapis.com/zenn-user-upload/topics/0929aebbc1.png)Devin](/topics/devin)[![](https://static.zenn.studio/images/drawing/tech-icon.svg)tech](/tech-or-idea)

最近、Devin AIを契約したので、はじめて使う人や決済するか悩んでる人向けのTipsを書こうと思います。

![](https://storage.googleapis.com/zenn-user-upload/fb1675dd2e46-20241231.png)

契約する前は海外の悪評が目立っていたのでどうかな？と思っていたんですが、Ubieの鹿野さんの記事に触発されて、まずは試してみないとわからないかと思い決済しました。（円安で8万1千円ほどのでしたが、まぁマネージャーレイヤーだとありかなと思います。）

<https://zenn.dev/ubie_dev/articles/devin-for-test>

いまは使い方に慣れてきて、毎日お話しています。継続してもいいかな？とも思っており、以下の点に気をつけて使っています。ほぼリモートエンジニアと仕事するときと一緒ですね。シェアしていきます。

1. 段階的なオンボーディング
   * 小さなタスクから始める
   * 成功体験を積み重ねる
2. 明確な振る舞いの指示
   * プロジェクト固有の規約を説明
   * 期待する成果物の形式を具体的に示す

---

\*ちなみに、DevinのOSS版と言われるOpen Hands（旧Open Devin）も使ってみましたが、以下の点でDevinとの差異を感じました。コーディング作業を常に一人で完了する場合は悪くないかもしれません。

* Open HandsもGithubにPRまで上げてくれるが、ローカルのDockerで動かす必要や、Slack連携などがないため重い。
* ただし、APIコストのみで使えるため、価格的には圧倒的なコスパ
* また、文脈の横断性はDevinのほうが上だが、おそらくコーディング能力はそこまで遜色はない。どちらもCursorクラスだと思って問題ない。

<https://github.com/All-Hands-AI/OpenHands>

---

Devin.ai育成のTips
===============

1. 段階的なオンボーディング 🚀
-----------------

最初にDevinを触ってみて、あんまりうまくいかなかったんですよね。正直残念な印象でした。具体的には、TypeScriptのリファクタリングの中でも複雑なタスク（Interfaceの集約のタスク、依存関係が3ファイルを横断している。）を渡しちゃって...結果的に3,4回も同じようなタスクを違うやり方で指示することになっちゃいました。

![](https://storage.googleapis.com/zenn-user-upload/49593ab9ccaa-20241231.png)

1回目は、Cursorでリファクタの指示書を作りました。Few Shotで具体例を示しつつ、使うファイルもすべて指示したんですが、うまくいかず。  

2回目は、実際に違うブランチで同様の作業の例をコミットしたものを見せて、実行させたがうまくいかず。  

3回目以降は以下のようにPlaybookなども活用したのですが、これもうまくいかず。

![](https://storage.googleapis.com/zenn-user-upload/87ed1633f20a-20241231.png)

\*Playbookとは、Devinにシステムプロンプトの塊を渡せる機能で、成功したプロンプトで実行を再生産できるものです。  

<https://docs.devin.ai/working-with-teams/using-playbooks>

60ACUくらい使って、何のせいかも得られませんでした、みたいな感じだったので結構ショックでした。  

ただ、さすがにここでタスクの対象が悪いのかな？と思い始めて、違うタスクにするようにしました。ここでの学びは以下のとおりです。

\*ACUとはDevinが働ける時間をあらわすクレジットのようなものです。250ACUもらえます。  

<https://devin.ai/pricing>

### 小さなタスクから始める

これは完全に私の失敗だったんですけど、この経験から学んだことがあります：

* いきなり複雑なリファクタリング（ファイルを横断する、Lintのエラーなどが発生しやすい）は避ける
* 1回のプロンプトですべてを説明せずにステップバイステップにタスク分割する
* まずは50行程度の小規模な変更から始めるのがベスト
* 環境のセットアップも含めて、スモールステップで進める

![](https://storage.googleapis.com/zenn-user-upload/69d73c78e495-20241228.png)

実際、以下の西尾さんの事例を見ても、最初は小さなタスクから始めて、徐々にスケールアップしていったみたいですね。

[https://scrapbox.io/nishio/Devin.aiを試す](https://scrapbox.io/nishio/Devin.ai%E3%82%92%E8%A9%A6%E3%81%99)

### 成功体験を積み重ねる

ここがポイントなんですけど、小さな成功を重ねることで、AIエージェントの特性もよく理解できるようになります：

* 最初は簡単な修正タスクから
* うまくいったパターンを記録
* 成功体験を基に、少しずつ複雑なタスクにチャレンジ

私の場合、最初のコード修正で躓いた後、1ファイルの作成→チャットで作成の追加指示→ループのような指示に絞ったら、かなりスムーズに進められるようになりました。これ、人間のチームメンバーのオンボーディングと似てるなって気付きましたね。

人間でも難しいタスクをいきなり投げられても困っちゃいますよね。AIエージェントも同じで、適切なステップアップが大事なんです。最初は地道に、でも確実に...という感じで進めていくのがコツかなと思います。

DevinはKnowledgeという機能があり、細かい指示のたびにレポジトリでの振る舞いを学習していきます。なので、小さい単位で仕事をこなしていくことで、レポジトリへの解像度が上がるということにもつながるのです。

<https://docs.devin.ai/onboard-devin/knowledge>

2. 明確な振る舞いの指示 🎯
---------------

そういう意味では、レポジトリの文脈を理解して振る舞いを学習していくためのプロンプトを重ねていくことが大事になってくるのかなと思います。

![](https://storage.googleapis.com/zenn-user-upload/1562fd00941f-20241228.png)

![](https://storage.googleapis.com/zenn-user-upload/0bd7e2cf1fde-20241228.png)

### プロジェクト固有の規約を説明

これが結構重要なポイントで：

* AIエンジニアだからって何でも対応できるわけじゃないんですよね
* レポジトリごとの振る舞いルールは明確に伝える必要がある
* 依存関係とかも丁寧に説明していく

Devinの公式の事例を見ても、ETLの移行プロジェクトで成功したのは、プロジェクトのルールをしっかり定義していたからだと思うんです。

### 期待する成果物の形式を具体的に示す

ここで私が学んだことなんですけど、最初から曖昧なタスクを一気に渡さないほうがいいということです。

* 既存のファイルへの追加や修正方法を具体的に示す
* コードの書き方やドキュメントの形式も明確に
* 人間のエンジニアに指示するのと同じように丁寧に

Cursorに慣れていると、Codebaseの理解とトライアンドエラーが高速に回せるので、こうなってしまったのかなと思いますが、Devinはまた違います。人間のチームメンバーと同じで、期待値をちゃんと伝えることが大事だなって気づきました。

特に面白かったのは、一度理解した規約は覚えていってくれるところ。でも、文脈の対応力は人間ほど高くないので、その辺りは補助が必要ですね。結局のところ、人間のエンジニアに対して丁寧に指示を出すのと同じような配慮が必要なんだなって実感しています。

![](https://storage.googleapis.com/zenn-user-upload/3f17cc40c62b-20241231.png)

Devinを育てるということ
==============

Devinとのコミュニケーション
----------------

最初は「あれ？思ったようにいかないな」って感じだったんですけど、フィードバックを重ねていくと、どんどん良い感じになってくるんですよね。人間のチームメンバーと同じで、良いところは褒めて、改善点は具体的に伝える...そんな感じのコミュニケーションが大事だなって実感しています。

結局のところ、AIエージェントも一人のチームメンバーとして考えて、丁寧にフィードバックを重ねていく。そうすることで、プロジェクト全体の効率も上がっていくんじゃないかなって思います。

今後のDevinへの期待としては、最初はつまずいたTypeScriptのリファクタリングでも、フィードバックを重ねていって、だんだん「あ、こういうことね」って感じで理解してくれることを期待しています。

これはLLMのモデルの精度向上やDevinのエージェントの設計の改善はもちろん、Knowledgeの蓄積による効果が今後高まっていくという予測があります。また、タスクの成功が増えていけば、Playbookに成功した指示を貯めることもできるので、これも資産になりそうです。

個人的にもAIエージェントのメモリは実はMoatになるんじゃないかとも思っており、関心を寄せています。

Devinを扱う際の変数
------------

Devinを扱う際には、開発環境のきれいさ、指示の明確さ、Devinの能力の3つのバランスが重要だと思いました。そもそもコードが汚いなら、AIでも読み解くのが難しいし、いかに明瞭な指示でもDevinの文脈理解の限界であれば、それは難しい。環境が汚い場合、Devinはうまく働けないという、しっぺ返しを食らう可能性もあります。

![](https://storage.googleapis.com/zenn-user-upload/a6e39367a4db-20241231.png)

能力について言うと、タスクの向き不向きは明確にあり、依存関係が多そうなものは無駄になるのでやめておいたほうがいいです。Devinはジュニアくらいのコーディング能力はあっても、文脈理解はやはりスタックしてしまうことがあるため、そういうタスクは小さい単位にするか、渡すタスクのコード自体をもっとシンプルにリファクタしてから渡すべきでしょう。

どの開発PJでもシンプルなタスクがあるはずで、そこをでゔぃんに、そうじゃないところは人間＋Cursorなどで処理していくのが2025年の最速コーディングかもしれません！

![](https://storage.googleapis.com/zenn-user-upload/8f4c0fea8c57-20241231.png)

---

About me
========

現在、市場調査やデスクリサーチの生成AIエージェントを作っています 仲間探し中 / Founder of AI Desk Research Agent @deskrex , <https://deskrex.ai>

ぜひお気軽にチャットしましょう！Devinもいます。  

<https://x.com/ItaruTomita9779/status/1856471446614356395>

生成AIデスクリサーチサービス Deskrex | サービスページ
---------------------------------

<https://lp.deskrex.ai/>

生成AIデスクリサーチエージェント Deskrex App | アプリケーションサイト
-------------------------------------------

<https://app.deskrex.ai/>

DeskrexAIリサーチ | メディア
--------------------

<https://media.deskrex.ai/>

株式会社Deskrex | 会社概要
------------------

<https://www.deskrex.ai/>

Deskrex | Xページ
--------------

<https://x.com/deskrex>

* 会社概要：<https://www.deskrex.ai/>
* Deskrex App：<https://app.deskrex.ai/>
* サービスページ：<https://lp.deskrex.ai/>
* メディア：<https://media.deskrex.ai/>
* X：<https://x.com/deskrex>
[![Itaru Tomita](https://storage.googleapis.com/zenn-user-upload/avatar/820b04468d.jpeg)](/tomtar9779)[Itaru Tomita](/tomtar9779)

市場調査やデスクリサーチの生成AIエージェントを作っています 仲間探し中 / Founder of AI Desk Research Agent @deskrex , [deskrex.ai](https://deskrex.ai)

[![Deskrex テックブログ](https://storage.googleapis.com/zenn-user-upload/avatar/a219487bc3.jpeg)](/p/deskrex)[Deskrex テックブログ](/p/deskrex)[Publication](/faq#what-is-publication)

株式会社Deskrexのテックブログです。生成AIやLLMに関するリサーチを共有します。

バッジを贈って著者を応援しよう

バッジを受け取った著者にはZennから現金やAmazonギフトカードが還元されます。

バッジを贈る