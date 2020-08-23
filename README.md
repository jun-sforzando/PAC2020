# Python Ability Check 2020 - <前田純>

## Requirement

- Python 3.8.5
- pytest 6.0.1
- tqdm 4.48.2

## Setup

1. ターミナルで `python3 -m venv venv` を実行して仮想環境を作成
1. `source venv/bin/activate` を実行
1. `pip install -r requirements.txt` を実行

## How to Run

1. `python main.py` を実行することでジャンケンができる
1. また、オプションを追加した実行も可能
   - `--first`, `--second` にキャラクター名、 `--trials` に勝負回数を指定
     - キャラクター名は `源静香` 、 `野比のび太` 、 `ドラえもん` 、 `骨川スネ夫` 、 `ドラミ` から選択可能
     - 勝負回数は `10000` 以下の整数のみ
   - e.g. `python main.py --first 骨川スネ夫 --second 源静香 --trials 3`

## How to Test

- ターミナルで `pytest --capture=no test_family.py` を実行

## References

- [Python でじゃんけんポイっ 初心者向け(回答と解説）](https://qiita.com/sandream/items/01374069f447b7748eba)
- [辞書に含まれるすべてのキーと値を取得する
  ](https://www.javadrive.jp/python/dictionary/index8.html)
- [はじめに — pep8-ja 1.0 ドキュメント](https://pep8-ja.readthedocs.io/ja/latest/)
- [python でコーディング規約(pep8)に準拠しているかチェック方法](https://qiita.com/HyunwookPark/items/b54baf66710ca5fa647a)
- [Python で小数点以下の桁数を指定する方法を現役エンジニアが解説【初心者向け】](https://techacademy.jp/magazine/23378)
- [Python の%演算子による文字列フォーマット](https://qiita.com/takahiro_itazuri/items/e585b46d096036bc837f)

## Miscellaneous

備考
