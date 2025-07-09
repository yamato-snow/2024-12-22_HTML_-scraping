# WordPressオリジナルテーマの作り方③（functions.php編）

今回は、**WordPressオリジナルテーマ**の作り方【第3回】functions.php編となります。

WordPressオリジナルテーマの作り方は、当記事を含め以下の記事があります。

WordPressオリジナルテーマ制作の記事

* **ファイルの準備**
* **トップページ作成**
* **functions.phpからCSSやJavaScriptなどを読み込む ← 当記事**
* **固定ページ作成**
* **ブログカード作成**
* **記事一覧ページ作成**
* **パンくずリスト作成**
* **個別記事ページ作成**
* **カテゴリーページ作成**
* **カスタム投稿作成**
* **404ページ**
* **検索フォーム・検索結果ページ**
* **月別アーカイブページ**
* **カスタムフィールド**

前回の記事で、トップページからヘッダーとフッターを分ける作業は完了しました。

今回は、『functions.php』というテーマファイルについて説明していきたいと思います。

## WordPressオリジナルテーマの作り方：functions.phpの書き方

『functions.php』とは各ページのコンテンツを表示させるものではなく、WordPress全体のプラグインのような働きをするものです。

例えば、オリジナルテーマは既存テーマには普通にある、アイキャッチの設定画面も表示されません。

そこでこの『functions.php』にアイキャッチを使えるようにする機能を追加していく、といった感じになります。

もちろん必要に応じてどんどんコードを追記していくので、この『functions.php』も**ほぼ必須ファイル**となります。

今回は、最低限書くべきことを書いていきます。

**注意ポイント**

『function.php』ではなく『functions.php』なのでご注意下さい（sを忘れずに）

### 基本設定

まずは、`add_theme_support()`という関数を使って、テーマの基本設定を行います。

```php
<?php
  function my_setup(){
    add_theme_support('post-thumbnails'); // アイキャッチ画像を有効化
    add_theme_support('automatic-feed-links'); // 投稿とコメントのRSSフィードのリンクを有効化
    add_theme_support('title-tag'); // titleタグ自動生成
    add_theme_support('html5', array( // HTML5による出力
      'search-form',
      'comment-form',
      'comment-list',
      'gallery',
      'caption',
    ));
  }
  add_action('after_setup_theme', 'my_setup');
```

これを『functions.php』にコピペすればOKです。

特にアイキャッチは普通にあると思ってる方が多いと思いますが、ここで設定しないと表示されないので忘れずに設定しておきましょう。

### CSSやJavaScriptを読み込む

**CSS**や**JavaScript**は『header.php』の『headタグ』から読み込むことも出来ますが・・・

一般的にはこの『functions.php』から読み込みます（Wordpressが推奨しています）

それではその『functions.php』でCSSやJavaScriptを読み込むコードを書いていきます。

```php
<?php
/* CSSとJavaScriptの読み込み */
function my_script_init()
  { // WordPressに含まれているjquery.jsを読み込まない
    wp_deregister_script('jquery');
    // jQueryの読み込み
    wp_enqueue_script( 'jquery', '//code.jquery.com/jquery-3.6.1.min.js', "", "1.0.1", true);
    wp_enqueue_script( 'main-js', get_template_directory_uri() . '/js/main.js', array( 'jquery' ), '1.0.1', true );
    wp_enqueue_style( 'style-css', get_template_directory_uri() . '/css/style.css', array(), '1.0.1' );
  }
  add_action('wp_enqueue_scripts', 'my_script_init');
```

これでOKです。少し解説します。

* `wp_enqueue_script`が、JavaScriptを読み込む関数（7～8行目）
* `wp_enqueue_style`が、CSSを読み込む関数（9行目）

になります。

* 7行目はjQuery本体
* 8行目は自作したjsファイル
* 9行目は自作したcssファイル

なので、自作したファイルのファイル名やファイルまでのパスは、ご自身の環境に合わせて変更して下さい。

`get_template_directory_uri()`は、前回画像を表示させるために書いた関数と同じ、テーマのディレクトリ（フォルダ）までのパスを出力させるものです。

上記のコードは『functions.php』とcssやjsフォルダが同じ階層にある場合なので、もし階層が違っていたらご自身の環境に合わせて下さい（同じ階層にあるというのはこのような状態です）

これで『functions.php』からCSSやJavaScriptを読み込むことが出来たので、**前回の記事**で作成した『header.php』からCSSを読み込む一行は削除しましょう。

『header.php』はこうなります。

```html
<!DOCTYPE html>
<html <?php language_attributes(); ?>>
<head>
    <meta charset="<?php bloginfo( 'charset' ); ?>" />
    <title>タイトル</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="format-detection" content="telephone=no" />
    <link href="style.css" rel="stylesheet" /><!-- この行を削除 -->
  </head>
  <body <?php body_class(); ?>><?php wp_body_open(); ?>
    <header>ヘッダー</header>
```

8行目を削除ですね。

同じように『footer.php』の</body>タグ直前にあると思われるjsの読み込み部分も削除します（前回の記事にはありません）

あといくつか注意点があります。

#### WordPressに含まれているjquery.jsを読み込まない

通常、静的サイトで**jQuery**を使用するにはjQuery本体を読み込む必要があります。

ただWordPressにはjQueryが標準で用意されているので、本体を読み込む必要はありません。

しかしWordPressが用意しているjQueryは標準のjQueryとは書き方が少し異なるので、ここでは5行目でWordPressが用意しているjQueryの読み込みをキャンセルし、7行目で自分が使いたいjQueryを読み込んでいます。

#### 第一引数の名前は重複させない

この第一引数というのは以下の『'script-name'』や『'lightbox'』の部分になります。

ここの名前は自由に決めていいのですが、CSS同士、js同士で同じ名前を付けると動かなくなります。

```php
<?php
/* CSSとJavaScriptの読み込み */
function my_script_init()
{
wp_enqueue_style('lightbox', get_theme_file_uri('/css/lightbox.css'), array(), '1.0.1');
wp_enqueue_script('script-name', get_theme_file_uri('/js/main.js'), array( 'jquery' ), '1.0.1', true);
wp_enqueue_script('lightbox', get_theme_file_uri('/js/lightbox.js'), array( 'jquery' ), '1.0.1', true);
wp_enqueue_script('script-name', get_theme_file_uri('/js/access.js'), array( 'jquery' ), '1.0.1', true);
}
add_action('wp_enqueue_scripts', 'my_script_init');
```

上の例では『wp_enqueue_script』の第一引数で『script-name』が2つあるので**NG**となります（6行目と8行目）

また『lightbox』も2つありますが、これは『wp_enqueue_script』と『wp_enqueue_style』なので**OK**です。

以前これでかなりハマったことがあるのでご注意下さい。

そして上記のコードから分かる通り、ファイルの種類が増えれば追記していくことが可能です。

また最後にあるtrueですが、

* false → </head>の前に書かれる
* true → </body>の前に書かれる

という違いになります（デフォルトはfalse）

#### 全角スペースを入れない

これがあると誰もが恐れる

**画面真っ白**

という状態になりかねません。

もし画面が真っ白になったら、functions.phpに全角スペースがないか確認してみましょう。

## まとめ：functions.phpはプラグインの様に機能を追加するもの

この『functions.php』には案件によっていろいろ追記していく事になると思うので、慣れておきましょう。