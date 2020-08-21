# 結果の文字
def judge_result():
    return["Win", "Lose", "Draw"]


# ジャンケンで使う手
def pats():
    return ["グー", "チョキ", "パー"]


# ジャンケンをした時の結果を返す
# 引数は「グー、チョキ、パー」
def jankenpon(first, second):
    # 勝負の結果ごとの値
    win = judge_result()[0]
    lose = judge_result()[1]
    draw = judge_result()[2]

    # ジャンケンの手の名前
    guu = pats()[0]
    cho = pats()[1]
    paa = pats()[2]
    if first in pats() and second in pats():
        # あいこの時
        if first == second:
            judge = draw
        else:
            # グーを出した時
            if first == guu:
                if second == cho:
                    judge = win
                else:
                    judge = lose
            # チョキを出した時
            elif first == cho:
                if second == paa:
                    judge = win
                else:
                    judge = lose
            # それ以外(パーを出した時)
            else:
                if second == guu:
                    judge = win
                else:
                    judge = lose

        return judge
    else:
        raise ValueError("入力は「%s」「%s」「%s」でお願いします。" % (guu, cho, paa))


# 勝率の計算
def win_rate(win, trials):
    w_rate = win / trials * 100
    return " {:.2f} %".format(w_rate)


# # 絶対に勝つパターン
# def always_winner(jan):
#     if jan == guu:
#         return paa
#     elif jan == cho:
#         return guu
#     else:
#         return cho
