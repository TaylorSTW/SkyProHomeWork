import random


def read_file():
    with open("words.txt", "r") as file:
        words = file.read().splitlines()
        random.shuffle(words)
        return words


def shuffle_word(word):
    list_word = list(word)
    random.shuffle(list_word)
    shuffled = "".join(list_word)
    return shuffled


def save(name, score):
    with open("hystory.txt", "a") as file:
        file.write(f"\n{name} {score}")


def get_top():
    with open("hystory.txt", "r") as file:
        score_list = []
        for line in file:
            score_list.append(int(line.split(' ')[-1]))

    return len(score_list), max(score_list)
