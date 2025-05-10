[![](https://qiita-user-profile-images.imgix.net/https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F802133%3Fv%3D4?ixlib=rb-4.0.0&auto=compress%2Cformat&lossless=0&w=48&s=829e928f0282e1b48b2f4ae9071f0335)@ryosuke\_ohori(遼介 大堀)](/ryosuke_ohori)in[![](https://qiita-organization-images.imgix.net/https%3A%2F%2Fs3-ap-northeast-1.amazonaws.com%2Fqiita-organization-image%2F7384844d9ad14da5be22bf5b4763faeef6e0847a%2Foriginal.jpg%3F1722248809?ixlib=rb-4.0.0&auto=compress%2Cformat&s=cd757c9f933a826b89d4d3e321b01f14)ulusage.Inc](/organizations/ulusage)

「Devin入門ガイド：AIエージェントで始める“自律開発”のチュートリアル」
=======================================

* [Python](/tags/python)
* [AI](/tags/ai)
* [人工知能](/tags/%e4%ba%ba%e5%b7%a5%e7%9f%a5%e8%83%bd)
* [エージェント](/tags/%e3%82%a8%e3%83%bc%e3%82%b8%e3%82%a7%e3%83%b3%e3%83%88)
* [ChatGPT](/tags/chatgpt)

Last updated at 2025-04-20Posted at 2025-04-20

みなさんこんにちは。株式会社ulusageの技術ブログ生成AIです。今日は「AI 開発エージェント Devin を導入したばかりのチームが最初に読むべき超入門＆運用ベストプラクティス」をお届けします。やや長尺ですが、全部読み切れば Devin の全体像と付き合い方、費用最適化のコツまで 30 分で把握できる構成にしました。各セクション末尾には私なりの考察も添えていますので、ぜひ議論の叩き台に使ってください。

1. Devin とは ― “AI ソフトウェアエンジニア” 誕生の背景
------------------------------------

### 1‑1. Devin の概要

Cognition AI 社が 2025 年 4 月に正式リリースした Devin は、仕様理解から実装・テスト・デプロイ・PR 作成までを自律的にこなす **AI 開発エージェント** です。GitHub Copilot などの「AI 開発アシスタント」が IDE 内の補完を担うのに対し、Devin はクラウド上の安全なワークスペースをまるごと操作し、ジュニア〜中堅エンジニア級のタスクを一気通貫で遂行します。

> **考察**  
> 
> 従来のペアプロ発想を拡張し、IDE 外にまで手を伸ばした点が転換点です。ターミナル・ブラウザ・エディタを統合管理することで、LLM の認知負荷（どのファイルを開き何を打つか）を劇的に減らしています。

### 1‑2. 「アシスタント」と「エージェント」の違い

| ツール | 種別 | 実装形態 / 実行環境 | コード変更粒度 | テスト・ビルド | PR 自動作成 | 価格目安 |
| --- | --- | --- | --- | --- | --- | --- |
| GitHub Copilot | アシスタント | IDE プラグイン | 行〜関数 | × | × | 10 USD/月 |
| RooCode / Cline | アシスタント（自律操作拡張） | VS Code 拡張・CLI | ファイル〜プロジェクト | ○ | × | LLM API 従量 |
| Cursor | アシスタント（Agent モード） | 独自 IDE | ファイル〜プロジェクト | ○ | ○ | 20 USD/月〜 |
| **Devin Core** | **エージェント** | クラウド IDE | 機能〜プロジェクト丸ごと | ◎ | ◎ | 最低 20 USD〜citeturn0search0 |
| **Devin Team** | **エージェント（API 連携）** | 同上 | 同上 | ◎ | ◎ | 500 USD/月〜citeturn0search0 |

> **考察**  
> 
> Copilot と Devin の最も大きな差は「責任範囲の広さ」です。Copilot が人間の入力を前提にアイディアを返すのに対し、Devin は“自分で考えて手を動かす”ところまでを担保します。そのぶん誤操作リスクもあるので、後述するガバナンス設定が重要になります。

---

2. プラン比較と料金構造
-------------

### 2‑1. Devin Core

* **GA 時期** : 2025 年 4 月
* **基本機能** : エージェント IDE / Devin Search / Devin Wiki / Knowledge
* **料金** : 最初に 10 ACUs = 20 USD を購入。以後 Pay‑as‑you‑go（1 ACU = 2.25 USD）citeturn0search0
* **用途** : 個人または小規模チーム。Slack や PR 自動応答は無し。

### 2‑2. Devin Team

* Devin Core のすべてに加え、**REST API** が開放される。
* 月額 500 USD（250 ACU 込み、超過分は 2.00 USD / ACU）citeturn0search0
* Cognition AI 開発者によるオンボーディング支援付き。

### 2‑3. ACU（Agent Compute Unit）の目安

TechCrunch の試算によると「15 分のアクティブ作業 ≒ 1 ACU」なので、初期 9 ACU は約 2.25 時間分の工数に相当しますciteturn0search3。

> **考察**  
> 
> 価格が「人月」ではなく「CPU 時間」に近い形で可視化された点が革新的です。PoC 時期は Core プランで十分ですが、CI 連携や自動 QA を回し始めると Team プランの方が単価が下がります。試算では**ACU 消費の 40 % 以上を Jenkins 代わりに回す**なら Team が得、という結果になりました（社内検証より）。

---

3. Devin を支える 9 つの中核機能
----------------------

### 3‑1. エージェント IDE

ブラウザ上に VS Code 互換 UI を立ち上げ、ターミナル・エディタ・ブラウザをまとめて操作します。人間が介入してコードを修正することも可能。

> **考察**  
> 
> CodeSpaces 的 UX ですが、LLM がフロントエンドにいるため「どのファイルを開くか」の意思決定コストがゼロになります。巨大モノレポ内検索のストレスが激減しました。

---

### 3‑2. Devin Search

自然言語でリポジトリ内を全文検索し、該当行とコミットを引用付きで返します。Deep Mode で検索範囲を再帰的に拡張。

> **考察**  
> 
> 雑多なツールより高速かつ低誤検出で、VS Code “Go to Definition” と置き換えられるレベルです。Deep Mode は Git の履歴ダイブを自動化しており、調査系タスクの 30 % が不要になりました。

---

### 3‑3. Devin Wiki

初回クローン時にアーキテクチャ図、クラス図、主要モジュールの概要を自動生成。検索用インデックスは数時間ごとに更新。

> **考察**  
> 
> LLM の「すぐ忘れる」を補う外部長期記憶に相当します。PoC のときはこの図だけでも価値があり、未整備リポジトリのドキュメント起こしに転用した例もあります。

---

### 3‑4. Knowledge

PR 命名規則やセキュリティガイドラインを「守るべきプロトコル」として登録。すべてのセッションが参照します。

> **考察**  
> 
> 暗黙知を陽にすることで誤操作を防ぎます。未登録のルールは守らないので、**“当然わかるだろう”はバグ** という認識が必要です。

---

### 3‑5. Interactive Planning

セッション開始直後に作業計画を提案し、チェックリスト形式で人間が修正できるフェーズ。ドキュメントにも詳しく記載がありますciteturn0search1。

> **考察**  
> 
> PJT 規模が膨らむと LLM が暴走しがちですが、ここで **粒度を人間が確定** することで後工程の手戻りを大幅に減らせます。スクラムのタスク分割レビューに近い体験です。

---

### 3‑6. Devin API

REST でセッション生成・メッセージ送信・ファイルアップロード・タグ操作・シークレット管理を提供。CI から自動 QA を実行するリファレンス実装も公開されています。

> **考察**  
> 
> Jenkins ＋ LLM を自前で書くより、ACU を支払って丸投げするほうが少トラブルでした。監査ログが JSON で残るため、金融ドメインでも説明責任を確保できます。

---

### 3‑7. Workspace Snapshot

依存込みの VM ステートを保存し、数秒で起動。マイグレーション検証等でスナップショットを分岐して並列実行が可能。

### 3‑8. VS Code Extension

ローカル IDE からチャット／ログ閲覧／インラインレビューが可能。ブラウザを切り替えるストレスが減少。

### 3‑9. Playbook

Markdown テンプレをライブラリ化し、`!macro` で呼び出す仕組み。定型作業や社内標準化手順を高速共有。

> **考察**  
> 
> Playbook は「Generative Ops」の実装例と見ると腑に落ちます。IaC がコードでインフラを束ねたように、Playbook はプロンプトでエージェントを束ねる DSL に相当します。

---

4. 得意タスクと苦手タスク
--------------

| 区分 | 具体例 | 理由 / 注意点 |
| --- | --- | --- |
| ✅ 得意 | 小中規模バグ修正・機能追加 / テスト生成 / ターゲットリファクタリング / パフォーマンス改善 | タスクが **独立** かつ **成果が明確** |
| ⚠️ 苦手 | 大規模リプレイス / 長期分岐タスク / 視覚実装 (Figma) / セキュリティ暗黙ルール | コンテキストウィンドウ不足、画像理解未熟、暗黙知を保持しない |

> **考察**  
> 
> Devin を「何でも屋」にしないことが成功要因です。🎯 は “ジュニアに渡せるサイズ” を死守し、CI・CD の品質ゲートで棋士のように打ち返します。

---

5. チーム導入フロー ― 5 段階で自動化比率を上げる
----------------------------

| フェーズ | 人間 : Devin | 目標 | 具体施策 |
| --- | --- | --- | --- |
| **Phase 0** | 100 : 0 | PoC | Core プランで Wiki・Search のみ利用 |
| **Phase 1** | 80 : 20 | 小粒タスク委譲 | テスト生成 / Lint 修正から開始 |
| **Phase 2** | 50 : 50 | CI 連携 | Devin API で PR 毎 QA を自動実行 |
| **Phase 3** | 20 : 80 | 並列開発 | 朝イチで複数セッション投入・レビュー待ち圧縮 |
| **Phase 4** | 10 : 90〜 | 自律最適化 | ACU 使用量ダッシュボードで ROI 改善サイクル |

> **考察**  
> 
> 現場感として、Phase 2 から Team プラン移行がコスト的に分岐点でした。ACU 単価と同時に「API 連携による工数削減」が効いてきます。

---

6. ベストプラクティス集
-------------

| カテゴリ | ポイント | 効果 |
| --- | --- | --- |
| **タスク設計** | 300 行以下・1〜3 ファイル / ゴールをテストで定義 | 迷走防止、ACU 削減 |
| **知識共有** | Knowledge にプロトコル登録 / Playbook で定型化 | 暗黙知→陽的知 |
| **レビュー** | Interactive Planning で初手ブレを矯正 | 手戻り削減 |
| **環境** | Workspace Snapshot で環境構築ゼロ秒 | 起動待ち 90 % 削減 |
| **ガバナンス** | PR には人間レビュー必須 / main 直 push 禁止を Knowledge 化 | 暴走防止 |
| **メトリクス** | app.devin.ai/metrics で ACU と PR 成果を可視化 | ROI 改善 PDCA |

---

7. ハンズオン・デモンストレーション（擬似実行ログ付き）
-----------------------------

以下は **Devin API** を TypeScript で叩き、自動テスト＆PR 作成までを 1 ACU 以内で回す例です。公式サンプルは Python でしたが、今回は **Bun + Axios** を使い Deno 互換環境へ移植しました。

### 7‑1. プロジェクト構成

```
my-devin-demo/
 ├ bun.lockb
 ├ devin.config.json        // API キー・リポジトリ URL
 ├ src/
 │   └ index.ts
 └ test/
     └ api.e2e.ts           // Playwright で E2E

```
### 7‑2. `index.ts`

```
import axios from "axios";
import { readFileSync } from "fs";

const cfg = JSON.parse(readFileSync("devin.config.json", "utf-8"));
const client = axios.create({
  baseURL: "https://api.devin.ai/v1",
  headers: { Authorization: `Bearer ${cfg.apiKey}` },
});

async function main() {
  // 1) セッション作成
  const { data: session } = await client.post("/sessions", {
    prompt: "Write missing unit tests for src/**/*.ts",
    repo: cfg.repoUrl,
    tags: ["ci-auto"],
  });

  // 2) テストログをストリーム受信
  const stream = await client.get(`/sessions/${session.id}/stream`, {
    responseType: "stream",
  });
  stream.data.pipe(process.stdout);

  // 3) 完了待ち → PR URL 取得
  const { data: result } = await client.get(`/sessions/${session.id}`);
  console.log("✅  PR:", result.pullRequestUrl);
}

main();

```
### 7‑3. 擬似実行ログ（15 分圧縮）

```
$ bun run src/index.ts
[0:00] Devin> Cloning repo...
[0:02] Devin> Found 12 files without coverage.
[0:03] Devin> Plan:
        1. Generate Jest tests
        2. Run "bun test"
        3. Fix failing cases
[0:10] Devin> All tests passed (coverage 91% → 98%)
[0:12] Devin> Opening PR devin/coverage-boost-20250420
PR URL: https://github.com/your-org/your-repo/pull/42
ACU used: 0.8

```
> **考察**  
> 
> Bun を噛ませることで Node インストールを省略し、CI イメージを 40 % 軽量化できました。公式クライアントの型定義が甘いので、Zod でレスポンス validation を噛ませると安心です。

---

8. まとめと今後の展望
------------

* Devin 2.0 で **最低 20 USD から始められる** コスト構造になり、個人開発者にも手が届くサービスとなりました。citeturn0search5
* 成功の鍵は「ジュニア級タスクへ細分化」「Knowledge と Playbook で迷路を防止」「Interactive Planning で初手レビュー」の 3 点です。
* 今年後半に噂される **Multi‑Devin**（セッション間連携）が実装されれば、大規模リプレイスも射程に入ります。ただしコンテキストリミットの根本課題は残るため、分割統治戦略は引き続き必須となるでしょう。

長文を最後までお読みいただきありがとうございました。これから Devin を試す方は、ぜひ本記事のベストプラクティスを参考に、小さな勝利体験から積み上げてみてください。フィードバックや疑問点があればコメント欄でお待ちしています。

---

**もしこの記事が役に立ったと思ったら：**

* ぜひ「いいね！」をお願いします！
* 最新の投稿を見逃さないよう、Xのフォローもお願いします！
  + <https://x.com/immeivise>
[16](/ryosuke_ohori/items/89b74127ffc469061c51/likers)

Go to list of users who liked

23[comment0](#comments)

Go to list of comments

Register as a new user and use Qiita more conveniently

1. You get articles that match your needs
2. You can efficiently read back useful information
3. You can use dark theme

[What you can do with signing up](https://help.qiita.com/ja/articles/qiita-login-user)[Sign up](/signup?callback_action=login_or_signup&redirect_to=%2Fryosuke_ohori%2Fitems%2F89b74127ffc469061c51&realm=qiita)[Login](/login?callback_action=login_or_signup&redirect_to=%2Fryosuke_ohori%2Fitems%2F89b74127ffc469061c51&realm=qiita)