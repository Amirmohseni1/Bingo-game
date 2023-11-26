from random import randint


class BingoPlayers:
    players = []

    def __init__(self):
        self.name = input('Inter Your name: ')
        self.__quesion = randint(1, 10)
        self.__guess_num = 3
        self.__is_won = False
        self.players.append(self)

    def check_answer(self, answer):
        if answer > self.__quesion:
            print(F'{self.name} Your guess higher')
        elif answer < self.__quesion:
            print(F'{self.name} Your guess lower')
        else:
            print(F'Bingo!!! {self.name} your WIN')
            self.__won_player()
        self.__miss_guess()
        print(F'{self.name}, you have only {self.__guess_num}')

    def __miss_guess(self):
        self.__guess_num -= 1

    def __won_player(self):
        self.__is_won = True

    def __check_won(self):
        pass


class GameControl:
    pass


if __name__ == '__main__':
    while True:
        task = input('Write your task: ')
        match task:
            case 'add':
                BingoPlayers()
            case 'start':
                GameControl()
            case 'exit':
                break
