# WordPressオリジナルテーマの作り方⑫（検索フォーム・検索結果ページ編）

今回は、**WordPressオリジナルテーマ**の作り方【第12回】検索フォーム・検索結果ページ編となります。

WordPressオリジナルテーマの作り方は、当記事を含め以下の記事があります。

WordPressオリジナルテーマ制作の記事

* **ファイルの準備**
* **トップページ作成**
* **functions.phpからCSSやJavaScriptなどを読み込む**
* **固定ページ作成**
* **ブログカード作成**
* **記事一覧ページ作成**
* **パンくずリスト作成**
* **個別記事ページ作成**
* **カテゴリーページ作成**
* **カスタム投稿作成**
* **404ページ**
* **検索フォーム・検索結果ページ ← 当記事**
* **月別アーカイブページ**
* **カスタムフィールド**

今回解説する『検索フォーム・検索結果ページ』は、テンプレートを2つ作ります。

個人的にはあまり実装したことは無いのですが、必要となる時は来ると思うので覚えておきましょう。

## WordPressオリジナルテーマ：検索フォーム・検索結果ページ編

今回解説する内容はこちらになります。

* 検索フォームのテンプレートを作成（searchform.php）
* 検索結果ページのテンプレートを作成（search.php）
* 検索対象のページタイプを指定（functions.php）
* キーワードとカテゴリーで検索する方法
* WP Multibyte Patchをインストール

それでは1つずつ解説していきます。

### 検索フォームのテンプレートを作成（**searchform.php**）

これは『キーワード入力欄』と『検索ボタン』になります。

使用するテンプレートは『searchform.php』となり、以下のコードを書きます。

```html
<form method="get" action="<?php echo esc_url(home_url('/')); ?>">
  <input type="text" name="s" id="s" placeholder="キーワードを入力" />
  <button type="submit">検索する</button>
</form>
```

『キーワードを入力』と『検索する』の文字は変更可能です。

また、検索フォームについてはテンプレートを作らずに直接表示させたいテンプレートに書いても大丈夫ですが、複数のテンプレートに設置したい場合は『header.php』や『footer.php』のように共通パーツとした方が使いやすいです。

#### 検索フォームの設置

先ほど作成した『searchform.php』を呼び出すには、以下のコードを設置したいテンプレートの表示させたい箇所に書けばOKです。

```php
<?php get_search_form(); ?>
```

### 検索結果ページのテンプレートを作成（**search.php**）

これは検索結果一覧ページとなるので、デザインとしては通常の記事一覧ページと同じかと思います。

こちらのコードを『search.php』に書きます（全体を囲むmainタグやarticleタグなどは適宜追記して下さい）

```php
<?php get_header(); ?>
<?php if (isset($_GET['s']) && empty($_GET['s'])) { ?>
<p>検索条件が入力されていません。</p>
<?php } else { ?>
<h1>
  <?php the_search_query(); ?>の検索結果 : <?php echo $wp_query->found_posts; ?>件
</h1>
<ul>
  <?php if(have_posts()): ?>
  <?php while(have_posts()): the_post(); ?>
  <li>
    <a href="<?php the_permalink(); ?>">
      <h2><?php the_title(); ?></h2>
    </a>
    <?php endwhile; ?>
    <?php else : ?>
    <p>検索条件に一致する記事がありませんでした。</p>
    <?php endif; ?>
  </li>
  <?php
    the_posts_pagination( array( 
      'mid_size' => 1,
      'prev_text' => '', 
      'next_text' => '' 
    ) );
  ?>
  <?php } ?>
</ul>
<?php get_footer(); ?>
```

ここでは、シンプルに投稿（ページ）のタイトルしか表示していません。

#### 検索条件が未入力時には検索結果は表示しない

何も設定しないと、キーワードが未入力で検索すると全件表示されてしまいます。

これを避けるためには、『functions.php』に以下のコードを追記します。

```php
// 検索条件が未入力時にsearch.phpにリダイレクトする
function set_redirect_template(){
  if (isset($_GET['s']) && empty($_GET['s'])) {
    include(TEMPLATEPATH . '/search.php');
    exit;
  }
}
add_action('template_redirect', 'set_redirect_template');
```

テンプレート側の記述は、先ほどのコードで大丈夫です。

#### 検索結果の表示件数を変更

検索結果の表示件数は特に指定しない場合、管理画面の『設定 → 表示設定 → 1ページに表示する最大投稿数』になります。

