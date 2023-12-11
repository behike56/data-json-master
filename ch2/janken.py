import json
import random
import os

save_file: str = 'janken_history.json'
history = []
hand_labels = ['グー', 'チョキ', 'パー']


def main():
    load_history(save_file)

    while True:
        show_history()
        flagStop = janken_game()
        if flagStop:
            break


def janken_game() -> bool:
    com = random.randint(0, 2)
    user = ask_user_hand()

    if user == 3:
        return True

    print('YOU:', hand_labels[user])
    print('OTHER:', hand_labels[com])

    result = (com - user + 3) % 3
    hantei = 'EVEN'

    if result == 1:
        hantei = 'WIN'

    if result == 2:
        hantei = 'LOSE'

    print('判定:', hantei)

    history.append({'com': com, 'user': user, 'result': hantei})
    save_history(save_file)

    return False


def load_history(savefile: str) -> None:
    """
        プレイ履歴をファイルから読み込む
    Args:
        savefile (str): ファイルパス
    """

    global history
    if os.path.exists(savefile):
        with open(savefile, encoding='utf-8') as fp:
            history = json.load(fp)


def save_history(savefile: str) -> None:
    """勝敗の履歴をファイルへ保存
    """

    with open(savefile, 'w', encoding='utf-8') as fp:
        json.dump(history, fp, ensure_ascii=False, indent=2)


def show_history() -> None:
    cnt, win = 0, 0
    for i in history:
        if i['result'] == 'EVEN':
            continue

        if i['result'] == 'WIN':
            win += 1

        cnt += 1

    r = 0 if cnt == 0 else win / cnt
    print('WIN RATE: {} ({}/{})'.format(r, win, cnt))


def ask_user_hand() -> int:
    """
    """

    print('---', len(history), 'times janken ---')
    print('[0]グー [1]チョキ [2]パー [3]終了')

    user = input('どの手をだす？＞')

    try:
        no = int(user)
        if 0 <= no <= 3:
            return no

    except:
        pass

    return ask_user_hand()


if __name__ == '__main__':
    main()
