# WordPressオリジナルテーマの作り方②（トップページ編）

今回は、WordPressオリジナルテーマの作り方【第2回】トップページ編となります。

WordPressオリジナルテーマの作り方は、当記事を含め以下の記事があります。

WordPressオリジナルテーマ制作の記事

* ファイルの準備
* **トップページ作成 ← 当記事**
* functions.phpからCSSやJavaScriptなどを読み込む
* 固定ページ作成
* ブログカード作成
* 記事一覧ページ作成
* パンくずリスト作成
* 個別記事ページ作成
* カテゴリーページ作成
* カスタム投稿作成
* 404ページ
* 検索フォーム・検索結果ページ
* 月別アーカイブページ
* カスタムフィールド

## WordPressオリジナルテーマ：トップページの作り方

トップページの作り方は以下の手順で進めます。

1. 『front-page.php』に『index.html』をコピペ
2. 『front-page.php』から共通するパーツを分割
3. 『header.php』を作成
4. 『footer.php』を作成
5. 『header.php』と『footer.php』を読み込む為のインクルードタグを追記
6. 画像を表示させる関数を追記
7. 『header.php』と『footer.php』に必須な関数を追記

簡単にまとまると、ベースとなる『index.html』を以下の3つに分けていきます。

* ヘッダー
* メインコンテンツ
* フッター

あとは、WordPress特有の関数を追記していきます。

### 『front-page.php』に『index.html』のコードをコピペ

まずはトップページのテンプレートとなる『front-page.php』に、準備しておいた静的ページである『index.html』の中身をまるごとコピペします。

『index.html』のファイルごとコピペして、ファイル名を『front-page.php』と拡張子ごと変えてしまっても構いません。

ここでちょっとややこしいのが、このthemesフォルダには『index.php』というファイルがあることです。

名前からイメージすると『index.html』の中身は『index.php』にコピペしたくなりますが、ここでは『index.php』の中身は空のままです。

『ここでは』というのは『index.php』をトップページとする場合もあるからですが、ここではトップページは『front-page.php』とします。

なので『index.html（左）』の中身をまるっと『front-page.php（右）』にコピペしたした状態がこちらになります。

**ポイント**
OGPなどのmetaタグは大量にあるので省略しています（All in One SEOなどのプラグインで設定する時はここには書きませんし）

ちなみに上記HTMLはこちらになります。

```html
<!DOCTYPE html>
<html lang="ja">
  <head>
    <meta charset="UTF-8" />
    <title>タイトル</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="format-detection" content="telephone=no" />
    <link href="style.css" rel="stylesheet" />
  </head>
  <body>
    <header>ヘッダー</header>
    <main>
      <h1>大見出し</h1>
      <section>
        <h2>コンセプト</h2>
        <div>
          <img src="画像パス" alt="" />
        </div>
        <p>文章が入ります</p>
      </section>
    </main>
    <footer>フッター</footer>
  </body>
</html>
```

### 『front-page.php』から共通するパーツ（ヘッダー、フッター）を分割

次からは1ページ物のLPではなく、**複数ページのサイト**をイメージしてください。

複数ページの場合、トップページ以外にお問い合わせ、会社概要、記事一覧ページなどあると思います。

ただこれらのページでも**ヘッダーやフッターは同じ場合が**多いと思います。

なので、**共通するパーツは切り取って専用のテンプレートを作成します。**

そうすることで修正する際には、その専用のテンプレートだけ修整すればOKです。

もし分割していなかったら、

1. トップページのヘッダーを修正
2. 会社概要のヘッダーを修正
3. お問い合わせのヘッダーを修正・・・

といった感じでページの数だけ同じ修正を繰り返すことになります。

Sassを使ったことがある人なら変数をイメージするといいかも知れません。

変数も元を変えれば全てを変更することが出来ますからね。

それでは説明が長くなりましたが、具体的にパーツを分けていきたいと思います。

順番に決まりはありませんが、以下の流れでやると分かりやすいと思います。

1. 『front-page.php』からヘッダー部分を切り取り『header.php』を作成
2. 切り取った箇所に『header.php』を読み込む為のインクルードタグを追記
3. 『front-page.php』からフッター部分を切り取り『footer.php』を作成
4. 切り取った箇所に『footer.php』を読み込む為のインクルードタグを追記
5. 画像を表示させる関数を追記
6. 『header.php』に必須な関数を追記
7. 『footer.php』に必須な関数を追記

