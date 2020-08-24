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
def test_shizuka():
    # それぞれの手をカウントする変数
    guu_count = 0
    cho_count = 0
    paa_count = 0
    # 10000回実行した時のグーの結果をカウントする
    for i in tqdm(range(10000)):
        dora = Doraemon_family("", "", "", "", "")
        shizuka = dora.shizuka_hand()
        # 出した手をそれぞれカウントしていく
        if shizuka == guu:
            guu_count += 1
        if shizuka == cho:
            cho_count += 1
        if shizuka == paa:
            paa_count += 1
    # それぞれの手が1/3の前後10％ならOK
    assert san_zen <= guu_count / 10000 <= san_go
    assert san_zen <= cho_count / 10000 <= san_go
    assert san_zen <= paa_count / 10000 <= san_go


# ドラミちゃんがグーを出す時の確率チェック
def test_dorami_guu():
    # それぞれの手をカウントする変数
    guu_count = 0
    cho_count = 0
    paa_count = 0
    # 10000回実行した時のグーの結果をカウントする
    for i in tqdm(range(10000)):
        dora = Doraemon_family("", "", "", "", "")
        dorami = dora.dorami_hand()
        # 出した手をそれぞれカウントしていく
        if dorami == guu:
            guu_count += 1
        if dorami == cho:
            cho_count += 1
        if dorami == paa:
            paa_count += 1
    # グーは50%の前後10%ならOK
    assert 0.4 <= guu_count / 10000 <= 0.6
    # チョキは25%の前後10%ならOK
    assert 0.15 <= cho_count / 10000 <= 0.35
    # パーは25%の前後10%ならOK
    assert 0.15 <= paa_count / 10000 <= 0.35


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
def test_suneo():
    # それぞれの手をカウントする変数
    guu_count = 0
    cho_count = 0
    paa_count = 0
    # 10000回実行した時のグーの結果をカウントする
    for i in tqdm(range(10000)):
        dora = Doraemon_family("", "", "", "", "")
        suneo = dora.suneo_hand()
        # 出した手をそれぞれカウントしていく
        if suneo == guu:
            guu_count += 1
        if suneo == cho:
            cho_count += 1
        if suneo == paa:
            paa_count += 1
    # グーは0ならOK
    assert guu_count == 0
    # チョキは50%の前後10%ならOK
    assert 0.4 <= cho_count / 10000 <= 0.6
    # パーは50%の前後10%ならOK
    assert 0.4 <= paa_count / 10000 <= 0.6


# 通常ののび太出す手の確率チェック
def test_nobita():
    # それぞれの手をカウントする変数
    guu_count = 0
    cho_count = 0
    paa_count = 0
    # 10000回実行した時のグーの結果をカウントする
    for i in tqdm(range(10000)):
        dora = Doraemon_family("", "", "", "", "")
        nobita = dora.nobita_hand()
        # 出した手をそれぞれカウントしていく
        if nobita == guu:
            guu_count += 1
        if nobita == cho:
            cho_count += 1
        if nobita == paa:
            paa_count += 1
    # それぞれの手が1/3の前後10％ならOK
    assert san_zen <= guu_count / 10000 <= san_go
    assert san_zen <= cho_count / 10000 <= san_go
    assert san_zen <= paa_count / 10000 <= san_go


# 前回firstで勝ったのび太が前回と同じ手を出すかチェック
def test_nobita_first_win():
    # カウントする変数
    count = 0
    # のび太の名前を取得
    nobita_name = members()[1]
    # グーチョキパーをランダムで出す
    janken_randam = random.choice(pats())
    # 前回と同じ手を必ず出しているか10000回チェック
    for i in tqdm(range(10000)):
        # 前回firstののび太が勝った後ののび太の手をランダムで作成
        dora = Doraemon_family(nobita_name, "", win, janken_randam, "")
        nobita = dora.nobita_hand()
        # 前回の自分(first)と同じ手を出していればカウントする
        if nobita == dora.first_before:
            count += 1
    # すべての勝負で同じ手を出していたらOK
    assert count == 10000


# 前回secondで相手を負けさせたのび太が前回と同じ手を出すかチェック
def test_nobita_second_lose():
    # カウントする変数
    count = 0
    # のび太の名前を取得
    nobita_name = members()[1]
    # グーチョキパーをランダムで出す
    janken_randam = random.choice(pats())
    # 前回と同じ手を必ず出しているか10000回チェック
    for i in tqdm(range(10000)):
        # 前回secondののび太が勝った後ののび太の手をランダムで作成
        dora = Doraemon_family("", nobita_name, lose, "", janken_randam)
        nobita = dora.nobita_hand()
        # 前回の自分(second)と同じ手を出していればカウントする
        if nobita == dora.second_before:
            count += 1
    # 100%ならOK
    assert count == 10000
