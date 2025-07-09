# WordPressオリジナルテーマの作り方⑥（記事一覧ページ編）

今回は、**WordPressオリジナルテーマ**の作り方【第6回】記事一覧ページ編となります。

WordPressオリジナルテーマの作り方は、当記事を含め以下の記事があります。

WordPressオリジナルテーマ制作の記事

* **ファイルの準備**
* **トップページ作成**
* **functions.phpからCSSやJavaScriptなどを読み込む**
* **固定ページ作成**
* **ブログカード作成**
* **記事一覧ページ作成 ← 当記事**
* **パンくずリスト作成**
* **個別記事ページ作成**
* **カテゴリーページ作成**
* **カスタム投稿作成**
* **404ページ**
* **検索フォーム・検索結果ページ**
* **月別アーカイブページ**
* **カスタムフィールド**

今回は、記事一覧ページについて書いていきたいと思います。

## WordPressオリジナルテーマ：記事一覧ページの作り方

まずは、テンプレートファイルを作成します。

今回は、**WordPressオリジナルテーマの作り方①（ファイルの準備編）**で作成した、『home.php』を使っていきます。

また、固定ページにブログ一覧用のページを作る必要があります。

それではコードを書いていきます。

### 記事を取得するためのループを書く

まず、基本となる『header.php』と『footer.php』を読み込む為のインクルードタグを書きます。

ここは、**トップページの作り方**と同じですね。

これは 、`<?php get_header(); ?>`と`<?php get_footer(); ?>`が追記されている以外は、前回の**ブログカード編**の中身と基本的には同じです（もちろん案件によって中身は異なります）

```php
<?php get_header(); ?>
<main class="main">
  <article class="">
    <ul class="">
      <li class="">
        <!-- 記事へのリンク -->
        <a href="<?php the_permalink(); ?>" class="">
          <!-- アイキャッチ -->
          <div class="">
            <?php the_post_thumbnail('post-thumbnail', array('alt' => the_title_attribute('echo=0'))); ?>
          </div>
          <p class="">
            <!-- 投稿日 -->
            <time datetime="<?php the_time('Y.n.j'); ?>">
              <?php the_time('Y.m.d'); ?>
            </time>
          </p>
          <div class="">
            <!-- カテゴリー1件表示(カテゴリー順の上にある方が表示される) -->
            <?php
              $category = get_the_category();
              echo '<span class="'.$category->slug.'">'.$category[0]->name.'</span>';
            ?>
          </div>
          <h2 class="">
            <!-- タイトル -->
            <?php the_title(); ?>
          </h2>
          <div class="">
            <!-- 本文の抜粋 -->
            <?php the_excerpt(); ?>
          </div>
        </a>
      </li>
    </ul>
  </article>
</main>
<?php get_footer(); ?>
```

ここに、繰り返し処理であるループの記述するとこうなります。

```php
<?php get_header(); ?>
<main class="main">
  <article class="">
    <ul class="">
      <!-- 記事のループ処理開始 -->
      <?php
        if( wp_is_mobile() ){
          $num = 3; // スマホの表示数(全件は-1)
        } else {
          $num = 5; // PCの表示数(全件は-1)
        }
        $paged = get_query_var('paged') ? get_query_var('paged') : 1;
        $args = [
          'post_type' => 'post', // 投稿タイプのスラッグ(通常投稿なので'post')
          'paged' => $paged, // ページネーションがある場合に必要
          'posts_per_page' => $num, // 表示件数
        ];
        $wp_query = new WP_Query($args);
        if (have_posts()): while (have_posts()): the_post();
      ?>
      <li class="">
        <!-- 記事へのリンク -->
        <a href="<?php the_permalink(); ?>" class="">
          <!-- アイキャッチ -->
          <div class="">
            <?php the_post_thumbnail('post-thumbnail', array('alt' => the_title_attribute('echo=0'))); ?>
          </div>
          <p class="">
            <!-- 投稿日 -->
            <time datetime="<?php the_time('Y.n.j'); ?>">
              <?php the_time('Y.m.d'); ?>
            </time>
          </p>
          <div class="">
            <!-- カテゴリー1件表示(カテゴリー順の上にある方が表示される) -->
            <?php
              $category = get_the_category();
              echo '<span class="'.$category->slug.'">'.$category[0]->name.'</span>';
            ?>
          </div>
          <h2 class="">
            <!-- タイトル -->
            <?php the_title(); ?>
          </h2>
          <div class="">
            <!-- 本文の抜粋 -->
            <?php the_excerpt(); ?>
          </div>
        </a>
      </li>
      <?php endwhile; else: ?>
      <p>まだ記事がありません</p>
      <?php endif ?>
      <?php wp_reset_postdata(); ?>
      <!-- 記事のループ処理終了 -->
    </ul>
  </article>
</main>
<?php get_footer(); ?>
```

