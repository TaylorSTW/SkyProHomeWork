from classes import Player
from utils import load_random_word


def main():
    user_name = input("Ввведите имя игрока:\n")
    player = Player(user_name)
    words = load_random_word()
    print(f"Привет, {player}")
    print(f"Составьте {words.subwords_count()} слов из слова {words}")
    print('''Слова должны быть не короче 3 букв
Чтобы закончить игру, угадайте все слова или напишите "stop"
Поехали, ваше первое слово?\n''')

    while player.used_coun() != words.subwords_count():
        user_answer = input()

        if user_answer != "stop":
            if len(user_answer) < 3:
                print("Cлишком короткое слово")
                continue
            elif player.check_used(user_answer):
                print("Уже использовано")
                continue
            elif words.check_word(user_answer):
                print("Верно")
                player.add_word(user_answer)
            else:
                print("Неверно")
        else:
            break

    print(f"Игра завершена, вы угадали {player.used_coun()} слов!")


main()