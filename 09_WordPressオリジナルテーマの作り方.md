# WordPressオリジナルテーマの作り方⑨（カテゴリーページ編）

今回は、WordPressオリジナルテーマの作り方【第9回】カテゴリーページ編となります。

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
* **カテゴリーページ作成 ← 当記事**
* **カスタム投稿作成**
* **404ページ**
* **検索フォーム・検索結果ページ**
* **月別アーカイブページ**
* **カスタムフィールド**

今回は、カテゴリーページについて書いていきたいと思います。

まずこちらを見て下さい。

パンくずリストの例

これは個別記事ページのパンくずリストです。

記事のタイトルの前にカテゴリーである『チワワ』と書いてあり、これはカテゴリー名となります。

つまり、このようになります。

* ホーム：トップページ
* ブログ：ページ名
* チワワ：カテゴリー名
* 愛犬撮影会（チワワ）：記事タイトル

今回は、このカテゴリー名をクリックすると表示される『カテゴリー一覧ページ』を作っていきます。

他の投稿系ページとの違いは、

* 記事一覧ページ → 全てのカテゴリーを一覧表示
* 個別記事ページ → 1つの記事を表示
* カテゴリーページ → **特定のカテゴリーのみ一覧表示**

となります。

## WordPressオリジナルテーマ：カテゴリーページの作り方

今回は『category.php』というテンプレートを使います。

ここで書く内容は今までの記事を読んで頂いていれば何となく分かると思いますが、

* header.phpを読み込む
* パンくずリストを表示（必要に応じて）
* メインコンテンツ（今回はブログカード）
* ページネーション
* footer.phpを読み込む

となります。

なので記事一覧ページの『home.php』と見た目は基本的に同じデザインが多いですが、ループ処理の書き方など微妙に違いはあります（メインコンテンツは同じ）

### category.phpを作成

基本的には『home.php』と中身の同じですが、まずはページタイトルをカテゴリー名にしてみましょう。

例えば記事一覧ページ（home.php）のページタイトルが『ブログ』だったとします。

```html
<h1>ブログ</h1>
```

これをカテゴリーページ（category.php）の時にはこのようにします。

```php
<h1>
  <?php $cat_info = get_category( $cat );?>
  <?php echo wp_specialchars( $cat_info->name ); ?>
</h1>
```

こうする事によって、ページタイトルはカテゴリー名になります。

例えばカテゴリー名が『スタッフ日記』であれば以下のようになります。

```html
<h1>スタッフ日記</h1>
```

全体のコードはこちらになります。

```php
<?php get_header(); ?>
<main class="main">
  <article class="">
    <!-- カテゴリー名出力 -->
    <h1>
      <?php $cat_info = get_category( $cat );?>
      <?php echo wp_specialchars( $cat_info->name ); ?>
    </h1>
    <ul class="">
      <!-- 記事のループ処理開始 -->
      <?php
        $cat_info = get_category( get_query_var( 'cat' ) );
        $paged = get_query_var('paged') ? get_query_var('paged') : 1;
      ?>
      <?php
      if( wp_is_mobile() ){
          $num = 4; // スマホの表示数(全件は-1)
        } else {
          $num = 8; // PCの表示数(全件は-1)
        }
        $args = array(
          'post_type' => array('post'), // 投稿タイプのスラッグ(通常投稿なので'post')
          'paged' => $paged, // ページネーションがある場合に必要
          'posts_per_page' => $num, // 表示件数（変更不要）
          'category_name' => $cat_info->slug,
        );
        $wp_query = new WP_Query($args);
        if ( $wp_query->have_posts() ) : while ( $wp_query->have_posts() ) :
          $wp_query->the_post();
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
      <?php
        endwhile;
        endif;
        wp_reset_postdata();
      ?>
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

いろいろと書いてあって難しく見えるかも知れませんが、空欄のclass名やレイアウト以外で書き換えられる箇所は以下になります。

* スマホ・PCの表示件数
* ページネーションの『前へ・次へ』のテキスト

もしページネーションが上手く表示されない場合はこちらで試してみて下さい。

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

## まとめ

今回の内容ですが、以下のような設定も可能です。

* カテゴリーを全部表示（先ほどは1件のみ表示）
* ページネーション番号あり（前後を画像）
* ページネーション前後のみ（テキストか画像）

また、カテゴリーを以下のようにタブメニューで作成することも出来ます。

カテゴリー一覧タブメニュー

『すべて』は記事一覧ページなのでクリックすると『home.php』へ遷移、『すべて』以外はカテゴリーページなのでクリックすると『category.php』に遷移となります。