これを変更したい場合は、『search.php』に以下のコードを書けばOKです（先ほどの例では2行目あたりに書けばOK）

```php
<?php query_posts($query_string.'&posts_per_page=10'); ?>
```

この場合は10件になります。

ただし、`query_posts`の使用は推奨されていないので、代わりに以下のコードを『functions.php』に追記する方法もあります。

```php
function my_pre_get_posts( $query ) {
  if ( is_admin() || !$query->is_main_query() ) {
    return;
  }
  if ( $query->is_search() ) {
    $query->set( 'posts_per_page', 10 );
  }
}
add_action('pre_get_posts','my_pre_get_posts');
```

これも10件表示の場合になります。

### 検索対象のページタイプを指定

検索対象のページタイプは特に指定しない場合、『通常の投稿』や『カスタム投稿』『固定ページ』など全てになります。

しかし、検索対象になるのは基本的に投稿ページで、固定ページは対象外にしたい場合があると思います。

その場合は、『functions.php』にコードを追記すればOKです。

#### 通常投稿のみ（カスタム投稿、固定ページは除外）

```php
// 検索条件のページタイプを指定する(通常投稿のみ)
function SearchFilter( $query ) {
  if ( $query -> is_search ) {
    $query -> set( 'post_type', 'post' );
  }
  return $query;
}
add_filter( 'pre_get_posts', 'SearchFilter' );
```

#### 通常投稿、カスタム投稿（固定ページは除外）

通常投稿と、カスタム投稿タイプが『news』のカスタム投稿のみの場合。

```php
// 検索条件のページタイプを指定する(通常投稿とカスタム投稿)
function SearchFilter( $query ) {
  if ( $query -> is_search ) {
    $query -> set( 'post_type', array('post','news') );
  }
  return $query;
}
add_filter( 'pre_get_posts', 'SearchFilter' );
```

固定ページの場合は『page』となります。

### キーワードとカテゴリーで検索する方法

これまではキーワードのみで検索していましたが、『キーワード』と『カテゴリー』の複合条件で検索することも可能です。

カテゴリーを選択するドロップダウンメニューを入れるには、『searchform.php』で以下のように書きます。

```php
<form method="get" action="<?php echo esc_url(home_url('/')); ?>">
  <input type="text" name="s" id="s" placeholder="キーワードを入力" />
  <div>カテゴリー選択：
    <?php
      wp_dropdown_categories( array(
        'orderby'            => 'name',
        'show_option_all'    => 'すべてのカテゴリー',
      ) );
    ?>
  </div>
  <button type="submit">検索する</button>
</form> 
```

もしカテゴリー選択を『すべてのカテゴリー』にしてキーワードだけ入力して検索した場合、通常投稿もカスタム投稿も全て対象となりますが、これで選択できるのは『通常投稿のカテゴリー』になるので、検索結果に表示されるのも『通常投稿のみ』となります。

カスタム投稿のカテゴリー（ターム）にしたい場合は、以下のようにします。

```php
<form method="get" action="<?php echo esc_url(home_url('/')); ?>">
  <input type="text" name="s" id="s" placeholder="キーワードを入力" />
  <div>カテゴリー選択：
    <?php
      wp_dropdown_categories( array(
        'orderby'            => 'name',
        'show_option_all'    => 'すべてのカテゴリー',
        'taxonomy'           => 'タクソノミースラッグ',
        'name'               => 'タクソノミースラッグ',
        'value_field'        => 'slug',
      ) );
    ?>
  </div>
  <button type="submit">検索する</button>
</form>
```

これは逆に通常投稿のカテゴリーは表示されないので、カテゴリー（ターム）を選択したら『カスタム投稿のみ』表示されます。

#### タクソノミースラッグの確認

プラグイン『Custom Post Type UI』を使った場合ですが、『CPT UI → タクソノミーの追加と編集』をクリックします。

そして『タクソノミーを編集 → タクソノミーを選択 → タクソノミースラッグ』で確認できます。

## WP Multibyte Patchをインストール

検索フォームにキーワードを複数入力する時にスペースを入れると思いますが、**全角スペースを入れると上手く検索されない場合があります。**

これを回避するには、**WP Multibyte Patchというプラグイン**をインストールすれば解決します。

## まとめ

今回は、検索フォームと検索結果ページの作り方を解説してきました。

これは最後にテストをして、ちゃんとイメージ通りになるか確認しましょう。

以上になります。