from family import Doraemon_family, members
from janken import pats, judge_result
from tqdm import tqdm
import random

# ジャンケンの手の名前を取得
guu = pats()[0]
cho = pats()[1]
paa = pats()[2]
# 1/3の計算
sanbun = 1 / 3
# 1/3の前後10％
san_zen = sanbun - 0.1
san_go = sanbun + 0.1

win = judge_result()[0]
lose = judge_result()[1]


# 静香ちゃんがグーを出す時の確率チェック
def test_shizuka_guu():
    # カウントする変数
    count = 0
    # 10000回実行した時のグーの結果をカウントする
    for i in tqdm(range(10000)):
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
    for i in tqdm(range(10000)):
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
    for i in tqdm(range(10000)):
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
    for i in tqdm(range(10000)):
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
    for i in tqdm(range(10000)):
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
    for i in tqdm(range(10000)):
        dora = Doraemon_family("", "", "", "", "")
        dorami = dora.dorami_hand()
        if dorami == paa:
            count += 1
    per = count / 10000
    # 25%の前後10%ならOK
    assert 0.15 <= per <= 0.35


# ドラえもんが必ずグーを出すチェック
def test_doraemon_guu():
    # カウントする変数
    count = 0
    # 10000回実行した時のグーの結果をカウントする
    for i in tqdm(range(10000)):
        dora = Doraemon_family("", "", "", "", "")
        dorachan = dora.dorachan_hand()
        if dorachan == guu:
            count += 1
    per = count / 10000
    # 全てグーならならOK
    assert per == 1.0


# スネ夫が出すチョキのチェック
def test_suneo_choki():
    # カウントする変数
    count = 0
    # 10000回実行した時のグーの結果をカウントする
    for i in tqdm(range(10000)):
        dora = Doraemon_family("", "", "", "", "")
        suneo = dora.suneo_hand()
        if suneo == cho:
            count += 1
    per = count / 10000
    # 40%~60%ならならOK
    assert 0.4 <= per <= 0.6


# スネ夫が出すパーのチェック
def test_suneo_paa():
    # カウントする変数
    count = 0
    # 10000回実行した時のグーの結果をカウントする
    for i in tqdm(range(10000)):
        dora = Doraemon_family("", "", "", "", "")
        suneo = dora.suneo_hand()
        if suneo == paa:
            count += 1
    per = count / 10000
    # 40%~60%ならならOK
    assert 0.4 <= per <= 0.6


# 通常ののび太がグーを出す時の確率チェック
def test_nobita_guu():
    # カウントする変数
    count = 0
    # 10000回実行した時のグーの結果をカウントする
    for i in tqdm(range(10000)):
        dora = Doraemon_family("", "", "", "", "")
        nobita = dora.nobita_hand()
        if nobita == guu:
            count += 1
    per = count / 10000
    # 1/3の前後10%ならOK
    assert san_zen <= per <= san_go


# 通常ののび太がチョキを出す時の確率チェック
def test_nobita_cho():
    # カウントする変数
    count = 0
    # 10000回実行した時のグーの結果をカウントする
    for i in tqdm(range(10000)):
        dora = Doraemon_family("", "", "", "", "")
        nobita = dora.nobita_hand()
        if nobita == cho:
            count += 1
    per = count / 10000
    # 1/3の前後10%ならOK
    assert san_zen <= per <= san_go


# 通常ののび太がパーを出す時の確率チェック
def test_nobita_paa():
    # カウントする変数
    count = 0
    # 10000回実行した時のグーの結果をカウントする
    for i in tqdm(range(10000)):
        dora = Doraemon_family("", "", "", "", "")
        nobita = dora.nobita_hand()
        if nobita == paa:
            count += 1
    per = count / 10000
    # 1/3の前後10%ならOK
    assert san_zen <= per <= san_go


# 前回firstで勝ったのび太が前回と同じ手を出すかチェック
def test_nobita_first_win():
    # カウントする変数
    count = 0
    # のび太の名前を取得
    nobita_name = members()[1]
    # グーチョキパーをランダムで出す
    janken_randam = random.choice(pats())
    # 前回と同じ手を必ず出しているかチェック
    for i in tqdm(range(10000)):
        dora = Doraemon_family(nobita_name, "", win, janken_randam, "")
        nobita = dora.nobita_hand()
        if nobita == dora.first_before:
            # 同じ手の合格をカウント
            count += 1
    # 100%ならOK
    assert count == 10000


# 前回secondで相手を負けさせたのび太が前回と同じ手を出すかチェック
def test_nobita_second_lose():
    # カウントする変数
    count = 0
    # のび太の名前を取得
    nobita_name = members()[1]
    # グーチョキパーをランダムで出す
    janken_randam = random.choice(pats())
    # 前回と同じ手を必ず出しているかチェック
    for i in tqdm(range(10000)):
        dora = Doraemon_family("", nobita_name, lose, "", janken_randam)
        nobita = dora.nobita_hand()
        if nobita == dora.second_before:
            # 同じ手の合格をカウント
            count += 1
    # 100%ならOK
    assert count == 10000
