[![kun432](https://lh3.googleusercontent.com/a-/AOh14Gj2-TWBIJGuFBxhPY_QFO7z0tZ3sGpJSf9rPLKPLg=s80-c)](/kun432)[kun432](/kun432)[5ヶ月前に更新](#comment-8603201b328815)

<https://note.com/shi3zblog/n/n7fa9f36e694c>

> こいつの何がすごいかというと、gitをcloneしてくると、ソースコード読ませて「これにこういう機能を追加しろ」と言うと勝手に追加してgit commitしてしまう。良きところで/git push origin mainとやればやってくれる。

> このツールのすごいところは、ユーザー(開発者)が完全に受け身になると言うこと。
> 
> これまでのAI支援開発ツールは、あくまでも「支援」にとどまっていた。作りたいものをどう作るかイメージするのはプログラマで、AIはそれをサポートする役だった。その方が、開発者は入ってきやすい。
> 
> しかしAIderによる開発は、支援ではない。むしろ開発請負ツールと言ってもいい。
> 
> AIderに対してユーザーは一切遠慮しなくていい。  
> 
> 「こう言うものを作れ」と言ったらAIderは勝手に作るし、「この機能を作れ」と言ってもAIderは勝手に作る。
> 
> AIderの対話環境は「エディタ」ではなくチャットに近い。  
> 
> しかし単なるチャットと違うのは、ソースコードを適宜修正してくれるところだ。

ドキュメント  

<https://aider.chat/>

GitHubレポジトリ  

<https://github.com/paul-gauthier/aider>

> ### AiderはあなたのターミナルでAIペアプログラミングをする
> 
> Aiderを使えば、LLMとペアプログラムを組んで、ローカルのgitリポジトリのコードを編集できる。新しいプロジェクトを始めるか、既存のgitリポジトリで作業しよう。AiderはGPT-4oとクロード3.5ソネットで最適に動作し、ほとんどのLLMに接続できる。

> ### 機能
> 
> * 編集したいファイルを指定して aider を実行： `aider <file1> <file2> ...`
> * 変更を求める：
>   + 新しい機能やテストケースを追加する。
>   + バグを記述する。
>   + エラーメッセージか GitHub issue URL を貼り付ける。
>   + コードをリファクタリングする。
>   + ドキュメントを更新する。
> * Aiderは、あなたのリクエストを完了するためにファイルを編集する。
> * Aiderは、適切なコミットメッセージで変更を[自動的にgitコミット](https://aider.chat/docs/git.html)する。
> * Aiderは、[ほとんどの一般的な言語](https://aider.chat/docs/languages.html)で動作する： python、javascript、typescript、php、html、cssなど。
> * AiderはGPT-4oとClaude 3.5 Sonnetで最適に動作し、[ほとんどのLLMに接続](https://aider.chat/docs/llms.html)できる。
> * Aiderは複雑なリクエストのために一度に複数のファイルを編集できる。
> * Aider は [git リポジトリ全体のマップを使用](https://aider.chat/docs/repomap.html)するので、大きなコードベースでもうまく動作する。
> * aiderとチャットしながらエディターでファイルを編集すれば、常に最新バージョンを使用する。AIとペアプログラムを組む。
> * チャットに画像を追加（GPT-4o、Claude 3.5 Sonnetなど）。
> * [チャットにURLを追加](https://aider.chat/docs/usage/images-urls.html)して、その内容をエイダーが読む。
> * [あなたの声でコードを書く](https://aider.chat/docs/usage/voice.html)。

返信[![kun432](https://lh3.googleusercontent.com/a-/AOh14Gj2-TWBIJGuFBxhPY_QFO7z0tZ3sGpJSf9rPLKPLg=s80-c)](/kun432)[kun432](/kun432)[4ヶ月前に更新](#comment-58b7d81a9ce014)

Getting Startedを進めてみる。CLIの対話ベースなのでローカルのMacで。

Pythonのパッケージでインストール。事前に仮想環境を作っておくと良い。

```
$ pip install aider-chat

```

サンプルとして以下のレポジトリを使わせていただく。シンプルはOpenAI APIを使ったStreamlitのチャットボットアプリ

<https://github.com/streamlit/chatbot-template>

```
$ git clone https://github.com/streamlit/chatbot-template
$ cd chatbot-template
$ pip install -r requirements.txt

```

試しに動かしてみる。

```
$ streamlit run streamlit_app.py

```

![](https://storage.googleapis.com/zenn-user-upload/5f9f602aae84-20240813.png)

こんな感じでチャットできる。Streamlitアプリはこのまま上げたままにしておいて、別ターミナルを開いてレポジトリディレクトリに移動しておく。

ではAiderを使ってみる。今回はOpenAI gpt-4oを使ってやってみる。OpenAI APIキーを環境変数にセットする。

```
$ export OPENAI_API_KEY=XXXXXXXXX

```

Aiderを起動

```
$ aider

```

Aiderはどうやらファイルを生成するらしく、`.aider*`というプレフィクスになる。これを.gitignoreに追加するか聞かれるので`y`

```
Add .aider* to .gitignore (recommended)? y

```

以下のように表示される。

```
Added .aider* to .gitignore
Aider v0.46.1
Models: gpt-4o with diff edit format, weak model gpt-4o-mini
Git repo: .git with 7 files
Repo-map: using 1024 tokens
Use /help <question> for help, run "aider --help" to see cmd line args
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
>

```

ヘルプを見てみる。

```
> /help

/add       Add files to the chat so GPT can edit them or review them in detail
/ask       Ask questions about the code base without editing any files
/chat-mode Switch to a new chat mode
/clear     Clear the chat history
/commit    Commit edits to the repo made outside the chat (commit message optional)
/diff      Display the diff of the last aider commit
/drop      Remove files from the chat session to free up context space
/exit      Exit the application
/git       Run a git command
/help      Ask questions about aider
/lint      Lint and fix provided files or in-chat files if none provided
/ls        List all known files and indicate which are included in the chat session
/model     Switch to a new LLM
/models    Search the list of available models
/quit      Exit the application
/run       Run a shell command and optionally add the output to the chat (alias: !)
/test      Run a shell command and add the output to the chat on non-zero exit code
/tokens    Report on the number of tokens used by the current chat context
/undo      Undo the last git commit if it was done by aider
/voice     Record and transcribe voice input
/web       Use headless selenium to scrape a webpage and add the content to the chat

```

日本語訳

```
/add       ファイルをチャットに追加して、GPTが編集したり、詳しくレビューできるようにする。
/ask       ファイルを編集せずにコードベースについて質問する
/chat-mode チャットモードを切り替える
/clear     チャット履歴を消去する
/commit    チャット外で行われたリポジトリへの編集をコミットする（コミットメッセージは任意）
/diff      最後の aider commit の diff を表示する
/drop      チャットセッションからファイルを削除してコンテキストスペースを空ける
/exit      アプリケーションを終了する
/git       コマンドを実行する
/aider     aiderに関する質問をする
/lint      提供されたファイル、または提供されていない場合はチャット内のファイルをLintして修正する
/ls        すべての既知のファイルをリストアップし、どれがチャットセッションに含まれているかを示す
/model     新しい LLM に切り替える。
/models    利用可能なモデルのリストを検索する
/quit      アプリケーションを終了する
/run       シェルコマンドを実行し、オプションで出力をチャットに追加する (エイリアス: !)
/test      シェルコマンドを実行し、終了コードが0以外の場合にチャットに出力を追加する。
/tokens    現在のチャットコンテキストで使用されているトークンの数を報告する
/undo      最後の git コミットが aider によって行われた場合、それを元に戻す
/voice     音声入力を録音して書き起こす
/web       ヘッドレスSeleniumを使ってウェブページをスクレイピングし、その内容をチャットに追加する

```

軽く試してみる。

Aiderではまず編集したいファイルを会話の中に追加する必要がある。`/ls`でみてみると現在の会話に追加されているファイルが確認できる。

```
> /ls

Repo files not in the chat:

  .devcontainer/devcontainer.json
  .github/CODEOWNERS
  .gitignore
  LICENSE
  README.md
  requirements.txt
  streamlit_app.py

```

ファイルが何も追加されていない。ではファイルを追加する。

```
> /add streamlit_app.py

```

会話に追加された

```
> /ls

Repo files not in the chat:

  .devcontainer/devcontainer.json
  .github/CODEOWNERS
  .gitignore
  LICENSE
  README.md
  requirements.txt

Files in chat:

  streamlit_app.py
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
streamlit_app.py
>

```

ではこのファイルについてチャットで色々やってみる。

```
streamlit_app.py
> このファイルについて説明して。

```
```
このファイル streamlit_app.py は、Streamlit を使用して OpenAI の GPT-3.5
モデルを利用したチャットボットアプリケーションを構築するための Python
スクリプトです。以下に、このファイルの主要な部分について説明します。

 1 インポート:

    import streamlit as st
    from openai import OpenAI

    • streamlit モジュールと openai モジュールをインポートしています。
 2 タイトルと説明の表示:

    st.title("💬 Chatbot")
    st.write(
        "This is a simple chatbot that uses OpenAI's GPT-3.5 model to generate responses. "
        "To use this app, you need to provide an OpenAI API key, which you can get
    [here](https://platform.openai.com/account/api-keys). "
        "You can also learn how to build this app step by step by [following our
    tutorial](https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps)."
    )

    • アプリケーションのタイトルと説明を表示します。
 3 APIキーの入力:

    openai_api_key = st.text_input("OpenAI API Key", type="password")
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.", icon="🗝️")
    else:

    • ユーザーに OpenAI API キーを入力させます。キーが入力されていない場合は、情報メッセージを表示します。
 4 OpenAI クライアントの作成:

    client = OpenAI(api_key=openai_api_key)

 5 セッション状態の管理:

    if "messages" not in st.session_state:
        st.session_state.messages = []

 6 既存のチャットメッセージの表示:

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

 7 チャット入力フィールドの作成:

    if prompt := st.chat_input("What is up?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

 8 OpenAI API を使用した応答の生成:

    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
             {"role": m["role"], "content": m["content"]}
             for m in st.session_state.messages
         ],
         stream=True,
     )

  9 応答のストリーミングと表示:

     with st.chat_message("assistant"):
         response = st.write_stream(stream)
     st.session_state.messages.append({"role": "assistant", "content": response})


このスクリプトは、ユーザーが入力したメッセージを OpenAI の GPT-3.5
モデルに送信し、その応答をチャット形式で表示するシンプルなチャットボットアプリケーションを実現しています。


Tokens: 2,670 sent, 839 received. Cost: $0.03 request, $0.03 session.

```

実際にはこんな感じでカラーリングされて表示される。

![](https://storage.googleapis.com/zenn-user-upload/6f59e4cb0f33-20240730.png)

少し編集させてみる。

```
streamlit_app.py
> 説明を日本語に書き換えて。

```
```
以下の変更を行います。

 1 タイトルを日本語に変更します。
 2 説明文を日本語に変更します。

streamlit_app.py


 <<<<<<< SEARCH
 # Show title and description.
 st.title("💬 Chatbot")
 st.write(
     "This is a simple chatbot that uses OpenAI's GPT-3.5 model to generate responses. "
     "To use this app, you need to provide an OpenAI API key, which you can get
 [here](https://platform.openai.com/account/api-keys). "
     "You can also learn how to build this app step by step by [following our
 tutorial](https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps)."
 )
 =======
 # タイトルと説明を表示します。
 st.title("💬 チャットボット")
 st.write(
     "これは、OpenAI の GPT-3.5 モデルを使用して応答を生成するシンプルなチャットボットです。"
     "このアプリを使用するには、OpenAI API キーを提供する必要があります。API キーは
 [こちら](https://platform.openai.com/account/api-keys) から取得できます。"
     "このアプリの作成方法については、[こちらのチュートリアル](https://docs.streamlit.io/develop/tutorials/llms/build-c
 versational-apps) をご覧ください。"
 )
 >>>>>>> REPLACE



Tokens: 6,422 sent, 363 received. Cost: $0.04 request, $0.10 session.
Applied edit to streamlit_app.py
Commit 92c8311 Translate title and description to Japanese.
You can use /undo to revert and discard commit 92c8311.
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

```

git logを見てみる。

```
$ git log
commit 92c8311343eae3d2262e3ca14a7e39c2341ab402 (HEAD -> main)
Author: kun432 (aider) <kun432@users.noreply.github.com>
Date:   Tue Jul 30 14:37:29 2024 +0900

    Translate title and description to Japanese.

```
```
$ git show 92c8311343eae3d2262e3ca14a7e39c2341ab402
commit 92c8311343eae3d2262e3ca14a7e39c2341ab402 (HEAD -> main)
Author: kun432 (aider) <kun432@users.noreply.github.com>
Date:   Tue Jul 30 14:37:29 2024 +0900

    Translate title and description to Japanese.

diff --git a/streamlit_app.py b/streamlit_app.py
index 1504769..a008e66 100644
--- a/streamlit_app.py
+++ b/streamlit_app.py
@@ -1,12 +1,12 @@
 import streamlit as st
 from openai import OpenAI

-# Show title and description.
-st.title("💬 Chatbot")
+# タイトルと説明を表示します。
+st.title("💬 チャットボット")
 st.write(
-    "This is a simple chatbot that uses OpenAI's GPT-3.5 model to generate responses. "
-    "To use this app, you need to provide an OpenAI API key, which you can get [here](https://platform.openai.com/account/api-keys). "
-    "You can also learn how to build this app step by step by [following our tutorial](https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps)."
+    "これは、OpenAI の GPT-3.5 モデルを使用して応答を生成するシンプルなチャットボットです。"
+    "このアプリを使用するには、OpenAI API キーを提供する必要があります。API キーは [こちら](https://platform.openai.com/account/api-keys) から取得できます。"
+    "このアプリの作成方法については、[こちらのチュートリアル](https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps) をご覧ください。"
 )

 # Ask user for their OpenAI API key via `st.text_input`.


```

修正してコミットまでされている！

StreamlitアプリでRun on Saveを有効にしておくと、書き換わったコードで動作しているのがわかる。

![](https://storage.googleapis.com/zenn-user-upload/5801c6442803-20240730.png)

なお、ファイル追加は以下のようにコマンドラインからの起動時に指定することもできる。

```
$ aider streamlit_app.py 

```

`/quit`または`/exit`で会話を終了する。

```
> /quit

$

```

ディレクトリの中身を見てみると`.aider`で始まるファイルがいくつか作成されている

```
$ ls -la
total 96
drwxr-xr-x@ 13 kun432  staff    416  7 30 14:15 .
drwxr-xr-x@  6 kun432  staff    192  7 30 13:53 ..
-rw-r--r--@  1 kun432  staff  13058  7 30 14:47 .aider.chat.history.md
-rw-r--r--@  1 kun432  staff    739  7 30 14:47 .aider.input.history
drwxr-xr-x@  5 kun432  staff    160  7 30 14:14 .aider.tags.cache.v3
(snip)

```
返信[![kun432](https://lh3.googleusercontent.com/a-/AOh14Gj2-TWBIJGuFBxhPY_QFO7z0tZ3sGpJSf9rPLKPLg=s80-c)](/kun432)[kun432](/kun432)[5ヶ月前](#comment-35d86f1622c622)

コマンドラインオプションも豊富

<https://aider.chat/docs/config/options.html>

返信[![kun432](https://lh3.googleusercontent.com/a-/AOh14Gj2-TWBIJGuFBxhPY_QFO7z0tZ3sGpJSf9rPLKPLg=s80-c)](/kun432)[kun432](/kun432)[5ヶ月前に更新](#comment-662ecd47ba6935)

Aiderには簡易なGUIも用意されている。`--gui`で起動するとブラウザでStreamlitベースのチャットが立ち上がる。

```
$ aider --gui

```

使い方は同じ。ファイルを追加して、指示を出す。

![](https://storage.googleapis.com/zenn-user-upload/c1faa5a307b9-20240730.png)

回答が英語になってしまったが、最初に「日本語で」みたいな指示をすれば問題ないと思う。

こんな感じで修正された。

![](https://storage.googleapis.com/zenn-user-upload/bb61c2a32b06-20240730.png)

返信[![kun432](https://lh3.googleusercontent.com/a-/AOh14Gj2-TWBIJGuFBxhPY_QFO7z0tZ3sGpJSf9rPLKPLg=s80-c)](/kun432)[kun432](/kun432)[5ヶ月前に更新](#comment-7f097c07dc63f2)

VSCodeのターミナル内で使うのが現実的には良さそうかなぁ、コードも見たいしね。devcontainerの設定とセットで用意しておくと良さそう。

返信[![kun432](https://lh3.googleusercontent.com/a-/AOh14Gj2-TWBIJGuFBxhPY_QFO7z0tZ3sGpJSf9rPLKPLg=s80-c)](/kun432)[kun432](/kun432)[5ヶ月前](#comment-12ba924623e11e)

結構ドキュメントのボリュームはある感じ

<https://aider.chat/>

使い方とかはこのあたりを見るのが良さそう

<https://aider.chat/docs/usage.html>

<https://aider.chat/examples/README.html>

返信[![kun432](https://lh3.googleusercontent.com/a-/AOh14Gj2-TWBIJGuFBxhPY_QFO7z0tZ3sGpJSf9rPLKPLg=s80-c)](/kun432)[kun432](/kun432)[5ヶ月前に更新](#comment-7d75b7bfcc9333)
> VSCodeのターミナル内で使うのが現実的には良さそうかなぁ、コードも見たいしね。devcontainerの設定とセットで用意しておくと良さそう。

とか考えてたら、コミットするかしないかが違うだけで、VSCode＋Github CopilotとかCursorで使うのと何も変わらないのではないか？とか思い出したんだけど、多分以下のような使い方が良いのかなと思った。

<https://aider.chat/examples/add-test.html>

* Aiderにコードを読ませてテストコードを書かせる
* Aiderのチャット内でテストコマンドを実行
* 上記のテストコマンドの出力を会話に追加
* 上記の出力を元にコードをAiderが修正

こういうのが多少なりともシームレスにできそうではある。VSCode＋Github CopilotとかCursorでこれができるのか、知らないんだけど。

返信[![kun432](https://lh3.googleusercontent.com/a-/AOh14Gj2-TWBIJGuFBxhPY_QFO7z0tZ3sGpJSf9rPLKPLg=s80-c)](/kun432)[kun432](/kun432)[4ヶ月前](#comment-b4a8a5baa9acc6)

ほぼゼロベースからCSVのデータだけ用意して、こういうStreamlit＋Plotlyのアプリぐらいは作れる。なお、gpt-4o-miniを使用。

![](https://storage.googleapis.com/zenn-user-upload/ad5e21358beb-20240814.png)

gpt-4o-miniでもたまにそうじゃない感のある修正してくることはある。あとollamaのいくつかのモデルでもやってみたけど、ぜんぜんダメだった。claude-3.5-sonnetあたり使えば、もっとサクサクできるのかなぁ？

返信このスクラップは5ヶ月前にクローズされました[ポスト](https://twitter.com/intent/tweet?url=https://zenn.dev/kun432/scraps/15a98cb5e8930b&text=%E3%82%BF%E3%83%BC%E3%83%9F%E3%83%8A%E3%83%AB%E3%81%A7AI%E3%81%A8%E3%83%9A%E3%82%A2%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%E3%81%8C%E3%81%A7%E3%81%8D%E3%82%8B%E3%80%8CAIder%E3%80%8D%E3%82%92%E8%A9%A6%E3%81%99&hashtags=zenn)[![kun432](https://lh3.googleusercontent.com/a-/AOh14Gj2-TWBIJGuFBxhPY_QFO7z0tZ3sGpJSf9rPLKPLg=s250-c)](/kun432)[kun432](/kun432)

フリーランスのインフラ系エンジニア。LLM関連でいろいろ試してみた内容とかその時思ったことを、メモ・覚書的に書いてます。特にdocument retrieval周辺技術とどのような実活用ができるかに興味があります。競馬が好き。

