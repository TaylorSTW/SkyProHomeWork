words_easy = {
    "family":"семья",
    "hand": "рука",
    "people":"люди",
    "evening": "вечер",
    "minute":"минута",
}

words_medium = {
    "believe":"верить",
    "feel": "чувствовать",
    "make":"делать",
    "open": "открывать",
    "think":"думать",
}

words_hard = {
    "rural":"деревенский",
    "fortune": "удача",
    "exercise":"упражнение",
    "suggest": "предлагать",
    "except":"кроме",
}

levels = {
   0: "Нулевой",
   1: "Так себе",
   2: "Можно лучше",
   3: "Норм",
   4: "Хорошо",
   5: "Отлично",
}

answers = {}

diff = input("Выбери уровень сложности:\nлегкий, средний, сложный\n").lower()
diff_levels = {
    "легкий":words_easy,
    "средний":words_medium,
    "сложный":words_hard
}
while True:
    diff = input("Выбери уровень сложности:\nлегкий, средний, сложный\n").lower()
    if diff in diff_levels:
        words = diff_levels[diff]
        break
    else:
        print("Такого уровня сложности нет")

for key, value in words.items():
    print(f"\n{key}, {len(value)} Букв, первая {value[0]}")
    answer = input("Ответ: ")
    if answer == value:
        print(f"Верно {key} - это {value}")
        answers[key] = True
    else:
        print(f"Неверно {key} - это {value}")
        answers[key] = False

count = 0
print("\nПравильно отвечены слова:\n")
for key, value in answers.items():
    if value is True:
        count += 1
        print(key)

print("\nНеправильно отвечены слова:\n")
for key, value in answers.items():
    if value is False:
        print(key)

print("Ваш ранг:")
print(levels[count])