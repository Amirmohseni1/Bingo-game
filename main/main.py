from random import randint


class PlayerAction:
    players = []

    def __init__(self):
        self.name = input('Inter Your name: ').strip().lower()
        self.__quesion = randint(1, 10)
        self.__guess_num = 3
        self.__is_won = False
        self.__debug = True
        self.players.append(self)

    @classmethod
    def reset_players(cls):
        cls.players.clear()

    def check_answer(self):
        answer = int(input(F'{self.name} Pleas, pik number = '))
        if type(answer) == int:
            if answer > self.__quesion:
                print(F'{self.name} Your guess higher')
            elif answer < self.__quesion:
                print(F'{self.name} Your guess lower')
            else:
                self.__won_player()
                return self.winner()
            self.__miss_guess()
            print(F'{self.name}, you have only {self.__guess_num}')
            print(F'---------------------------')
        else:
            print('pleas inter a number')
            return self.check_answer()

    def debug(self):
        if self.__debug:
            print({self.name, self.__quesion})

    def __miss_guess(self):
        self.__guess_num -= 1

    def __won_player(self):
        self.__is_won = True

    def winner(self):
        print(F'----------- Winner is {self.name} -----------')

    @classmethod
    def _game_has_winner(cls):
        for player in cls.players:
            if player.__is_won:
                return True

    def __str__(self):
        return self.name


class GameControl:
    def __init__(self):
        while True:
            for player in PlayerAction.players:
                if not player._game_has_winner():
                    player.debug()
                    player.check_answer()
                else:
                    break


if __name__ == '__main__':
    while True:
        print('add, reset, start, exit, list')
        task = input('Write your task: ').strip().lower()
        match task:
            case 'add':
                PlayerAction()
            case 'list':
                print(F'{PlayerAction.players}, {len(PlayerAction.players)}')
            case 'reset':
                PlayerAction.reset_players()
            case 'start':
                GameControl()
            case 'exit':
                break