まず元の『front-page.php』を確認します。

```html
<!DOCTYPE html>
<html lang="ja">
  <head>
    <meta charset="UTF-8" />
    <title>タイトル</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="format-detection" content="telephone=no" />
    <link href="style.css" rel="stylesheet" />
  </head>
  <body>
    <header>ヘッダー</header>
    <main>
      <h1>大見出し</h1>
      <section>
        <h2>コンセプト</h2>
        <div>
          <img src="画像パス" alt="" />
        </div>
        <p>文章が入ります</p>
      </section>
    </main>
    <footer>フッター</footer>
  </body>
</html>
```

### header.phpを作成

それではここから『header.php』となる部分を切り取ります。

すると『front-page.php』は以下のようなコードになります。

```html
    <main>
      <h1>大見出し</h1>
      <section>
        <h2>コンセプト</h2>
        <div>
          <img src="画像パス" alt="" />
        </div>
        <p>文章が入ります</p>
      </section>
    </main>
    <footer>フッター</footer>
  </body>
</html>
```

そして切り取った部分はそのまま『header.php』へコピーします。

こちらが『header.php』になります。

```html
<!DOCTYPE html>
<html lang="ja">
  <head>
    <meta charset="UTF-8" />
    <title>タイトル</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="format-detection" content="telephone=no" />
    <link href="style.css" rel="stylesheet" />
  </head>
  <body>
    <header>ヘッダー</header>
```

閉じタグが分かれてしまったりちょっと気持ち悪いかも知れませんが、これで大丈夫です。

### footer.phpを作成

そして次は『footer.php』となる部分を切り取ります。

これも『header.php』と考え方は同じです。

すると『front-page.php』は以下のようなコードになります。

```html
<main>
  <h1>大見出し</h1>
  <section>
    <h2>コンセプト</h2>
    <div>
      <img src="画像パス" alt="" />
    </div>
    <p>文章が入ります</p>
  </section>
</main>
```

そして切り取った部分はそのまま『footer.php』へコピーします。

こちらが『footer.php』になります。

```html
    <footer>フッターテキスト</footer>
  </body>
</html>
```

前回の記事でも書きましたが、それぞれ`<header>`から`</header>`や`<footer>`から`</footer>`ではありません。

### 『header.php』と『footer.php』を読み込む為のインクルードタグを追記

そしてこのヘッダーとフッターがなくなったところにそれぞれを読み込む為のインクルードタグを書きます。

『front-page.php』はこのようになります。

```php
<?php get_header(); ?>
<main>
  <h1>大見出し</h1>
  <section>
    <h2>コンセプト</h2>
    <div>
      <img src="画像パス" alt="" />
    </div>
    <p>文章が入ります</p>
  </section>
</main>
<?php get_footer(); ?>
```

`<?php get_header(); ?>`が『header.php』を読み込み、

`<?php get_footer(); ?>`が『footer.php』を読み込みます。

結果として切り取る前のコードと同じ内容となります。

もちろん書く場所を間違えると、変な所にヘッダーやフッターが表示されてしまうのでご注意ください。

あくまでも『**切り取った場所に置き換える**』というイメージです。

そしてこれと同じようなことを固定ページでもやりますが、それはまた次回以降説明したいと思います。

### 画像を表示させる関数を追記

そしてトップページを完成させるにはもう1つしなければいけないことがあり、このままでは画像が表示されません。

ちゃんと表示させるためには現在使っているテーマのディレクトリ（フォルダ）までの画像パスを出力させる必要があります。

こうする事でテスト環境から本番へURL変わっても正常に表示されるようになります。

それでは『front-page.php』を見てみます。

```php
<?php get_header(); ?>
<main>
  <h1>大見出し</h1>
  <section>
    <h2>コンセプト</h2>
    <div>
      <img src="<?php echo get_theme_file_uri( '画像パス' ); ?>" alt="" /> 
    </div>      
    <p>文章が入ります</p>
  </section>
</main>
<?php get_footer(); ?>
```

