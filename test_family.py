from family import Doraemon_family
from janken import pats
import pytest

# ジャンケンの手の名前を取得
guu = pats()[0]
cho = pats()[1]
paa = pats()[2]
# 1/3の計算
sanbun = 1 / 3
# 1/3の前後10％
san_zen = sanbun - 0.1
san_go = sanbun + 0.1


# 静香ちゃんがグーを出す時の確率チェック
def test_shizuka_guu():
    # カウントする変数
    count = 0
    # 10000回実行した時のグーの結果をカウントする
    for i in range(10000):
        dora = Doraemon_family("", "", "", "", "")
        shizuka = dora.shizuka_hand()
        if shizuka == guu:
            count += 1
    per = count / 10000
    # 1/3の前後10%ならOK
    assert san_zen <= per <= san_go


# 静香ちゃんがチョキを出す時の確率チェック
def test_shizuka_cho():
    # カウントする変数
    count = 0
    # 10000回実行した時のチョキの結果をカウントする
    for i in range(10000):
        dora = Doraemon_family("", "", "", "", "")
        shizuka = dora.shizuka_hand()
        if shizuka == cho:
            count += 1
    per = count / 10000
    # 1/3の前後10%ならOK
    assert san_zen <= per <= san_go


# 静香ちゃんがパーを出す時の確率チェック
def test_shizuka_paa():
    # カウントする変数
    count = 0
    # 10000回実行した時のパーの結果をカウントする
    for i in range(10000):
        dora = Doraemon_family("", "", "", "", "")
        shizuka = dora.shizuka_hand()
        if shizuka == paa:
            count += 1
    per = count / 10000
    # 1/3の前後10%ならOK
    assert san_zen <= per <= san_go


# ドラミちゃんがグーを出す時の確率チェック
def test_dorami_guu():
    # カウントする変数
    count = 0
    # 10000回実行した時のパーの結果をカウントする
    for i in range(10000):
        dora = Doraemon_family("", "", "", "", "")
        dorami = dora.dorami_hand()
        if dorami == guu:
            count += 1
    per = count / 10000
    # 50%の前後10%ならOK
    assert 0.4 <= per <= 0.6


# ドラミちゃんがチョキを出す時の確率チェック
def test_dorami_cho():
    # カウントする変数
    count = 0
    # 10000回実行した時のパーの結果をカウントする
    for i in range(10000):
        dora = Doraemon_family("", "", "", "", "")
        dorami = dora.dorami_hand()
        if dorami == cho:
            count += 1
    per = count / 10000
    # 25%の前後10%ならOK
    assert 0.15 <= per <= 0.35


# ドラミちゃんがパーを出す時の確率チェック
def test_dorami_paa():
    # カウントする変数
    count = 0
    # 10000回実行した時のパーの結果をカウントする
    for i in range(10000):
        dora = Doraemon_family("", "", "", "", "")
        dorami = dora.dorami_hand()
        if dorami == paa:
            count += 1
    per = count / 10000
    # 25%の前後10%ならOK
    assert 0.15 <= per <= 0.35
