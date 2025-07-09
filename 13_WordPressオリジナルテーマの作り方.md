# WordPressオリジナルテーマの作り方⑬（月別アーカイブページ編）

今回は、**WordPressオリジナルテーマ**の作り方【第13回】月別アーカイブページ編となります。

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
* **検索フォーム・検索結果ページ**
* **月別アーカイブページ ← 当記事**
* **カスタムフィールド**

ブログではサイドバーによくある、こういうやつですね。

今回は、このリストを表示する方法と、そこから遷移する月別アーカイブページの作り方を解説していきます。

## WordPressオリジナルテーマ：月別アーカイブページ編

冒頭でも書いた通り、今回は大きく分けて2つのことを解説していきます。

1. 月別アーカイブリストを表示する方法
2. 月別アーカイブページを作る方法（date.phpを使用）

それでは順番に解説してきます。

### 月別アーカイブリストを表示する方法

これは表示させたい箇所にこれから紹介するコードを貼ればOKですが、方法はいくつかあります。

#### 月別アーカイブリスト

```html
<ul class="monthly-list">
  <?php wp_get_archives( 'post_type=post&type=monthly&show_post_count=1' ); ?>
</ul>
```

#### 月別アーカイブリスト（ドロップダウン）

```html
<select name="archive-dropdown" onchange="document.location.href=this.options[this.selectedIndex].value;">
  <option disabled selected value>アーカイブ</option>
  <?php wp_get_archives( 'type=monthly&format=option&post_type=post&show_post_count=1' ); ?>
</select>
```

#### 年別アーカイブ

月別ではなく年別にしたい場合は、`monthly`を`yearly`にすればOK。

#### 記事数を非表示

記事数を表示させたくない場合は、`show_post_count=1`を`show_post_count=0`にすればOKです。

### 月別アーカイブページを作成（date.php）

月別アーカイブページに使用するのは、『date.php』というテンプレートになります。

そしてこちらのコードを書きます（全体を囲むmainタグやarticleタグなどは適宜追記して下さい）

```php
<?php get_header(); ?>
<h1>
  月別アーカイブ
</h1>
<ul>
  <?php if(have_posts()): while(have_posts()): the_post(); ?>
  <li>
    <a href="<?php the_permalink(); ?>">
      <time datetime="<?php the_time('Y-m-d'); ?>">
        <?php the_time('Y年m月d日'); ?>
      </time>
      <?php the_title(); ?>
    </a>
  </li>
  <?php endwhile; ?>
  <?php wp_reset_postdata(); ?>
  <?php endif; ?>
</ul>
<?php
  the_posts_pagination( array( 
    'mid_size' => 1,
    'prev_text' => '', 
    'next_text' => '' 
  ) );
?>
<?php get_footer(); ?>
```

#### 表示件数を変更

表示件数は特に指定しない場合、管理画面の『設定 → 表示設定 → 1ページに表示する最大投稿数』になります。

そこで、以下のコードを『functions.php』に追記すれば件数を変更できます。

```php
function my_pre_get_posts( $query ) {
  if ( is_admin() || !$query->is_main_query() ) {
    return;
  }
  if ( $query->is_date() ) {
    $query->set( 'posts_per_page', 10 );
  }
}
add_action('pre_get_posts','my_pre_get_posts');
```

これは10件表示の場合になります。

## まとめ

今回は、月別アーカイブページを作る方法を解説しました。

あまり実装する機会はないかも知れませんが、作れるようになっておきましょう。

以上になります。