![注目のAIエンジニア「Devin」を入れてみた！購入から初期設定まで](https://devio2024-media.developers.io/image/upload/v1737682597/user-gen-eyecatch/aibqscmnntfojegr3a4u.png)

注目のAIエンジニア「Devin」を入れてみた！購入から初期設定まで
==================================

[#Devin](/tags/devin/)[![佐藤智樹](https://devio2023-media.developers.io/wp-content/uploads/devio_thumbnail/2024-06/sato-tomoki.png)

佐藤智樹](/author/sato-tomoki/)[![facebook logo](/img/sns/facebook.svg)](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fdev.classmethod.jp%2Farticles%2Fdevin-init%2F&t=%E6%B3%A8%E7%9B%AE%E3%81%AEAI%E3%82%A8%E3%83%B3%E3%82%B8%E3%83%8B%E3%82%A2%E3%80%8CDevin%E3%80%8D%E3%82%92%E5%85%A5%E3%82%8C%E3%81%A6%E3%81%BF%E3%81%9F%EF%BC%81%E8%B3%BC%E5%85%A5%E3%81%8B%E3%82%89%E5%88%9D%E6%9C%9F%E8%A8%AD%E5%AE%9A%E3%81%BE%E3%81%A7%20%7C%20DevelopersIOhttps%3A%2F%2Fdev.classmethod.jp%2Farticles%2Fdevin-init%2F&t=%E6%B3%A8%E7%9B%AE%E3%81%AEAI%E3%82%A8%E3%83%B3%E3%82%B8%E3%83%8B%E3%82%A2%E3%80%8CDevin%E3%80%8D%E3%82%92%E5%85%A5%E3%82%8C%E3%81%A6%E3%81%BF%E3%81%9F%EF%BC%81%E8%B3%BC%E5%85%A5%E3%81%8B%E3%82%89%E5%88%9D%E6%9C%9F%E8%A8%AD%E5%AE%9A%E3%81%BE%E3%81%A7%20%7C%20DevelopersIO)[![hatena logo](/img/sns/hatena.svg)](https://b.hatena.ne.jp/add?mode=confirm&url=https%3A%2F%2Fdev.classmethod.jp%2Farticles%2Fdevin-init%2F&title=%E6%B3%A8%E7%9B%AE%E3%81%AEAI%E3%82%A8%E3%83%B3%E3%82%B8%E3%83%8B%E3%82%A2%E3%80%8CDevin%E3%80%8D%E3%82%92%E5%85%A5%E3%82%8C%E3%81%A6%E3%81%BF%E3%81%9F%EF%BC%81%E8%B3%BC%E5%85%A5%E3%81%8B%E3%82%89%E5%88%9D%E6%9C%9F%E8%A8%AD%E5%AE%9A%E3%81%BE%E3%81%A7%20%7C%20DevelopersIOhttps%3A%2F%2Fdev.classmethod.jp%2Farticles%2Fdevin-init%2F&t=%E6%B3%A8%E7%9B%AE%E3%81%AEAI%E3%82%A8%E3%83%B3%E3%82%B8%E3%83%8B%E3%82%A2%E3%80%8CDevin%E3%80%8D%E3%82%92%E5%85%A5%E3%82%8C%E3%81%A6%E3%81%BF%E3%81%9F%EF%BC%81%E8%B3%BC%E5%85%A5%E3%81%8B%E3%82%89%E5%88%9D%E6%9C%9F%E8%A8%AD%E5%AE%9A%E3%81%BE%E3%81%A7%20%7C%20DevelopersIO)[![twitter logo](/img/sns/twitter.svg)](https://twitter.com/intent/tweet?original_referer=https://dev.classmethod.jp/articles/devin-init/&text=%23DevelopersIO%20%E6%B3%A8%E7%9B%AE%E3%81%AEAI%E3%82%A8%E3%83%B3%E3%82%B8%E3%83%8B%E3%82%A2%E3%80%8CDevin%E3%80%8D%E3%82%92%E5%85%A5%E3%82%8C%E3%81%A6%E3%81%BF%E3%81%9F%EF%BC%81%E8%B3%BC%E5%85%A5%E3%81%8B%E3%82%89%E5%88%9D%E6%9C%9F%E8%A8%AD%E5%AE%9A%E3%81%BE%E3%81%A7%20https%3A%2F%2Fdev.classmethod.jp%2Farticles%2Fdevin-init%2F&t=%23DevelopersIO%20%E6%B3%A8%E7%9B%AE%E3%81%AEAI%E3%82%A8%E3%83%B3%E3%82%B8%E3%83%8B%E3%82%A2%E3%80%8CDevin%E3%80%8D%E3%82%92%E5%85%A5%E3%82%8C%E3%81%A6%E3%81%BF%E3%81%9F%EF%BC%81%E8%B3%BC%E5%85%A5%E3%81%8B%E3%82%89%E5%88%9D%E6%9C%9F%E8%A8%AD%E5%AE%9A%E3%81%BE%E3%81%A7%20)![Clock Icon](/img/clock.svg)2025.01.24

はじめに
----

今回は今注目されてるAIエンジニア「Devin」を調査のため購入したので、購入の流れや初期設定などを紹介します。本稿では、キャプチャなどを残しつつ初期のセットアップで必要な権限などに注目します。タスクを依頼した際の動作検証などは後続のブログで試していきます。

Devinをオンボーディングする上で、事前にSlackやGitHubで権限が必要です。購入前の権限確認などにご使用ください。

!

2025/01/21 時点の情報を記載しています。権限などが今後変更になる可能性はあるのでご注意ください。

Devinについて知らない方は以下のブログなどをご確認ください。

<https://www.cognition.ai/blog/devin-generally-available>

<https://zenn.dev/loglass/articles/2d48f39c3e6424>

Devinの購入
--------

まずは、以下のURLにアクセスして購入に進んでみます。

<https://app.devin.ai/>

まずSign upのボタンが出るので押下して、メールアドレス、Google or GitHub のSSOでアカウントを作成します。今回はGoogleでサインアップします。

![スクリーンショット 2025-01-20 18.08.50.png](https://devio2024-2-media.developers.io/upload/6SxfQhAuEvOXuP6ne0ms3I/2025-01-20/VoFJ3p5RcAtA.png)

![スクリーンショット 2025-01-20 18.10.33.png](https://devio2024-2-media.developers.io/upload/6SxfQhAuEvOXuP6ne0ms3I/2025-01-20/PQQcv4tXvXOy.png)

サインアップするとチャット画面がでます。GitHubとSlackへの招待を希望されます。GitLabやBitBucketへの対応はこれからですが、もうすぐのようです。  

今回はGitHubを使うので、`I use GitHub & Slack and am willing to provide access`を押下します。

![スクリーンショット 2025-01-20 18.27.45.png](https://devio2024-2-media.developers.io/upload/6SxfQhAuEvOXuP6ne0ms3I/2025-01-20/o6YzFR5QD3OY.png)

次に判別可能な組織名を聞かれるので入力します。今回は自分の所属する製造ビジネステクノロジー部の略称であるmbtを使います。GitHubやSlackのOrganizationsとは関係ないようです。

![スクリーンショット 2025-01-20 18.32.06.png](https://devio2024-2-media.developers.io/upload/6SxfQhAuEvOXuP6ne0ms3I/2025-01-20/W8ODzwSSrJjr.png)

サブスクリプションについて確認の画面が出ます。料金についてピックアップすると月額500ドルで購入でき、シート数は無制限で、月間250ACU(Agent Compute Unit)分使用できます。簡易的な翻訳も画像下に記載します。

![スクリーンショット 2025-01-20 18.35.13.png](https://devio2024-2-media.developers.io/upload/6SxfQhAuEvOXuP6ne0ms3I/2025-01-20/huQx3j2KLdte.png)

翻訳文

私と一緒に仕事をするためには、Teamsプランを購入する必要があります。サブスクリプション料金は月額500ドルで、以下が含まれます：

* 無制限のシート数
* すべてのタスクで私と協力して作業できます。特にフロントエンドタスク、バグ修正、リファクタリング、社内ツールの構築が得意です。
* Devin API、Slackインテグレーション、IDE拡張機能へのアクセス
* 月間250 ACU（Agent Compute Unit）の容量。1 ACUは約15分のDevinの作業時間に相当します。
* 参考までに、シンプルなフロントエンドのバグ修正には通常5-15分程度かかります。
* 追加のACUについては、設定した予算内で1 ACUあたり2ドルの従量課金オプションがあります。

`Purchase subscription`を押下して購入に進みます。購入はStripeを使って出来るようです。各々の決済方法で支払いします。

![スクリーンショット 2025-01-20 18.41.47.png](https://devio2024-2-media.developers.io/upload/6SxfQhAuEvOXuP6ne0ms3I/2025-01-20/KelcnZsGWfVy.png)

支払いが完了すると、月間の追加予算に関する設定が表示されます。サブスクした時点で250ACUはあるので、追加予算のデフォルトで500ですが今回は0で設定します。  

`This additional usage budget looks good to me`を押下します。

![スクリーンショット 2025-01-20 19.59.02.png](https://devio2024-2-media.developers.io/upload/6SxfQhAuEvOXuP6ne0ms3I/2025-01-20/v3u5Pvsp65Ef.png)

最後にDevinに適した働かせ方やタスクの与え方について紹介が入ります。画像下に簡易翻訳も記載します。`Start using Devin`で開始です！

![スクリーンショット 2025-01-20 20.02.18.png](https://devio2024-2-media.developers.io/upload/6SxfQhAuEvOXuP6ne0ms3I/2025-01-20/NXb37ssfj1g4.png)

私が最も効果的に働けるのは以下の場合です：

* 詳細な、ジュニアレベルのタスクを与えられた時
* 作業の検証方法を指示された時
* 3時間以上かかるタスクを分割された時
* 明確な要件が提供された時
* 私の知識ベースの改善を手伝ってもらえる時

私に適したタスクの例：

* 小規模なフロントエンドのバグやエッジケース — Slackのスレッドで私にメンションしてみてください
* バックログ作業の最初のPRドラフト作成 — 1日の始めにあなたのTODOリストからタスクを渡してみてください
* 特定のコードのリファクタリング — Devin IDE拡張機能を使用してみてください（VSCodeとそのフォーク向け）

参考ドキュメント

<https://docs.devin.ai/learn-about-devin/workflows>

GitHubのセットアップ
-------------

購入や事前処理が完了すると次はGitHubとの接続に移ります。Devinもエンジニアなのでオンボーディングが必要になります。`Connect to Github`から接続を進めます。

!

現状ではGitHub Orgのオーナー権のあるユーザでなければConnect GitHubの操作ができないようなので、`Invite Teammates`から管理者を招待して操作を行ってもらってください。またオーナーに直接`Devin.ai Integration`のGitHub Appを登録しても現状ではうまく連携できないようなので、後続のメンバーの追加作業後に実施してください。

![スクリーンショット 2025-01-20 20.06.29.png](https://devio2024-2-media.developers.io/upload/6SxfQhAuEvOXuP6ne0ms3I/2025-01-20/Dg7oB23OMAJM.png)

GitHubの個人アカウントかOrganizationsを選択して、権限を付与します。全リポジトリ一括か、リポジトリ単位で設定することもできます。

![スクリーンショット 2025-01-20 20.09.36.png](https://devio2024-2-media.developers.io/upload/6SxfQhAuEvOXuP6ne0ms3I/2025-01-20/KE2Qyqvn2Ugc.png)

権限についてもスクロールすると記載されています。主にコードやissue/PR/ワークフローなどへのRead/Writeの権限と、付随する情報のRead権限を必要とします。詳細はテキストとして画像下に転記します。

![スクリーンショット 2025-01-20 20.10.40.png](https://devio2024-2-media.developers.io/upload/6SxfQhAuEvOXuP6ne0ms3I/2025-01-20/avAmjIG1NFZ1.png)

* Read access to Dependabot alerts, actions, checks, commit statuses, deployments, members, metadata, packages, pages, repository advisories, repository hooks, and repository projects
* Read and write access to code, discussions, issues, pull requests, and workflows

もしOrganizationsへGitHub Appsをインストールする権限がない場合は、以下のようにエラーになるのでご注意ください。

![スクリーンショット 2025-01-20 20.13.44.png](https://devio2024-2-media.developers.io/upload/6SxfQhAuEvOXuP6ne0ms3I/2025-01-20/CVRSyu6LdidE.png)

Slackのセットアップ
------------

次はSlackをセットアップします。DevinにSlack上でメンションして依頼できるように、Slack Organizationsと連携します。`Connect Slack Organization`を押下します。

![スクリーンショット 2025-01-20 20.23.53.png](https://devio2024-2-media.developers.io/upload/6SxfQhAuEvOXuP6ne0ms3I/2025-01-20/Xtda9nNmaa4E.png)

Slack上で以下の権限が必要になります。

```
- あなたに関するコンテンツと情報
  - あなたのメールアドレスを表示
  - あなたの ID に関する情報にアクセスする
  - 自分の Slack アバターと Slack ワークスペースの基本情報を表示する
- チャンネルと会話に関するコンテンツと情報
  - Devinが連携されたパブリックチャンネルでメッセージやその他のコンテンツにアクセスする
  - あなたのワークスペースのパブリックチャンネルに関する基本情報にアクセスする
  - Devinが連携されたチャンネルと会話で共有されたファイルにアクセスする
  - Devinが連携されたプライベートチャンネルでメッセージやその他のコンテンツにアクセスする
  - Devinが連携されたプライベートチャンネルに関する基本情報にアクセスする
  - Devinが連携されたダイレクトメッセージでメッセージやその他のコンテンツにアクセスする
  - Devinが連携されたダイレクトメッセージに関する基本情報にアクセスする
  - Devinが連携されたグループ DM に関する基本情報にアクセスする
  - Devinが連携されたチャンネルと会話で絵文字リアクションや関連するコンテンツへアクセスする
- ワークスペースに関するコンテンツと情報
  - Devinが接続されたワークスペースの名前、メールドメインやアイコンにアクセスする
  - あなたのワークスペースのメンバーに関するプロフィールの詳細にアクセスする
  - あなたのワークスペースのメンバーを閲覧する
  - あなたのワークスペースメンバーのメールアドレスを閲覧する
- Devin は、以下を実行できるようになります :
  - チャンネルと会話でアクションを実行する
    - アプリが参加している会話で @Devin を直接メンションしているメッセージを表示
    - @Devin としてメッセージを送信する
    - カスタムのユーザー名とアバターを使用して @Devin としてメッセージを送信する
    - Devinとしてファイルをアップロード、編集、削除する
    - 他のメンバーとダイレクトメッセージを開始する
    - 絵文字リアクションを追加または削除する
- あなたのワークスペースでアクションを実行する
  - ユーザーが使用できるショートカットやスラッシュコマンドを追加する

```

認証が終わると元の画面で認証が確認でき、次にUserをLinkする必要があります。`Link User`を押下します。押下すると自動でユーザ情報が連携されます。

![スクリーンショット 2025-01-21 15.02.51.png](https://devio2024-2-media.developers.io/upload/6SxfQhAuEvOXuP6ne0ms3I/2025-01-21/7UUKJd3OC4lb.png)

メンバーの追加
-------

必要に応じてメールアドレスからメンバーの追加を行ってください。後から実行可能なので今回は飛ばします。

リポジトリのセットアップ
------------

最後にリポジトリのセットアップです。GitHub App上で許可したリポジトリが灰色の部分に表示されるので、今回使う内容を選択します。選択した後、青い部分を押下します。

![スクリーンショット 2025-01-21 17.02.53.png](https://devio2024-2-media.developers.io/upload/6SxfQhAuEvOXuP6ne0ms3I/2025-01-21/plI6nt0vfrnW.png)

今回は以下のリポジトリの内部向けで管理している方を利用します。コードの内容は公開しているものとほぼ同じです。

<https://github.com/classmethod/icasu-cdk-serverless-api-sample>

すると以下のようにポップアップが出てきて、Cloneが自動で動き出します。

![スクリーンショット 2025-01-21 17.17.53.png](https://devio2024-2-media.developers.io/upload/6SxfQhAuEvOXuP6ne0ms3I/2025-01-21/ckTecd91d0uR.png)

どうやら自分で依存関係とlint,testの実行が必要なようです。実行していき、完了したらDoneボタンを押していきます。

```
% npm run install:recommended-vscode-extensions #リポジトリの手順のため実行
% npm ci
% npm run test-unit

```

リポジトリの状態を最新にするための設定を行います。リポジトリ自体のpullと依存関係のコマンドを設定します。

![スクリーンショット 2025-01-21 17.34.05.png](https://devio2024-2-media.developers.io/upload/6SxfQhAuEvOXuP6ne0ms3I/2025-01-21/PGIiicdbX4Sv.png)

`Pulling latest changes`の`Test`を押下すると実際に、動作するか確認できます。

![スクリーンショット 2025-01-21 17.34.59.png](https://devio2024-2-media.developers.io/upload/6SxfQhAuEvOXuP6ne0ms3I/2025-01-21/XFw7TGg5t4cy.png)

依存関係の方のコマンドは自分で作成します。今回は以下としました。

```
cd ~/repos/icasu-cdk-serverless-api-sample && npm ci

```

最後にDevinに対するナレッジを追加します。テストの実行方法やPRのフォーマットなどの情報を渡してオンボーディングします。

![スクリーンショット 2025-01-21 17.51.57.png](https://devio2024-2-media.developers.io/upload/6SxfQhAuEvOXuP6ne0ms3I/2025-01-21/cOIb0Aedj7QR.png)

初期は以下の内容が入っていました。`npm ci`などコマンドからDependabotの使用などリポジトリを読み取って入力してくれるようです。

```
Dependencies
- Install all workspace dependencies with:
  `npm ci`

Code Formatting & Linting
- Check formatting: `npm run check:format`
- Check linting: `npm run check:lint`
- Check TypeScript types: `npm run check:type`
- Check spelling: `npm run check:cspell`

Verifying correctness
- When verifying your code, you should run lint with `npm run lint` and auto-fix with `npm run lint -- --fix`.
- You should generally not worry about running the code or local testing. Prefer to use the tests that are automatically run in CI as a feedback loop for your PRs.
- Assume that you are not able to run tests locally unless a human has deliberately provided verifiably working instructions. Generic instructions for testing in the README often do not work since you may require specific environment variables or other machine setup to be able to properly run tests.
    - If you are asked to run tests, a local dev server, or otherwise interact with a running application, you should tell the human user to update your Knowledge with verifiably working instructions on how to run tests in your environment.
    - You should primarily rely on both human review and CI to verify that your code is functionally and stylistically correct
- If you have in fact been provided with verifiably working instructions on how to run tests in your environment, then the bullet point about not running tests locally is not relevant (and humans editing this note should feel free to update this section).

PR Guidelines
- The repository uses Dependabot for automated dependency updates
- For patch and minor version updates:
  - Verify no breaking changes in dependencies
  - Ensure tests pass
  - Confirm minimal production impact
- For major version updates:
  - Additional caution required
  - Consider separating version updates from feature releases
  - Consider enhanced production monitoring

```

翻訳

```
- 依存関係
  - ワークスペースの依存関係をすべてインストールするには： npm ci

- コードフォーマットとリント
  - フォーマットのチェック：npm run check:format
  - リントのチェック：npm run check:lint
  - TypeScriptの型チェック：npm run check:type
  - スペルチェック：npm run check:cspell
- 正確性の検証
  - コードを検証する際は、npm run lintでリントを実行し、npm run lint -- --fixで自動修正を行ってください。
  - 一般的に、コードのローカル実行やテストは気にしないでください。PRのフィードバックループとしてCIで自動実行されるテストを利用することを推奨します。
  - 人間が検証済みの動作手順を明示的に提供していない限り、ローカルでテストを実行できないと想定してください。READMEにある一般的なテスト手順は、特定の環境変数や他のマシン設定が必要なため、正常に動作しないことがあります。
  - テストの実行、ローカル開発サーバーの起動、または実行中のアプリケーションとの対話を求められた場合、あなたの環境でテストを実行するための検証済みの手順を更新するよう、人間のユーザーに依頼してください。
  - コードが機能的にもスタイル的にも正しいことを確認するには、主に人間のレビューとCIに依存してください。
  - 実際にあなたの環境でテストを実行するための検証済みの手順が提供されている場合、ローカルでテストを実行しないという項目は関係ありません（この部分の編集は人間が自由に行えます）。

- PRガイドライン
  - このリポジトリは依存関係の自動更新にDependabotを使用しています
  - パッチおよびマイナーバージョンの更新の場合：
    - 依存関係に破壊的な変更がないことを確認
    - テストが合格することを確認
    - 本番環境への影響が最小限であることを確認
  - メジャーバージョンの更新の場合：
    - より慎重な対応が必要
    - バージョン更新と機能リリースの分離を検討
    - 本番環境の監視強化を検討

```

修正を依頼されていますが今回はそのままで進めます。`I have reviewed the pre-generated suggestions and confirm they are correct`をチェックしてセーブします。これで`Finish`を押せば以下の画面が表示されるので`Finish Setup`を押下し、オンボーディングは完了です。

![スクリーンショット 2025-01-21 17.54.28.png](https://devio2024-2-media.developers.io/upload/6SxfQhAuEvOXuP6ne0ms3I/2025-01-21/7vMBMS6e7biC.png)

ステップの詳細を確認したい場合は、動画も公開されているのでこちらもご確認ください。

<https://www.loom.com/share/8612d68820ef402c84d903c603ac7b32?sid=0045d2ae-6c2d-4445-a2b1-9433978d9d0f>

最後に招待したSlack上で会話すると、Devinが返答してくれます。これでいつでもSlackからDevinに依頼できそうです。

![スクリーンショット 2025-01-21 18.04.14.png](https://devio2024-2-media.developers.io/upload/6SxfQhAuEvOXuP6ne0ms3I/2025-01-21/iJ6asnA62Smk.png)

ちなみに、Devinに作業依頼を行った後Devin内での作業が完了するとユーザ側からの返答が待たれます。返答を素早く行うためにDevinは0.5hの間待機時間になるので、その分も課金が発生します。追加の作業指示が出来ない場合は、早めに`SLEEP`と打って作業を止めてもらうことをおすすめします。また`SLEEP`は斜体などが入っているとうまく認識されないみたいです。自分は途中まで気づかず挨拶だけで1ドル弱消費分しました…

所感
--

GitHubで管理者相当権限が必要なので、大規模組織で試すにはハードル高そうでしたが権限とお金さえあれば開始することは簡単でした。まだ実際のタスクを任せていないので、次の記事では簡単なタスクを依頼して、どの程度ならお願いできるのか探っていきます。

