[![](https://qiita-user-profile-images.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F4019%2Fprofile-images%2F1713835394?ixlib=rb-4.0.0&auto=compress%2Cformat&lossless=0&w=48&s=cc18a511696773705186943f502876ba)@tichise(Ichise Takuya)](/tichise)

Cursor 0.49で開発効率化：柔軟なターミナル操作とグローバル無視設定の実装
=========================================

* [AI](/tags/ai)
* [cursor](/tags/cursor)
* [LLM](/tags/llm)
* [VibeCoding](/tags/vibecoding)

Posted at 2025-05-02

**はじめに**
--------

Cursorの最新バージョン0.49がリリースされ、AIを活用したコーディング体験がさらに向上しました。今回のアップデートではルール生成、改良されたエージェントターミナルとMCP画像など、多くの機能強化が含まれています。この記事では、公式情報をベースに解説をしていきます。

[Changelog - Apr 15, 2025 | Cursor - The AI Code Editor | Cursor - The AI Code Editor](https://www.cursor.com/ja/changelog/0-49)

**自動化と改良されたCursor Rules**
-------------------------

`/Generate Cursor Rules`コマンドを使用して、Chatから直接Cursor Rulesを生成できるようになりました。これは、会話の既存のコンテキストをキャプチャして後で再利用したい場合に便利です。

`Auto Attached`パスパターンが定義されたルールの場合、エージェントはファイルの読み取りまたは書き込み時に適切なルールを自動的に適用するようになりました。

Rule Type `Auto Attached`が定義されたCusor Rulesの場合、エージェントはファイルの読み取りまたは書き込み時に適切なルールを自動的に適用するようになりました。

Rule Type `Always`が定義されたCusor Rulesの場合、以前は会話が長くなるとルールが外れてしまうことがあったが、長い会話の中でも持続して適用されるようになりました。

### **解説**

このアップデートでは、Cursorのルール機能が強化されました。会話内容からルールを自動生成する機能や、パスパターンに基づいて適切なルールを適用する機能が追加されています。

### **機能の利用手順**

1. チャット画面で会話が行われた後、`/Generate Cursor Rules`コマンドを入力する

[![](https://qiita-user-contents.imgix.net/https%3A%2F%2Fstorage.googleapis.com%2Fzenn-user-upload%2Ffdb7502931f6-20250428.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=00c2e956a8171fe5a6d8f79a1aa3b414)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fstorage.googleapis.com%2Fzenn-user-upload%2Ffdb7502931f6-20250428.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=00c2e956a8171fe5a6d8f79a1aa3b414)

**よりアクセスしやすい履歴**
----------------

チャット履歴がコマンドパレットに移動しました。チャット内の「Show Chat History」および「Show Chat History」コマンドからアクセスできます。

### **解説**

チャット履歴へのアクセス方法が改善され、より使いやすくなりました。

### **機能の利用手順**

1. チャット画面内の「Show Chat History」ボタンをクリックする

[![](https://qiita-user-contents.imgix.net/https%3A%2F%2Fstorage.googleapis.com%2Fzenn-user-upload%2F95c9d2abcf44-20250428.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=ed1dd49f9410f9820fbab15b868e9921)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fstorage.googleapis.com%2Fzenn-user-upload%2F95c9d2abcf44-20250428.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=ed1dd49f9410f9820fbab15b868e9921)

**レビューの簡易化**
------------

各会話の最後に組み込まれた差分ビューにより、エージェントが生成したコードのレビューがより簡単になりました。エージェントからのメッセージの後、チャットの下部に「Review Changes」ボタンが表示されます。

### **解説**

コードレビュープロセスが改善され、エージェントが生成したコードの変更点を簡単に確認できるようになりました。

### **機能の利用手順**

1. AIがコードを生成または編集した後、チャットの下部に表示される「Review Changes」ボタンをクリック
2. 表示された差分ビューで追加されたコード（緑色）と削除されたコード（赤色）を確認
3. 変更内容に問題がなければ承認し、必要に応じて部分的に変更を適用することも可能

[![](https://qiita-user-contents.imgix.net/https%3A%2F%2Fstorage.googleapis.com%2Fzenn-user-upload%2F2a335b1684e3-20250428.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=684e65235e20983468d59f07bcc52850)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fstorage.googleapis.com%2Fzenn-user-upload%2F2a335b1684e3-20250428.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=684e65235e20983468d59f07bcc52850)

**MCPでの画像**
-----------

MCPサーバーのコンテキストの一部として画像を渡せるようになりました。スクリーンショット、UIモック、または図表が質問やプロンプトに不可欠なコンテキストを追加する場合に役立ちます。

### **解説**

MCP（Model Control Panel）サーバーで画像をサポートするようになり、視覚的な情報をAIとの対話に含めることができます。

**改良されたエージェントターミナル制御**
----------------------

エージェントが開始するターミナルに対するより多くの制御が追加されました。コマンドは実行前に編集したり、完全にスキップしたりできるようになりました。また、「Pop-out」を「Move to background」に改名し、その機能をより明確に反映させました。

### **解説**

エージェントが提案するターミナルコマンドに対するユーザーの制御が強化されました。

### **機能の利用手順**

1. AIにターミナルコマンドの実行を依頼する
2. AIが提案したコマンドが表示されたら、そのまま実行、編集して実行、またはスキップを選択
3. コマンドを編集する場合は、表示されたコマンド入力欄で直接テキストを修正
4. 「Run」ボタンをクリックしてコマンドを実行するか、「Skip」を選択して次のステップに進む
5. 長時間実行されるコマンドは「Move to background（バックグラウンドに移動）」ボタンを使って別ウィンドウで実行可能

[![](https://qiita-user-contents.imgix.net/https%3A%2F%2Fstorage.googleapis.com%2Fzenn-user-upload%2F0db03b735401-20250428.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=72a134400fadf1644594a8a39453d61a)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fstorage.googleapis.com%2Fzenn-user-upload%2F0db03b735401-20250428.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=72a134400fadf1644594a8a39453d61a)

### 注意事項

Enable auto-run modeが有効になってると、この提案は表示されません。

[![](https://qiita-user-contents.imgix.net/https%3A%2F%2Fstorage.googleapis.com%2Fzenn-user-upload%2F092f6384713a-20250428.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=02fae27382b914c94fe2d4e5937480d7)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fstorage.googleapis.com%2Fzenn-user-upload%2F092f6384713a-20250428.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=02fae27382b914c94fe2d4e5937480d7)

**グローバル無視ファイル**
---------------

ユーザーレベルの設定を通じて、すべてのプロジェクトに適用されるグローバル無視パターンを定義できるようになりました。これにより、プロジェクトごとの設定を必要とせずに、ビルド出力やシークレットなどのノイズの多いファイルや機密ファイルをプロンプトから除外できます。

### **解説**

ユーザーレベルの設定で特定のファイルを除外するためのグローバル設定が可能になりました。グローバル無視ファイルには主に2つの目的があります。

* **セキュリティ**: APIキーやデータベース認証情報などの機密ファイルをAIから隠すことができます。ただし、予測不可能なLLMの動作により、完全な保護は保証できないことに注意してください。
* **パフォーマンス**: 大規模なモノレポや巨大なコードベースで作業する場合、関連性の低い部分を除外することでインデックス作成速度が向上し、コンテキスト検索の精度も上がります。

### **機能の利用手順**

[Cursor – Ignore Files](https://docs.cursor.com/context/ignore-files#global-ignore-files)

**新しいモデル**
----------

最近、使用できる多くの新しいモデルが追加されました。モデル設定から、Gemini 2.5 Pro、Gemini 2.5 Flash、Grok 3、Grok 3 Mini、GPT-4.1、o3およびo4-miniを試してみてください。

### **解説**

より多くのAIモデルがCursorで利用可能になり、用途に応じて選択肢が増えました。

[Cursor – Models](https://docs.cursor.com/settings/models)

**まとめ**
-------

Cursor 0.49では、ルール生成の自動化、履歴アクセスの改善、エージェントターミナルの制御強化など、開発体験を向上させる多くの機能が追加されました。特に、コードレビューの簡易化や画像サポートの追加は、より直感的なAIとの対話を可能にし、グローバル無視ファイル機能は、大規模プロジェクトでの作業効率を高めます。また、新しいAIモデルの追加により、より高度なコード生成と問題解決が可能になりました。これらの改善により、Cursorはより強力で使いやすい開発ツールへと進化しています。

[0](/tichise/items/6c4a21d47dc7ee0968eb/likers)

Go to list of users who liked

1[comment0](#comments)

Go to list of comments

Register as a new user and use Qiita more conveniently

1. You get articles that match your needs
2. You can efficiently read back useful information
3. You can use dark theme

[What you can do with signing up](https://help.qiita.com/ja/articles/qiita-login-user)[Sign up](/signup?callback_action=login_or_signup&redirect_to=%2Ftichise%2Fitems%2F6c4a21d47dc7ee0968eb&realm=qiita)[Login](/login?callback_action=login_or_signup&redirect_to=%2Ftichise%2Fitems%2F6c4a21d47dc7ee0968eb&realm=qiita)