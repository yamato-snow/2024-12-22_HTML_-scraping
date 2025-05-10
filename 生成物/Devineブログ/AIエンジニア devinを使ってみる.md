

はじめに
----

Devinは､全自動のAIエンジニアのようです｡昨年の12月に一般版が公開されたとのことです｡

[**Devin AIにテストを丸ごと書かせてCIがパスするまで作業してもらう方法**

*zenn.dev*](https://zenn.dev/ubie_dev/articles/devin-for-test)

最近､自分のプログラミングが､ ChatGPTに聞く→コードを貼る→結果をChatGPTに戻す→ … という感じの作業になってきたので､一連の作業をAIにやってもらえるかも､という期待を込めて､課金してみることにしました｡

1ヶ月あたり$500とお高いですが､時間はそれよりも重要だと判断したので､お試しでの利用です｡

登録
--

googleアカウントなどでサインインできます｡  
チャット風の画面に回答していくと､課金を迫られますので､課金します｡  
500ドルで､250x15 minくらいは働いてくれるようです｡

![](https://assets.st-note.com/img/1736838945-gi3OfwYtCBHvMd9uExbZNn1R.png?width=1200)



課金後､githubやらslackに接続するように言われるので､設定していきます｡

![](https://assets.st-note.com/img/1736839037-fqhYWJ9LX8Kn7bAtD0N3M1gd.png?width=1200)



githubのレポジトリ登録まで済ませたら､ブラウザ上にvs codeの画面などが出てきました｡

![](https://assets.st-note.com/img/1736839578-2ygXLAkxubziQ4KSm9awpHn1.png?width=1200)



  


動かしてみる
------

上記画面では､pythonの環境設定やら､なんやら(skip1-4)を聞かれたのですが､とりあえず空欄&何もせず､進めてみました｡

### コードを作る

slackから指示をして､みたいな画面が出てきたので､devinに指示をしてみました｡  
@Devin でメンションしながら作業するようです｡

とりあえず､hello world的なコードを作らせてみました｡

![](https://assets.st-note.com/img/1736840310-Qzvpu5rVD3AgK64RUZ0s7FTO.png?width=1200)



### pushする

[@Devin](https://slack-e749560.slack.com/team/U088J354E2X)  
pushして

と頼むと､pushもしてくれました｡

### 動作テストする

ブラウザ上でもchatできました(slackにも反映されるようです)

![](https://assets.st-note.com/img/1736840744-MQl5ZcreyfVHuhOkIKno4FsA.png?width=1200)



結果

![](https://assets.st-note.com/img/1736840795-w50ToO6k3y8c4dXpMPiZW1uB.png)



ブラウザ上の画面の右側で､テーミナルログが出力されていました｡

![](https://assets.st-note.com/img/1736840979-Drc01jhYPWMVG5o2JLZg7esC.png?width=1200)



失敗: ローカルマシンにリモート接続して作業させる
-------------------------

devinは基本的に､この会社が用意したコンテナ上で作業するサービスのようです｡  
個人的には､手持ちのGPUサーバー上で機械学習系の作業させたいので､ローカルマシンにリモート接続してみることにします｡

やり方をきちんと調べてはいないんですが､devinのsecret keyにsshのconfig情報とpubkeyを設定して､接続することはできそうです｡  
(こういうやり方でよいのか､､という)

まずはsecret keyを設定します｡  


![](https://assets.st-note.com/img/1736848309-0g83j6DxIh2z9JYMto4kOCpb.png?width=1200)



![](https://assets.st-note.com/img/1736846753-8r7AT4MU0a3PiZxsDRE1dQbv.png?width=1200)



この状態で､

```
ssh-config secret keyには､sshのconfigがあります
id_ed25519.pubには､id_ed25519.pubのキーが格納されています
ssh a100でアクセスして､作業してください｡

アクセスしたら/data/devin
というフォルダを作ってください
```

と投げてみました｡

結果は､

```
SSHでの接続を試みましたが、パスワード認証を要求されています。現在以下の設定が完了しています：

    ~/.ssh/config にssh_configの内容を設定
    ~/.ssh/id_ed25519.pub に公開鍵を設定

接続方法について以下のいずれかをご確認させていただけますでしょうか：

    パスワード認証を使用する場合、パスワードをご提供いただけますでしょうか？
    公開鍵認証を使用する場合、秘密鍵（id_ed25519）が必要となります。

ご指示をお願いいたします。
```

でした｡   
sshのconfigを見てみると､IdentityFileの記入を忘れていたようです｡

結論としては､  
このやり方でも､頑張ればリモートマシンにssh接続できるけれども､  
明らかに推奨されていない雰囲気がしました｡

  


既存プロジェクトのコードを改造させる
------------------

devin上で動きそうなプロジェクトのコードをuploadし､リファクタリングなどをさせてみます｡

以下の感じの雑な指示を出しました｡

```
・新しいコードをpushしたので､pullして
・必要なpipライブラリなどのrequirements.txtを作って
・1212prediction_test.py をリファクタリングしたうえで､評価件数を適当に減らしてコードを実行して
```

すると､これから作業しますよ､みたいな感じの返事が返ってました｡  
いい感じに作業してくれてそうです｡

![](https://assets.st-note.com/img/1736849117-hAktSXoiDNBsc7V24rRyWIKv.png?width=1200)



いい感じにやっといて､みたいな雑な指示を投げておきました｡

> user  
> ・新しいコードをpushしたので､pullして   
> ・必要なpipライブラリなどのrequirements.txtを作って  
> ・1212prediction\_test.py をリファクタリングしたうえで､評価件数を適当に減らしてコードを実行して  
>   
> Devin will sleep after using 10 ACUs (resets with each new instruction). Manage session usage limit.  
>   
>   
> Devin  
>   
> 了解しました。コードをpullして、requirements.txtを作成し、1212prediction\_test.pyのリファクタリングと実行を行います。  
>   
>   
> Running startup commands...  
>   
> Startup commands completed (2.5s)  
>   
> Devin  
> I'll first work on a plan. If you want me to confirm the plan with you before proceeding, please click the 'wait for confirmation' button below.  
> Investigated the codebase by reviewing the `1212prediction\_test.py` file.  
> Investigated the codebase by reviewing the `1212prediction\_test.py` file and identified the necessary libraries for requirements.txt creation.  
>   
> (中略)  
>   
> user  
> リファクタリングが終わったら､  
> ・readme.mdを生成   
> ・いまはルールベースの処理なので､いい感じの機械学習アルゴリズムを作って､精度を99%まで上げて｡   
> ・基本的にconfirmしますので､いい感じに作業しといてください  
>   
> Devin  
> 了解しました。リファクタリング完了後、README.md作成と機械学習アルゴリズムの実装を順次進めていきます。



**結果: リファクタリングはうまくいきました｡**一方､機械学習の結果は微妙でした｡自分がこれまでの経験で得てきたノウハウ的な要素を教えていなかったので､愚直にやってイマイチな結果に陥る､という感じでした｡

所感・まとめ
------

触ってわかった所感を記します｡

以下は私が感じたことをまとめたものです。

* **作業速度：人間よりも遅い?です。**リファクタリングなどは素早く行ってくれます。ただし、パラメータの最適化などは少し時間がかかる印象です。
* **タスクの投げ方：寝る前にタスクを投げて、朝に確認するという使い方はまだ難しいです**。モデルのコンテキスト長などの問題があります。感覚的には、1時間くらいで終わる細かいタスクを投げるのが良さそうです。
* **作業履歴とセッショ**ン：デフォルト設定では、3時間ほど動かすと、作業履歴が膨れてくるため、新しいセッションで開始しなおしたほうが良いです。
* **進捗確認方法：slackでやりとりしながら、下っ端の作業者に作業を進めてもらう感じ**です。指示してもそこそこのクオリティで作業してくれますが、定期的に進捗を確認し、フィードバックを入れるほうが良さそうです。スマホ画面でチャットしながら指示を出す使い方には向いているかもしれません。
* **パソコンを使わずにプログラミング**：スマホからdevinに作業を指示することで、パソコンを使わずにプログラミングができるようになってしまいます。隙間時間や就寝時間帯に作業を指示することができますが、一日中作業ができるとQOLが下がるかもしれないという危機感があります。

  


