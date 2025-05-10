[![](https://qiita-user-profile-images.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F118627%2Fprofile-images%2F1680349233?ixlib=rb-4.0.0&auto=compress%2Cformat&lossless=0&w=48&s=5fec3b5757af9249c81bda031ba9f701)@Satoshi\_Numasawa(Numasawa Satoshi)](/Satoshi_Numasawa)in[![](https://qiita-organization-images.imgix.net/https%3A%2F%2Fs3-ap-northeast-1.amazonaws.com%2Fqiita-organization-image%2Fe3765eb723da6eace0557eb2085916953dc56a07%2Foriginal.jpg%3F1527231530?ixlib=rb-4.0.0&auto=compress%2Cformat&s=70b238ebe5a853384e9247592faad0eb)株式会社Ruby開発](/organizations/ruby-dev)

Devin AI の概要を簡単に調べてみる
=====================

* [Devin](/tags/devin)

Last updated at 2025-04-02Posted at 2025-02-10

Devin とは
========

Cognition 社の自律協調型のAIソフトウェアエンジニア, チームメイト

料金体系
====




Teamプラン
-------

**$500 / 月**

* Devin の基本機能へのアクセス
* コードの自動生成とデバッグ
* ソフトウェアの自動デプロイ
* 継続的な学習と最適化
* 自然言語およびチャットインターフェースでの共同作業
* 月間250 ACU（Agent Compute Units）の使用量
  + エージェントの稼働時間は, **62.5 時間 / 月**まで可能

Enterpriseプラン
-------------

カスタム価格  

Teamプランのすべての機能に加えて, 以下の追加機能が提供される

* Devin Enterprise およびカスタム Devin へのアクセス
* マルチ Devin 機能
* 仮想プライベートクラウド（VPC）内でのデプロイ
* 専任のアカウントチーム
* カスタム契約条件

ACU（Agent Compute Unit）とは
-------------------------

* Devin の作業単位.
* タスク実行に使用する計算リソースを正規化した指標
  + 仮想マシン時間
  + モデル推論
  + ネットワーク帯域幅
* 250ACU / 月 が付与される
  + 1 ACU = 15分の作業時間に相当
  + 時給1,200円ほど
* 追加購入も可能
  + 2$ / 1ACU
  + 設定した使用上限まで, 追加ACUを従量課金で自動購入する
* Devin が稼働しない間, ACU は消費されない
  + Devinは～0.1ACU活動しないと自動的にスリープする
* 月に何時間利用できるのか
  + 250 \* 15 = 3,750
  + 3750 / 60.0 = 62.5時間 / 月




機能
==

* 自律性, 自然言語での共同作業
  + 自然言語で指示を与え, 自動で設計, 実装する
    - Slack, VSCode, GitHub, Devin tool などを通じて対話・指示が可能
  + コードを生成
  + エラーを自動で修正
  + リアルタイムの進捗報告
  + 自動デプロイ, PR作成
* Devin workspace
  + 独自の shell, browser, editor, planner を搭載
    - Devin の状態を引き継ぎ, コマンド実行, コード編集, ブラウザ操作などが可能
* Devin api
  + API を通じてプログラムから Devin セッションを作成し, 結果を取得
* Machine snapshots
  + Devin の状態を保存し, その状態から開始できる
* Knowledge
  + 学習機能
  + 与えた指示を記憶し成長する
* 複数実行
  + 複数のタスクを並行して実行可能
  + ACUはその分消費する
* Custom Devins（Enterprise 限定）
  + 特定のユースケースに特化した Devin
  + 高速で信頼性が高く, 反復的なタスクに推奨

Devin の長所は？
===========




Devin は, ジュニアレベルの複雑さにおいて効果を発揮するとの事

Knowledge, 学習機能
===============




Devin へドキュメント, ヒント, カスタム内部ライブラリ, その他, 必要とする資料を共有することができる

* 知識とそのトリガーを記述することで, Devin は適切な状況において知識を用いる
* 指示のたびにリポジトリでの振る舞いを学習する

投入したデータはモデルの学習に用いられるのか
======================




* 学習に用いられる
  + team プランでは手動で学習を無効化する事ができる
  + Enterprise プランではデフォルトで無効
* ここでの学習とは恐らく knowledge 機能ではなく, LLM のトレーニングデータとして利用されることを指すと思われる

事例と参考情報
=======

初期導入時の流れ
--------




* 導入方法と導入時のチュートリアル的な情報
* Devin knowledge へ与えるオンボーディング情報などを確認できる
* 返答を素早く行うために, 0.5 時間の待機時間があり, その間も課金が発生するとのこと
  + SLEEP とうちこみ手動停止が可能

クイックスタートガイド
-----------




Tips
----




* Devin を育てる
  + いきなり複雑な作業はできない
  + 小さなステップやタスクから始める必要がある
  + 人間同様にオンボーディングが必要
  + knowledge 機能により指示を記憶し, リポジトリへの理解度が向上していく
  + 期待する成果を具体的に指示することが重要
* Devin はジュニアレベル
  + シンプルで依存関係が少ないものは Devin で高速化
  + その他は, 人間が他の AI Editor と協調して作成するのが良い
* ドキュメントを読まずに始めると ACU を無駄にする

とんこつさんの利用風景
-----------




* 実際に作業を依頼している画像など参照できる
* 作業依頼のフィードバックや指示を Devin が [学習して覚えてくれる](https://zenn.dev/ubie_dev/articles/devin-for-test#%E3%83%95%E3%82%A3%E3%83%BC%E3%83%89%E3%83%90%E3%83%83%E3%82%AF%E3%81%AE%E7%9F%A5%E8%A6%8B%E3%81%8C%E6%BA%9C%E3%81%BE%E3%82%8B)
* とんこつさんの結論
  + > 面倒なテストはAIに任せよう

テストフレームワークの入れ替えで失敗
------------------




* 大雑把な指示は苦手
  + 具体的な task や指示が望ましい
* 大きな task は苦手
  + テストフレームワークを入れ替えるなどの単位では失敗する
* document 起こしはそこそこ良い
  + ドメイン知識や抽象度が高い概念は補足する必要がある
  + 解りやすいコードは的確

使用体験, 優れた点や注意点
--------------




参考動画
====

約 10 分の動画で Devin の動作を簡単に確認できる  

<https://www.youtube.com/watch?v=uHsN4fFsMes>

約 1 時間の動画で省略なしの動作を確認できる  

<https://www.youtube.com/watch?v=2fCQUmIfd7o>

所管
==

各記事や Twitter などの反応を見る限り, 有用で実用レベルに達している  

ただし, 人間側も使い方を学ぶ必要がある  

使い所はジュニアレベル, シンプルなタスク

個人で $500 は高額だが, 企業で試験導入する価値はあると考えられる

余談
==

Devin を通して[ラーメン](https://x.com/teramotodaiki/status/1888815700762079356)や[牛丼](https://x.com/teramotodaiki/status/1887391066741240039)を注文している方がおられる

[6](/Satoshi_Numasawa/items/7eed1cdf6c42783ead90/likers)

Go to list of users who liked

1[comment0](#comments)

Go to list of comments

Register as a new user and use Qiita more conveniently

1. You get articles that match your needs
2. You can efficiently read back useful information
3. You can use dark theme

[What you can do with signing up](https://help.qiita.com/ja/articles/qiita-login-user)[Sign up](/signup?callback_action=login_or_signup&redirect_to=%2FSatoshi_Numasawa%2Fitems%2F7eed1cdf6c42783ead90&realm=qiita)[Login](/login?callback_action=login_or_signup&redirect_to=%2FSatoshi_Numasawa%2Fitems%2F7eed1cdf6c42783ead90&realm=qiita)