いろいろ書いてありますが、変更可能な箇所は『スマホ・PCの表示件数』だけです。

### ページネーションを設置

次は、ページ送りするページネーションを設置します。

```php
<?php
  the_posts_pagination( array( 
    'mid_size' => 1,
    'prev_text' => '前へ', 
    'next_text' => '次へ' 
  ) );
?>
```

これは、上記コードで言えば</ul>の直後に書きます。

この 『前へ』や『次へ』のテキストは、自由に変えられます。

ページネーションについては細かく書くと大変なので、ここのページネーションは一例と思って下さい。

もし、ページネーションが上手く表示されない場合は、こちらで試してみて下さい。

```php
<?php
  global $wp_query;
  $big = 9999999999;
  $arg = array(
    'base' => str_replace( $big, '%#%', esc_url( get_pagenum_link( $big ) ) ),
    'current' => max( 1, get_query_var('paged') ),
    'total'   => $wp_query->max_num_pages,
    'mid_size' => 1,
    'prev_text' => '前へ',
    'next_text' => '次へ',
  );
  echo paginate_links($arg);
?>
```

それでは、最後に全体を見てみます。

```php
<?php get_header(); ?>
<main class="main">
  <article class="">
    <ul class="">
      <!-- 記事のループ処理開始 -->
      <?php
        if( wp_is_mobile() ){
          $num = 3; // スマホの表示数(全件は-1)
        } else {
          $num = 5; // PCの表示数(全件は-1)
        }
        $paged = get_query_var('paged') ? get_query_var('paged') : 1;
        $args = [
          'post_type' => 'post', // 投稿タイプのスラッグ(通常投稿なので'post')
          'paged' => $paged, // ページネーションがある場合に必要
          'posts_per_page' => $num, // 表示件数
        ];
        $wp_query = new WP_Query($args);
        if (have_posts()): while (have_posts()): the_post();
      ?>
      <li class="">
        <!-- 記事へのリンク -->
        <a href="<?php the_permalink(); ?>" class="">
          <!-- アイキャッチ -->
          <div class="">
            <?php the_post_thumbnail('post-thumbnail', array('alt' => the_title_attribute('echo=0'))); ?>
          </div>
          <p class="">
            <!-- 投稿日 -->
            <time datetime="<?php the_time('Y.n.j'); ?>">
              <?php the_time('Y.m.d'); ?>
            </time>
          </p>
          <div class="">
            <!-- カテゴリー1件表示(カテゴリー順の上にある方が表示される) -->
            <?php
              $category = get_the_category();
              echo '<span class="'.$category->slug.'">'.$category[0]->name.'</span>';
            ?>
          </div>
          <h2 class="">
            <!-- タイトル -->
            <?php the_title(); ?>
          </h2>
          <div class="">
            <!-- 本文の抜粋 -->
            <?php the_excerpt(); ?>
          </div>
        </a>
      </li>
      <?php endwhile; else: ?>
      <p>まだ記事がありません</p>
      <?php endif ?>
      <?php wp_reset_postdata(); ?>
      <!-- 記事のループ処理終了 -->
    </ul>
    <!-- ページネーション -->
    <div class="">
      <?php
        the_posts_pagination( array( 
          'mid_size' => 1,
          'prev_text' => '前へ', 
          'next_text' => '次へ' 
        ) );
      ?>
    </div>
  </article>
</main>
<?php get_footer(); ?>
```

以上になります。

## まとめ

今回の内容ですが、以下のような設定も可能です。

* カテゴリーを全部表示
* ページネーション番号あり（前後を画像）
* ページネーション前後のみ（テキストか画像）

また、カテゴリーを以下のようにタブメニューで作成することも出来ます。

『すべて』は記事一覧ページなので、クリックすると『home.php』へ遷移、『すべて』以外はカテゴリーページなのでクリックすると『category.php』に遷移となります。

つまり、『すべて』で表示しているページを『home.php』にすることも可能です。