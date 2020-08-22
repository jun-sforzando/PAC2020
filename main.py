#!/usr/bin/env python3
from janken import judge_result, jankenpon, win_rate
from family import Doraemon_family, members


def main(first: str, second: str, trials: int):
    # 勝った時の文字を判別
    win = judge_result()[0]

    # すべてのメンバー
    all_member = members()

    # 記録のための変数と配列
    # 前回出した手
    first_before = ""
    second_before = ""
    # 前回の結果
    before_time = ""
    # 全ての結果
    all_match = []
    # 勝った数を計測
    win_counter = 0

    # 入力されている値が正しいか確認
    if type(trials) != int:
        raise ValueError("整数を入力してください")
    if 10000 < trials:
        raise ValueError("回数が多すぎます")
    if (type(first) != str) or (type(second) != str):
        raise ValueError("文字を入力してください。")
    if not (first in all_member) or not (second in all_member):
        raise ValueError("ジャンケンメンバーではない名前が入力されています。")

    # 正しい名前と数字が入力された場合
    for i in range(trials):
        chalengers = Doraemon_family(first, second,
                                     before_time, first_before,
                                     second_before)
        # それぞれの手
        f_h = chalengers.f_hand()
        s_h = chalengers.s_hand()
        # ジャンケンをする
        pon = jankenpon(f_h, s_h)
        jan_res = (f_h, s_h, pon)

        # 今回の結果を記録
        before_time = pon
        first_before = f_h
        second_before = s_h

        # 結果を配列に追加
        all_match.append(jan_res)
        # 勝ったらカウントしていく
        if pon == win:
            win_counter += 1

    # 勝率計算したものを追加
    print("{} {}".format(all_match, win_rate(win_counter, trials)))


if __name__ == "__main__":
    import argparse

    # 引数の指定
    parser = argparse.ArgumentParser()
    parser.add_argument("--first", type=str,
                        default=members()[0], choices=members())
    parser.add_argument("--second", type=str,
                        default=members()[1], choices=members())
    parser.add_argument("--trials", type=int, default=10)
    args = parser.parse_args()

    main(args.first, args.second, args.trials)
