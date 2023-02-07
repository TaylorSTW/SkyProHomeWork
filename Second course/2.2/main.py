from  functions import get_student_by_pk, get_profession_by_title, check_fitness


while True:
    stu_pk = input("Введите номер студента: ")
    if stu_pk.isdigit():
        student = get_student_by_pk(int(stu_pk))
        if student:
            prof_title = input("Введите название профессиии ").title()
            profession = get_profession_by_title(prof_title)
            if profession:
                fitness = check_fitness(student, profession)
                print(f'Пригодность:{fitness["percent"]}')
                print(f'{student["full_name"]} знает {", ".join(fitness["has"])}% ') if len(fitness["has"]) != 0 \
                    else print(f'{student["full_name"]} не владеет нужными скиллами')
                print(f'{student["full_name"]} не знает {", ".join(fitness["lacks"])}') if len(fitness["lacks"]) != 0 \
                    else print(f'{student["full_name"]} знает все, что необходимо')
                break
            else:
                print("Такой профессии нет!")
        else:
            print("Такого студента нет!")
            break

