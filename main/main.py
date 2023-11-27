from random import randint


class PlayerAction:
    player_list = []

    def __init__(self):
        self.name = input('Inter Your name: ').strip().lower()
        self.__quesion = randint(1, 10)
        self.__guess_num = 3
        self.__is_won = False
        self.__debug = True
        self.player_list.append(self)

    @classmethod
    def reset_players(cls):
        cls.player_list.clear()

    def debug(self):
        if self.__debug:
            print({self.name, self.__quesion})

    def __str__(self):
        return self.name

    def check_answer(self):
        try:
            answer = int(input(F'{self.name} Pleas, pik number = '))
        except:
            print('pleas inter a number')
            return self.check_answer()

        if answer > self.__quesion:
            print(F'{self.name} Your guess is higher')
        elif answer < self.__quesion:
            print(F'{self.name} Your guess is lower')
        else:
            self.__is_won = True
            print(F'----------- Winner is {self.name} -----------')

        if not self.__is_won:
            self.__miss_guess()
            print(F'{self.name}, you have only {self.__guess_num} guess')
            print(F'---------------------------')

    def __miss_guess(self):
        self.__guess_num -= 1


    @classmethod
    def _game_has_winner(cls):
        for player in cls.player_list:
            if player.__is_won:
                return True


class GameControl:
    def __init__(self):
        while True:
            for player in PlayerAction.player_list:
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
                print(F'{PlayerAction.player_list}, {len(PlayerAction.player_list)}')
            case 'reset':
                PlayerAction.reset_players()
            case 'start':
                GameControl()
            case 'exit':
                break
