## プロジェクト概要
Game A Week一週目に作られたゲームを作成したプロジェクト

## Game A Week
### Game A Weekとは
Game A Weekとは、一週間で1つゲームを作って、ゲーム開発者の経験値を上げる方法として、オランダのインディー系デベロッパー「Vlambeer」のRami Ismail氏が提唱したものです。

### 「Game A Week」の定義
1. 毎週ゲームを作る  
これはGame A Weekで最も重要なことです。ゲームを作り続けることが、ゲーム開発者としての経験を積むための唯一の最良の方法であるからです。

2. 毎週ゲームリリースする  
作ったゲームを遊んでもらって、面白かった・つまらなかったという反応をもらい、そのフィードバックを次に生かせるようにします。

3. 作り終えたゲームは修正しない  
個人ゲーム制作は基本的に期限がなく、どこまでも作り込むことができます。これはとても自由である反面、開発が永遠に終わらない（エターナる）原因となります。ですので、1週間経過したら、どんなに気に入ったゲームでも(改良すればもっと面白くなると思っても)、それに手を入れてはいけません。どうしても手を入れたいのであれば、Game A Week終了後に行います

4. パターン化を避ける  
同じようなゲームを作り続けないようにします。ゲームが完成したら、そのゲームのことは頭の外に追いやり、次のゲームのアイデアを考えるようにします。

5. 振り返りについて  
たとえゲームをたくさん作っても、悪い部分は改善し、良い部分は次に生かせるようにならないと、効果が薄くなってしまいます。そうならないように、振り返り（反省文）を書き残しておきます。

### 振り返りで検討した方が良い項目
- Idea: アイデア。コンセプト。テーマ。元ネタ
- What went right: やってみて良かったこと。うまくいったところ。成功したところ。次回に活かせそうなこと
- What went wrong: ダメだったところ。うまく機能しなかったところ。問題点。改善すべき点
- What I learned: 学んだこと。効果的なゲームデザインの方法やツールの使い方、獲得したテクニックなど

### 参考記事
[Game A Weekの定義まとめ](https://2dgames.jp/game_a_week/)  
[Game A Weekについて](https://note.com/syun77/n/n8063d509a864)  
[15週間でクソゲーを20本作って得たもの](https://qiita.com/2dgames_jp/items/6a23207fd0057df92552)  


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
