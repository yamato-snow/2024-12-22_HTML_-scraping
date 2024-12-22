# Pythonプロジェクトテンプレート

シンプルなPython開発環境のテンプレートです。

作成日：2024年11月01日
作成者：yamato-snow

### 前提条件

- Gitがインストールされていること
- Homebrewがインストールされていること（macOSの場合）
    - 参考：https://brew.sh/ja/
- Pyenvがインストールされていること
    - 参考：https://hitori-sekai.com/python/mac-python-install/ (macOSの場合)
    - 参考：https://almonta2021blog.com/pyenv-version-windows/ (Windowsの場合)

## セットアップ手順

### 1. プロジェクトの作成

```bash
# リポジトリのクローン
git clone https://github.com/yamato-snow/python_testproject_venv.git <プロジェクト名>
cd <プロジェクト名>

# 開発用ブランチの作成と切り替え
git branch <ブランチ名>
git checkout <ブランチ名>
```

### 2. 初回セットアップ

```bash
# Pythonバージョンの設定
pyenv local 3.13.1

## Pythonをインストールしていない場合
pyenv install 3.13.1

# 仮想環境の作成
python -m venv .venv

# 仮想環境の有効化
# Windows:(コマンドプロンプトで実行)
.venv\Scripts\activate.bat
# macOS:
source .venv/bin/activate

# 依存パッケージのインストール
pip install --upgrade pip
pip install -r requirements.txt

コマンドプロンプトの場合は、'pip'の前に'python -m 'をつける必要があります。

# 仮想環境の無効化
deactivate

```

### 3. 2回目以降の実行

```bash
# 仮想環境の有効化のみ実行
# Windows:
.venv\Scripts\activate.bat
# macOS:
. .venv/bin/activate
```

### 4. プログラムの実行

```bash
python main.py
```

### 5. 変更の保存

```bash
# 変更をコミット
git add .
git commit -m "変更の説明"

# リモートリポジトリにプッシュ
git push origin <ブランチ名>
```

## プロジェクト構成

```
.
├── .venv/              # Python仮想環境
├── .gitignore         # Git除外設定ファイル
├── .python-version    # Python指定バージョン
├── main.py            # メインプログラム
└── requirements.txt   # 依存パッケージリスト
```

## ライセンス

MITライセンス
```