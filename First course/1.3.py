points = 0
count = 0
procent = 100
questions = ["My name ___ Vova", "I ___ a coder", "I live ___ Moscow"]
answers = ["is", "am", "in"]

print('Привет! Предлагаю проверить свои знания английского! Наберите "ready", чтобы начать!')
ready = input()
ready = ready.lower()

if ready == "ready":
    for question in questions:
      print(question)
      answer_user = input("Ответ: ")
      for answer in answers:
          if answer == answer_user:
              points += 10
              count += 1
              print("Ответ верный!\nВы получаете 10 баллов!")
              del answers[0]
              break
          else:
              print("Неправильно.\nПравильный ответ = " + answer)
              procent = round(procent - 100 / 3, 2)
              del answers[0]
              break
else:
    print("Кажется, вы не хотите играть. Очень жаль")
    exit()

print("Вот и все.\nВы ответили на " + str(count) + " вопроса из 3 верно.\nВы заработали " + str(points) + " баллов.\nЭто " + str(procent) + " процентов.")