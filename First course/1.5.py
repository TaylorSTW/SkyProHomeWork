import random


def get_word(list_):
  return random.choice(list_)

def morse_encode(word):
  morse = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "...-....",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--",
    "h": "....",
    "i": "...",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "...",
    "o": "---",
    "p": "......",
    "q": "....-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
  }
  morse_word = " "
  for symb in word:
    morse_word += morse[symb] + ""
  return morse_word

def print_statistics(answers):
  print(f"Всего задачек: {len(answers)}")
  print(f"Отвечено верно: {answers.count(True)}")
  print(f"Отвечено неверно: {answers.count(False)}")

answers = []
words_list = ["code", "bit", "list", "soul", "next"]

print("""Сегодня мы потренируемся расшифровывать морзянку.
Нажмите Enter и начнем""")
input()


for _ in range(5):
  word = get_word(words_list)
  print("Какое слово загадано?" + morse_encode(word) + " ")
  answer = input().lower()
  if answer == word:
    count = True
    answers.append(count)
    print("Ответ верный!")
  else:
    count = False
    answers.append(count)
    print("Ответ неверный!")

print_statistics(answers)

