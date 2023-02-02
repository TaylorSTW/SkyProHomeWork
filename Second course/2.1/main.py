from functions import read_file, shuffle_word, save, get_top


username = input("Введите свое имя:")
score = 0

for word in read_file():
    answer = input(f"Угадайте слово:{shuffle_word(word)}\n ").lower()
    if answer == word:
        print("Верно! Вы получаете 10 очков.")
        score += 10
    else:
        print(f"Неверно! Верный ответ – {word}.\n")

print(f"{username} - {score}")
save(username, score)

games, max_score = get_top()

print(f"\nВсего игр сыграно: {games}\nМаксимальный рекорд: {max_score}")
