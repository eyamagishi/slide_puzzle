## プロジェクト概要
Game A Week一週目に作られたゲームを作成したプロジェクト

## 振り返り
### Idea
スライドパズルを作成しました。
![スライドパズル.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/2954837/43461242-6d15-49fa-ac12-9300923add55.png)

https://github.com/eyamagishi/slide_puzzle

### What I learned
- Pythonを使用しての開発
- Pygameを使用しての開発
- Gameの開発
- LICENSEの表記追加
- パリティ設定

### What went right
- Pythonの簡単さは理解できた
- Pygameを使って画面を表示することができた

### What went wrong
- パリティの精度
パリティ機能を作成したものの正常に機能していないように見える（3回に1回程度解けない問題が出てくる）。以下を参考にしたもののPythonになれていないこと、数式としての理解がまだ浅いため実装漏れをしたんだと思う...。次回パズルを作成する際には気を付けたい。

https://manabitimes.jp/math/979

## インストール方法
1. リポジトリをクローンします。
```bash
git clone https://github.com/eyamagishi/slide_puzzle.git
cd slide_puzzle
```

2. 仮想環境を作成し、アクティベートします（オプションですが推奨）。
```bash
python3 -m venv env
source env/bin/activate  # Unix/macOS
venv\Scripts\activate  # Windows
```

3. 必要な依存関係をインストールします。
```bash
pip install -r requirements.txt
```

## 使い方
1. プロジェクトをパッケージとして実行します。
```bash
python3 -m my_project.main
```

2. ゲームが起動し、スライドパズルをプレイすることができます。矢印キーを使ってタイルを移動させてください。

## ディレクトリ構成
```markdown
slide_puzzle/
├── docs/
│   └── index.md
├── env/
├── slide_puzzle/
│   ├── __init__.py
│   ├── game_logic.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   └── test_game_logic.py
├── .gitignore
├── README.md
└── requirements.txt
```

- my_project/: メインのプロジェクトディレクトリ
    - __init__.py: パッケージとして扱うための初期化ファイル
    - game_logic.py: ゲームロジックを含むファイル
    - main.py: メインの実行ファイル
- tests/: テストスクリプトを含むディレクトリ
    - __init__.py: パッケージとして扱うための初期化ファイル
    - test_game_logic.py: ゲームロジックのテストを含むファイル
- docs/: ドキュメントを含むディレクトリ
    - index.md: プロジェクトのドキュメント
- requirements.txt: プロジェクトの依存関係リスト
- README.md: このファイル
- .gitignore: Gitが無視するファイルやディレクトリのリスト

## テスト方法
テストは、以下のコマンドを実行して実行できます。

```bash
python -m unittest discover -s tests
```
これにより、tests/ ディレクトリ内のすべてのテストが実行されます。

## ライセンス
このプロジェクトはMITライセンスの下で公開されています。詳細は、[LICENSE](LICENSE)ファイルをご覧ください。

## 貢献方法
1. このリポジトリをフォークします。
2. 新しいブランチを作成します（git checkout -b feature/fooBar）。
3. 変更をコミットします（git commit -am 'Add some fooBar'）。
4. ブランチにプッシュします（git push origin feature/fooBar）。
5. プルリクエストを開きます。

## 連絡先
Author: eyamagishi  
Email: e.yamagishi0625@example.com  
GitHub: [eyamagishi](https://github.com/eyamagishi)  
