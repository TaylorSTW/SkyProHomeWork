import json


def load_students():
    with open("students.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def load_professions():
    with open("professions.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def get_student_by_pk(pk):
    students = load_students()
    for student in students:
        if student["pk"] == pk:
            return student


def get_profession_by_title(title):
    professions = load_professions()
    for profession in professions:
        if profession["title"] == title:
            return profession


def check_fitness(student, profession):
    student_skills = set(student["skills"])
    profession_skills = set(profession["skills"])

    has = student_skills.intersection(profession_skills)
    lacks = student_skills.difference(profession_skills)
    percents = len(has) / len(profession_skills) * 100

    return {
        "has": has,
        "lacks": lacks,
        "percent": percents
    }