**imgタグの書き換え**

・変更前  
→ `<img src="画像パス" alt="" />`

・変更後  
→ `<img src="<?php echo get_theme_file_uri( '画像パス' ); ?>" alt="" />`

この`<?php echo get_theme_file_uri(); ?>`という関数が変更点になります。

ここで注意して欲しいのが`uri()`の中の 『' '（シングルクォーテーション）』もしくは『 " "（ダブルクォーテーション）』です。

どちらでも大丈夫ですが、これがないと画像が反映されません。

これで『front-page.php』は完了です・・・が、

『header.php』と『footer.php』であと1つずつ入れなければいけない関数があります。

### 『header.php』と『footer.php』に必須な関数を追記

これも決まり事のようなものなので深く考えずに入れて大丈夫ですが、これがないとプラグインが動かないなど不具合が発生する事があるようです。

実際にこれを入れずに不具合が起きたケースを何度か見たことがあります（人から相談されたときなど）

それではそれぞれのコードを見てみましょう。

まずは『header.php』から。

```html
<!DOCTYPE html>
<html lang="ja">
  <head>
    <meta charset="UTF-8" />
    <title>タイトル</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="format-detection" content="telephone=no" />
    <link href="style.css" rel="stylesheet" />
    <?php wp_head(); ?>
  </head>
  <body>
    <header>ヘッダー</header>
```

次は『footer.php』

```html
      <footer>フッター</footer>
    <?php wp_footer(); ?>
  </body>
</html>
```

『header.php』は`</head>`の直前に`<?php wp_head(); ?>`

『footer.php』は`</body>`の直前に`<?php wp_footer(); ?>`

を入れます。

これも書く場所は決まっているので間違えないようにしましょう。

あとは『header.php』ではCSSの読み込みなど出来るようにする関数を入れることも出来ますが、それは『functions.php』というテンプレートファイルを使ってやっていきます。

### headタグに関数追加

最後に、headタグ内に関数を追加します。

まず、こちらが現在のheader.phpになります。

```html
<!DOCTYPE html>
<html lang="ja">
  <head>
    <meta charset="UTF-8" />
    <title>タイトル</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="format-detection" content="telephone=no" />
    <link href="style.css" rel="stylesheet" />
  </head>
  <body>
    <header>ヘッダー</header>
```

これを、以下のようにします。

```html
<!DOCTYPE html>
<html <?php language_attributes(); ?>>
  <head>
    <meta charset="<?php bloginfo( 'charset' ); ?>" />
    <title>タイトル</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="format-detection" content="telephone=no" />
    <link href="style.css" rel="stylesheet" />
  </head>
  <body <?php body_class(); ?>><?php wp_body_open(); ?>
    <header>ヘッダー</header>
```

3ヶ所の追加した関数について、少し解説します。

#### <?php language_attributes(); ?>

これは`lang="ja"`の代わりに書く関数で、サイトの言語が日本語のままであれば書き換える必要はありません。

ただし、日本語以外にしたときに、自動で変更されるようにする為にはこの関数を書きます。

ちなみに、言語設定とは管理画面の設定から変更できる『**サイトの言語**』になります。

#### <?php bloginfo( 'charset' ); ?>

使われている文字コード（UTF-8）を表示するための関数です。

#### <body <?php body_class(); ?>><?php wp_body_open(); ?>

body開始タグ内に`<?php body_class(); ?>`

その直後に`<?php wp_body_open(); ?>`を書きます。

これを書くとbodyタグにページ固有のclass名がページごとに付与されます。

例えば固定ページの場合はページIDが含まれたclassが付与されます（他にも色々とclassが付与されます）

特定のページのみデザインを変えたり出来るので、カスタマイズ性がアップします（あまり使わないかも知れませんが）

## まとめ：ヘッダーとフッターは分けて作成！

これで、トップページは完成となります。

今回のヘッダーとフッターを分けて作成する、というのがWordPressのオリジナルテーマ制作の特徴になるので、少しずつ慣れていきましょう。

トップページに、

* 投稿新着一覧表示
* カスタム投稿新着一覧表示
* 上記新着一覧をPC、SPで表示件数変更

という実装も良くありますが、それについては別途解説いたします。