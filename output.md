

1. [HOME](https://junpei-sugiyama.com)  >
2. [WordPress](https://junpei-sugiyama.com/category/wordpress/)  >
3. [オリジナルテーマ](https://junpei-sugiyama.com/category/wordpress/original-theme/)  >

[オリジナルテーマ](https://junpei-sugiyama.com/category/wordpress/original-theme/ "View all posts in オリジナルテーマ") [WordPress](https://junpei-sugiyama.com/category/wordpress/ "View all posts in WordPress")

WordPressオリジナルテーマの作り方⑬（月別アーカイブページ編）
===================================

 2022年10月22日 2024年9月28日 

※ 当サイトではアフィリエイト広告を利用しています

* Twitter
* [Pinterest](https://www.pinterest.com/pin/create/button/?url=https%3A%2F%2Fjunpei-sugiyama.com%2Fwordpress-original-theme-13%2F&media=https://junpei-sugiyama.com/wp-content/uploads/2022/10/wordpress-original-theme-13-eye-catch.jpg&description=WordPressのオリジナルテーマの作り方を解説していくシリーズ。今回は月別アーカイブページの作り方です。)
* [LINE](//line.me/R/msg/text/?WordPress%E3%82%AA%E3%83%AA%E3%82%B8%E3%83%8A%E3%83%AB%E3%83%86%E3%83%BC%E3%83%9E%E3%81%AE%E4%BD%9C%E3%82%8A%E6%96%B9%E2%91%AC%EF%BC%88%E6%9C%88%E5%88%A5%E3%82%A2%E3%83%BC%E3%82%AB%E3%82%A4%E3%83%96%E3%83%9A%E3%83%BC%E3%82%B8%E7%B7%A8%EF%BC%89%0Ahttps%3A%2F%2Fjunpei-sugiyama.com%2Fwordpress-original-theme-13%2F)

今回は、**[WordPressオリジナルテーマ](https://junpei-sugiyama.com/what-is-wordpress-original-theme/)**の作り方【第13回】月別アーカイブページ編となります。

WordPressオリジナルテーマの作り方は、当記事を含め以下の記事があります。

WordPressオリジナルテーマ制作の記事

* **[ファイルの準備](https://junpei-sugiyama.com/wordpress-original-theme-1/)**
* **[トップページ作成](https://junpei-sugiyama.com/wordpress-original-theme-2/)**
* **[functions.phpからCSSやJavaScriptなどを読み込む](https://junpei-sugiyama.com/wordpress-original-theme-3/)**
* **[固定ページ作成](https://junpei-sugiyama.com/wordpress-original-theme-4/)**
* **[ブログカード作成](https://junpei-sugiyama.com/wordpress-original-theme-5/)**
* **[記事一覧ページ作成](https://junpei-sugiyama.com/wordpress-original-theme-6/)**
* **[パンくずリスト作成](https://junpei-sugiyama.com/wordpress-original-theme-7/)**
* **[個別記事ページ作成](https://junpei-sugiyama.com/wordpress-original-theme-8/)**
* **[カテゴリーページ作成](https://junpei-sugiyama.com/wordpress-original-theme-9/)**
* **[カスタム投稿作成](https://junpei-sugiyama.com/wordpress-original-theme-10/)**
* **[404ページ](https://junpei-sugiyama.com/wordpress-original-theme-11/)**
* **[検索フォーム・検索結果ページ](https://junpei-sugiyama.com/wordpress-original-theme-12/)**
* **月別アーカイブページ ← 当記事**
* **[カスタムフィールド](https://junpei-sugiyama.com/custom-field-suite/)**

ブログではサイドバーによくある、こういうやつですね。

![月別アーカイブ](https://junpei-sugiyama.com/wp-content/uploads/2022/10/wordpress-original-theme-13-01.jpg)![月別アーカイブ](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20400%20360%22%3E%3C/svg%3E)

月別アーカイブ

今回は、このリストを表示する方法と、そこから遷移する月別アーカイブページの作り方を解説していきます。

また、記事の最後には**[WordPressのおすすめ教材](https://junpei-sugiyama.com/web-production-teaching-materials/)**をご紹介させて頂きます。

![](https://junpei-sugiyama.com/wp-content/uploads/2021/07/Joy-1024x1024.png)![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%2060%2040%22%3E%3C/svg%3E)じゅんぺいブログは、Web制作（コーディング・WordPress制作）の技術記事を中心に、**約500記事**公開しています。ぜひ他の記事も参考にしてみてください！完全無料のプログラミングスクール『ZeroPlus Gate』30日間でWeb制作を学べる無料のプログラミングスクールがこちら[![](//image.moshimo.com/af-img/1998/000000058972.jpg)](//af.moshimo.com/af/c/click?a_id=4187964&p_id=4131&pc_id=10468&pl_id=58972)![](//i.moshimo.com/af/i/impression?a_id=4187964&p_id=4131&pc_id=10468&pl_id=58972)![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%201%201%22%3E%3C/svg%3E)いきなり数十万するプログラミングスクールは厳しい・・・という人のお試しに最適です。現在は無料ですがいつ有料になるか分からないので、気になる方はお早めに👇  
 （有料になっていたらすいません🙇‍♂️）

＼ 完全無料 ／

[ZeroPlus Gate公式サイト](//af.moshimo.com/af/c/click?a_id=4187964&p_id=4131&pc_id=10468&pl_id=56580)

毎日先着制！

![](//i.moshimo.com/af/i/impression?a_id=4187964&p_id=4131&pc_id=10468&pl_id=56580)![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%201%201%22%3E%3C/svg%3E)

WordPressオリジナルテーマ：月別アーカイブページ編
-----------------------------

![](https://junpei-sugiyama.com/wp-content/uploads/2022/04/wordpress-study.jpg)![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%201388%20781%22%3E%3C/svg%3E)

冒頭でも書いた通り、今回は大きく分けて2つのことを解説していきます。

1. 月別アーカイブリストを表示する方法
2. 月別アーカイブページを作る方法（date.phpを使用）

それでは順番に解説してきます。

### 月別アーカイブリストを表示する方法

これは表示させたい箇所にこれから紹介するコードを貼ればOKですが、方法はいくつかあります。

#### 月別アーカイブリスト

```
<ul class="monthly-list">
  <?php wp_get_archives( 'post_type=post&type=monthly&show_post_count=1' ); ?>
</ul>
```
#### 月別アーカイブリスト（ドロップダウン）

```
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

```
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

```
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

WordPressオリジナルテーマ制作のおすすめ教材
--------------------------

勉強方法は書籍、動画、プログラミングスクールなど色々あり、個人によって向き不向きがあると思います。

そこでタイプごとにご紹介させて頂きたいと思いますが、その前におすすめの勉強方法は以下になります。

1. 分かるところまでどんどん進める
2. 勉強に詰まる
3. 無視して次に進む or 他の教材などを使う
4. もう一度詰まった場所を見てみる
5. 理解できるようになっている

これからご紹介する教材と一緒にこのブログを読み進めて頂けると、より理解が深まるかと思います。

### 書籍

WordPressに関する本も沢山ありますが、ここでおすすめするのは2冊です。

#### いちばんやさしいWordPressの教本

リンク

こちらは以前私が持っていた本で、タイトル通りやさしいというかWordPressを1から勉強したい人向けの内容となっています。

Lightningという無料のWordPressテーマを使った制作方法など載っています。

ちなみにLightningを使ったサイト制作についてはこちらのブログでもご紹介しています。

[**Lightningを使ってサイト作成（前編）**](https://junpei-sugiyama.com/lightning-samplesite-first/)

[**Lightningを使ってサイト作成（後編）**](https://junpei-sugiyama.com/lightning-samplesite-second/)

#### 初心者からちゃんとしたプロになる WordPress基礎入門

リンク

こちらは私も個人的にお世話になっているちづみさんが書かれた本になります。

WordPressの本はこれまで何冊か購入しましたが、ダントツで読みやすいです。

ちなみに私が初めてにして唯一購入したコーディング教材がちづみさんのnoteでした。

また、初心者から実務経験者まで活用出来る非常におすすめの本となっています（電子書籍で購入しました）

### 動画教材

WordPressを動画で学びたい人はこちらの教材がおすすめです。

**[WordPress テーマ開発講座](https://click.linksynergy.com/deeplink?id=Ye/8zgpHXfQ&mid=47984&murl=https%3A%2F%2Fwww.udemy.com%2Fcourse%2Fwordpress_master%2F)**

本と違って動画だと手を動かしながら確認出来るのでいいですね。

こちらは[**Udemy**](https://click.linksynergy.com/fs-bin/click?id=Ye/8zgpHXfQ&offerid=1138543.179&type=3&subid=0)の有料教材ですが、かなりの頻度でセールを行っていて90%オフとか良くあるので出来ればそのタイミングを狙いましょう（私はセール時に購入しました）

『WordPressの動画教材と言えばコレ』というくらい有名な教材で、私を含め周りでも購入している人がたくさんいます。

もちろん[**Udemy**](https://click.linksynergy.com/fs-bin/click?id=Ye/8zgpHXfQ&offerid=1138543.179&type=3&subid=0)はWordPress以外の教材もたくさんあるので、気になる教材がセールをやっていたら購入を検討しても良いかも知れませんね。

### [プログラミングスクール](//af.moshimo.com/af/c/click?a_id=2741605&p_id=3554&pc_id=8575&pl_id=51304&guid=ON)

プログラミングスクールも色々ありますが『Web制作に特化したスクール』であれば**[デイトラ](//af.moshimo.com/af/c/click?a_id=2741605&p_id=3554&pc_id=8575&pl_id=51304&guid=ON)**![](//i.moshimo.com/af/i/impression?a_id=2741605&p_id=3554&pc_id=8575&pl_id=51304)![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%201%201%22%3E%3C/svg%3E)一択かと思います。

開校1年で受講生が7,000人を突破したオンラインスクールで、スクールと言ってもオンラインなので自宅で受講することが出来ます。

WordPressのカリキュラムは『Web制作コース上級編』にあります。

デイトラはTwitterをやっていれば分かりますが、悪い評判は見たことがなく、叩かれやすいWeb制作業界において非常にクリーンなイメージです。

カリキュラムの質が高いのはもちろん、他のスクールと比べて圧倒的なコスパかつ買い切りとなっています。

そしてカリキュラムはどんどん更新されるので『情報が古い』ということもなく、メンターに質問が出来る点も独学だと挫折しやすいWeb制作の勉強においてはおすすめです。

私の周りも『Web制作を始めるならまずデイトラを勧める』という人も多いです。

**[デイトラについて](https://junpei-sugiyama.com/daily-trial/)**は以下の記事を参照下さい。

[参考記事 ![デイトラのサービス内容・コース料金・評判・口コミをまとめて紹介【Web制作におすすめのスクール】](https://junpei-sugiyama.com/wp-content/uploads/2022/12/daily-trial-eye-catch.jpg)![デイトラのサービス内容・コース料金・評判・口コミをまとめて紹介【Web制作におすすめのスクール】](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%201388%20927%22%3E%3C/svg%3E)
##### デイトラのサービス内容・コース料金・評判・口コミをまとめて紹介【Web制作におすすめのスクール】

続きを見る](https://junpei-sugiyama.com/daily-trial/) 

また、

![](https://junpei-sugiyama.com/wp-content/uploads/2021/07/Sleepy-1024x1024.png)![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%2060%2040%22%3E%3C/svg%3E)10万円台でも厳しい・・・

という人は、完全無料で30日間Web制作を学べる**[ZeroPlus Gate](//af.moshimo.com/af/c/click?a_id=4187964&p_id=4131&pc_id=10468&pl_id=56580)![](//i.moshimo.com/af/i/impression?a_id=4187964&p_id=4131&pc_id=10468&pl_id=56580)![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%201%201%22%3E%3C/svg%3E)**がおすすめです。

[あわせて読みたい ![ZeroPlus Gateの口コミや評判と特徴やメリットを徹底解説【無料のプログラミングスクール】](https://junpei-sugiyama.com/wp-content/uploads/2024/02/zeroplus-gate.jpg)![ZeroPlus Gateの口コミや評判と特徴やメリットを徹底解説【無料のプログラミングスクール】](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%201388%20927%22%3E%3C/svg%3E)
##### ZeroPlus Gateの評判と特徴やメリットを解説【無料プログラミングスクール】

続きを見る](https://junpei-sugiyama.com/zeroplus-gate/) 

他にもDMM WEBCAMPやテックアカデミーにもWordPressコースがあるので、まずは無料相談を受けてみるといいと思います。

**[DMM WEBCAMPのWordPressコースはこちら](https://px.a8.net/svt/ejp?a8mat=3TLJXR+4RGV02+3XAE+6BEQA)![](https://www11.a8.net/0.gif?a8mat=3TLJXR+4RGV02+3XAE+6BEQA)![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%201%201%22%3E%3C/svg%3E)**

[あわせて読みたい ![DMM WEBCAMPの評判・口コミ・注意点など徹底解説【未経験者向けプログラミングスクール】](https://junpei-sugiyama.com/wp-content/uploads/2023/11/dmm-webcamp.jpg)![DMM WEBCAMPの評判・口コミ・注意点など徹底解説【未経験者向けプログラミングスクール】](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%201388%20927%22%3E%3C/svg%3E)
##### DMM WEBCAMPの評判・口コミ・注意点など徹底解説【未経験者向けプログラミングスクール】

続きを見る](https://junpei-sugiyama.com/dmm-webcamp/) 

**[TechAcademyのWordPressコースはこちら](//af.moshimo.com/af/c/click?a_id=2480723&p_id=1555&pc_id=2816&pl_id=22740&url=https%3A%2F%2Ftechacademy.jp%2Fwordpress-bootcamp%3Futm_source%3Dmoshimo%26utm_medium%3Daffiliate%26utm_campaign%3Dbannerad)![](//i.moshimo.com/af/i/impression?a_id=2480723&p_id=1555&pc_id=2816&pl_id=22740)![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%201%201%22%3E%3C/svg%3E)**

[あわせて読みたい ![テックアカデミーの評判・口コミ・注意点など徹底解説【プログラミングスクール受講者数No1！】](https://junpei-sugiyama.com/wp-content/uploads/2023/01/techacademy-eye-catch.jpg)![テックアカデミーの評判・口コミ・注意点など徹底解説【プログラミングスクール受講者数No1！】](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%201388%20927%22%3E%3C/svg%3E)
##### テックアカデミーの評判・口コミ・注意点など徹底解説【プログラミングスクール受講者数No1！】

続きを見る](https://junpei-sugiyama.com/techacademy/) 
### [**初心者向け実践型****WordPress****教材**](https://brmk.io/URuS)

これはBrainという知識共有プラットフォームで販売されている教材になります（👇画像クリック出来ます）

[![【"誰でも月収50万円以上"を達成可能にする】初心者向け実践型WordPress教材](https://junpei-sugiyama.com/wp-content/uploads/2021/03/roadmap-brain-masata.jpg)![【"誰でも月収50万円以上"を達成可能にする】初心者向け実践型WordPress教材](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20600%20314%22%3E%3C/svg%3E)](https://brmk.io/URuS)

こちらは学習面以外にも制作会社とのやり取りの流れや、特典では『作業前・納品前のチェックシート』『営業文のサンプル』『見積もり計算シート』など『実務に対する不安を払拭できる内容』となってます。

LP1本のコーディング費が安くても3万円くらいだと考えれれば、軽く1日で回収出来るので早めに『安心』を購入しましょう。

詳細はこちらからどうぞ👇

今だけ！購入者限定の10大特典付き🎁

[WordPress案件の不安を払拭！](https://brmk.io/URuS)

### [実務で使った2年分のコーディング&WordPressメモまとめ集](https://brain-market.com/u/junpei-sugiyama/a/bQjM5UTOgoTZsNWa0JXY)

[![【コピペで使える】コーディング&WordPressメモまとめ集を発売！（無料特典あり）](https://junpei-sugiyama.com/wp-content/uploads/2022/04/coding-wordpress.png)![【コピペで使える】コーディング&WordPressメモまとめ集を発売！（無料特典あり）](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20600%20398%22%3E%3C/svg%3E)](https://brain-market.com/u/junpei-sugiyama/a/bQjM5UTOgoTZsNWa0JXY)

これは私が販売しているものですが『教材』ではなく『コード集(コードスニペット集)』という感じです。

こちらは、1,100部以上売れています。

詳細については**[以下の記事](https://junpei-sugiyama.com/coding-wordpress/)**を参照ください（Brain販売ページと重なる内容もあります）

[あわせて読みたい ![【コピペで使える！】コーディング&WordPressコードスニペット集【無料特典あり】](https://junpei-sugiyama.com/wp-content/uploads/2022/04/coding-wordpress.png)![【コピペで使える！】コーディング&WordPressコードスニペット集【無料特典あり】](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%201388%20921%22%3E%3C/svg%3E)
##### 初心者向き教材！コーディング&WordPressコードスニペット集【コピペで使える】

続きを見る](https://junpei-sugiyama.com/coding-wordpress/) 

1,100部突破！

[コーディング効率と時給をアップしたい人はこちら！](https://brain-market.com/u/junpei-sugiyama/a/bQjM5UTOgoTZsNWa0JXY)

コピペで使える！

まとめ
---

![](https://junpei-sugiyama.com/wp-content/uploads/2021/03/wordpress-original-theme-end.jpg)![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20600%20338%22%3E%3C/svg%3E)

今回は、月別アーカイブページを作る方法を解説しました。

あまり実装する機会はないかも知れませんが、作れるようになっておきましょう。

以上になります。

関連記事[**WordPressオリジナルテーマ関連記事**](https://junpei-sugiyama.com/category/wordpress/original-theme/)

![](https://junpei-sugiyama.com/wp-content/uploads/2021/07/Joy-1024x1024.png)![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%2060%2040%22%3E%3C/svg%3E)この記事が役に立ったと思ったら、シェアボタンからX（旧Twitter）などにシェアすると、いいねされてフォロワーが増えたりすることがあるよ！[投げ銭で応援する🐶](https://ofuse.me/o?uid=71173)

* Twitter
* [Pinterest](https://www.pinterest.com/pin/create/button/?url=https%3A%2F%2Fjunpei-sugiyama.com%2Fwordpress-original-theme-13%2F&media=https://junpei-sugiyama.com/wp-content/uploads/2022/10/wordpress-original-theme-13-eye-catch.jpg&description=WordPressのオリジナルテーマの作り方を解説していくシリーズ。今回は月別アーカイブページの作り方です。)
* [LINE](//line.me/R/msg/text/?WordPress%E3%82%AA%E3%83%AA%E3%82%B8%E3%83%8A%E3%83%AB%E3%83%86%E3%83%BC%E3%83%9E%E3%81%AE%E4%BD%9C%E3%82%8A%E6%96%B9%E2%91%AC%EF%BC%88%E6%9C%88%E5%88%A5%E3%82%A2%E3%83%BC%E3%82%AB%E3%82%A4%E3%83%96%E3%83%9A%E3%83%BC%E3%82%B8%E7%B7%A8%EF%BC%89%0Ahttps%3A%2F%2Fjunpei-sugiyama.com%2Fwordpress-original-theme-13%2F)

* この記事を書いた人

  [![](https://junpei-sugiyama.com/wp-content/uploads/2021/07/favicon.png)![](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%2080%2080%22%3E%3C/svg%3E)](https://junpei-sugiyama.com/author/junpei0411blog/) 

じゅんぺい

37歳からWeb制作とブログ開始。Web制作歴5年目でコーディングとWordPressオリジナルテーマ制作が中心。これまで120件以上を納品。当ブログ月間最高15万PVで、370記事以上はWeb制作の技術記事。コンテンツ販売→累計売上1200万円&1500部超え。X（旧Twitter）フォロワー7200人以上。2024年3月からブログの経験を活かしてライターとしても活動を開始。

  

-[オリジナルテーマ](https://junpei-sugiyama.com/category/wordpress/original-theme/), [WordPress](https://junpei-sugiyama.com/category/wordpress/)  


[author](https://junpei-sugiyama.com/author/junpei0411blog/ "じゅんぺい")

#### おすすめ記事

 [![WordPressのオリジナルテーマ制作とは？【おすすめ教材あり】](https://junpei-sugiyama.com/wp-content/uploads/2024/09/what-is-wordpress-original-theme.jpg)![WordPressのオリジナルテーマ制作とは？【おすすめ教材あり】](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%201388%20927%22%3E%3C/svg%3E)](https://junpei-sugiyama.com/what-is-wordpress-original-theme/) 
##### [WordPressのオリジナルテーマ制作とは？【おすすめ教材あり】](https://junpei-sugiyama.com/what-is-wordpress-original-theme/)

     [![Custom Field Suiteの使い方【カスタムフィールドの繰り返しが無料で使える】](https://junpei-sugiyama.com/wp-content/uploads/2024/02/custom-field-suite.jpg)![Custom Field Suiteの使い方【カスタムフィールドの繰り返しが無料で使える】](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%201388%20927%22%3E%3C/svg%3E)](https://junpei-sugiyama.com/custom-field-suite/) 
##### [Custom Field Suiteの使い方【カスタムフィールドの繰り返しが無料で使える】](https://junpei-sugiyama.com/custom-field-suite/)

 [![LocalのLive LinkでWordPress開発サイトを共有する方法【サーバーにアップ不要】](https://junpei-sugiyama.com/wp-content/uploads/2022/11/local-live-link.jpg)![LocalのLive LinkでWordPress開発サイトを共有する方法【サーバーにアップ不要】](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%201388%20931%22%3E%3C/svg%3E)](https://junpei-sugiyama.com/local-live-link/) 
##### [LocalのLive LinkでWordPress開発サイトを共有する方法【サーバーにアップ不要】](https://junpei-sugiyama.com/local-live-link/)

     [![WordPressのバージョンをダウングレードするプラグイン『WP Downgrade Specific Core Version』の使い方](https://junpei-sugiyama.com/wp-content/uploads/2022/11/wp-downgrade-specific-core-version-eye-catch.jpg)![WordPressのバージョンをダウングレードするプラグイン『WP Downgrade Specific Core Version』の使い方](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%201388%20927%22%3E%3C/svg%3E)](https://junpei-sugiyama.com/wp-downgrade-specific-core-version/) 
##### [WordPressのバージョンをダウングレードするプラグイン『WP Downgrade Specific Core Version』の使い方](https://junpei-sugiyama.com/wp-downgrade-specific-core-version/)

 もっと読む  [![WordPressオリジナルテーマの作り方⑫（検索フォーム・検索結果ページ編）](https://junpei-sugiyama.com/wp-content/uploads/2022/10/wordpress-original-theme-12-eye-catch-100x100.jpg)![WordPressオリジナルテーマの作り方⑫（検索フォーム・検索結果ページ編）](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%2060%2060%22%3E%3C/svg%3E) WordPressオリジナルテーマの作り方⑫（検索フォーム・検索結果ページ編）](https://junpei-sugiyama.com/wordpress-original-theme-12/) [【転職のプロが解説】Web制作で未経験から効率よく転職できる方法3選 ![【転職のプロが解説】Web制作で未経験から効率よく転職できる方法3選](https://junpei-sugiyama.com/wp-content/uploads/2022/10/web-production-career-change-eye-100x100.jpg)![【転職のプロが解説】Web制作で未経験から効率よく転職できる方法3選](data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%2060%2060%22%3E%3C/svg%3E)](https://junpei-sugiyama.com/web-production-career-change/)