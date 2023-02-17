from utils import load_questions


def main():
    questions = load_questions()
    for question in questions:
        print(question.build_question())
        answer = input("Ответ: ").lower()

        question.is_asked = True
        question.user_answer = answer

        print(question.build_feedback())


main()