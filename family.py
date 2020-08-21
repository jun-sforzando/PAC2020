import random
from janken import pats, judge_result


# ジャンケンメンバーの配列
def members():
    all = ["源静香", "野比のび太", "ドラえもん", "骨川スネ夫", "ドラミ"]
    return list(all)


# キャラクターごとのジャンケンの手の設定と引数で今回のキャラクターの手を返すクラス
class Doraemon_family:
    def __init__(self, first, second, before_time,
                 first_before, second_before):
        self.first = first
        self.second = second
        self.before_time = before_time
        self.first_before = first_before
        self.second_before = second_before

    # 静香ちゃん
    # ランダムでグーチョキパーを出す
    def shizuka_hand(self):
        hand = random.randint(0, 2)
        return pats()[hand]

    # のび太
    # 通常はランダム、前回勝っていた場合は同じ手を出す
    def nobita_hand(self):
        # のび太の名前の取得
        nobi = members()[1]
        # 勝った時と負けた時の表示名を取得
        win = judge_result()[0]
        lose = judge_result()[1]
        # のび太が最初でかつ前回勝っていた場合
        if self.first == nobi and self.before_time == win:
            hand = self.first_before
            return hand
        # のび太が2番目でかつ負けていた場合
        elif self.second == nobi and self.before_time == lose:
            hand = self.second_before
            return hand
        else:
            # ランダムでグーチョキパーを出す
            hand = random.randint(0, 2)
        return pats()[hand]

    # ドラえもん
    # グーしか出せないようにする
    def dorachan_hand(self):
        hand = 0
        return pats()[hand]

    # スネ夫
    # チョキとパーをランダムで出す
    def suneo_hand(self):
        h = random.randint(0, 1)
        ha = [1, 2]
        hand = ha[h]
        return pats()[hand]

    # ドラミ
    # グーが50%、チョキとパーが25％ずつの確率で出す
    def dorami_hand(self):
        h = random.randint(0, 3)
        # 4分の2がグー、チョキとパーを4分の1ずつ
        ha = [0, 0, 1, 2]
        hand = ha[h]
        return pats()[hand]

    # メンバーと手を紐づける
    def member_hands(self):
        return {
            members()[0]: self.shizuka_hand(),
            members()[1]: self.nobita_hand(),
            members()[2]: self.dorachan_hand(),
            members()[3]: self.suneo_hand(),
            members()[4]: self.dorami_hand()
            }

    # 最初の人の手
    def f_hand(self):
        return self.member_hands()[self.first]

    # 2番目の人の手
    def s_hand(self):
        return self.member_hands()[self.second]
