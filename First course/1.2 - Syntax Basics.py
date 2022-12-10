points = 0
count = 0
procent = 100
print("Привет! Предлагаю проверить свои знания английского!")
name = input("Расскажи, как тебя зовут! ")
print("Привет, " + name + " ,начинаем тренировку!")
q1 = input("My name ___ Vova  ")
q1 = q1.lower()
if q1 == "is":
  points += 10
  count += 1
  print("Ответ верный!\nВы получаете 10 баллов!")
else:
  print("Неправильно.\nПравильный ответ = is")
  procent = round(procent - 100 / 3, 2)
q2 = input("I ___ a coder  ")
q2 = q2.lower()
if q2 == "am":
  count += 1
  points += 10
  print("Ответ верный!\nВы получаете 10 баллов!")
else:
  print("Неправильно.\nПравильный ответ = am")
  procent = round(procent - 100 / 3, 2)
q3 = input("I live ___ Moscow  ")
q3 = q3.lower()
if q3 == "in":
  count += 1
  points += 10
  print("Ответ верный!\nВы получаете 10 баллов!")
else:
  print("Неправильно.\nПравильный ответ = in")
  procent = round(procent - 100 / 3, 2)

print("Вот и все, " + name + "\nВы ответили на " + str(count) + " вопроса из 3 верно.\nВы заработали " + str(points) + " баллов.\nЭто " + str(procent) + " процентов.")