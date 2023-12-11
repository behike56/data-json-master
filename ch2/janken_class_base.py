import json
import random
import os


class JankenGame:
    hand_labels = ['グー', 'チョキ', 'パー']

    def __init__(self, save_file):
        self.history_manager = HistoryManager(save_file)

    def play_game(self):
        self.history_manager.load_history()

        while True:
            self.history_manager.show_history()
            if self.janken_round():
                break

    def janken_round(self):
        com = random.randint(0, 2)
        user = self.ask_user_hand()

        if user == 3:
            return True

        print('YOU:', JankenGame.hand_labels[user])
        print('OTHER:', JankenGame.hand_labels[com])

        result = (com - user + 3) % 3
        hantei = 'EVEN'
        if result == 1:
            hantei = 'WIN'
        if result == 2:
            hantei = 'LOSE'

        print('判定:', hantei)

        self.history_manager.add_to_history(com, user, hantei)
        self.history_manager.save_history()

        return False

    def ask_user_hand(self):
        print('---', len(self.history_manager.history), 'times janken ---')
        print('[0]グー [1]チョキ [2]パー [3]終了')
        user = input('どの手をだす？＞')

        try:
            no = int(user)
            if 0 <= no <= 3:
                return no
        except ValueError:
            pass

        return self.ask_user_hand()


class HistoryManager:
    def __init__(self, save_file):
        self.save_file = save_file
        self.history = []

    def load_history(self):
        if os.path.exists(self.save_file):
            with open(self.save_file, encoding='utf-8') as fp:
                self.history = json.load(fp)

    def save_history(self):
        with open(self.save_file, 'w', encoding='utf-8') as fp:
            json.dump(self.history, fp, ensure_ascii=False, indent=2)

    def add_to_history(self, com, user, result):
        self.history.append({'com': com, 'user': user, 'result': result})

    def show_history(self):
        cnt, win = 0, 0
        for i in self.history:
            if i['result'] == 'EVEN':
                continue
            if i['result'] == 'WIN':
                win += 1
            cnt += 1
        r = 0 if cnt == 0 else win / cnt
        print('WIN RATE: {} ({}/{})'.format(r, win, cnt))


if __name__ == '__main__':
    game = JankenGame('janken_history.json')
    game.play_game()
