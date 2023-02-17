import requests
import json
from quest import Question
from random import shuffle


def load_questions():
    data = requests.get("https://www.jsonkeeper.com/b/MX13")
    json_data = json.loads(data.text)

    questions = []
    for quest in json_data:
        another_question = Question(quest["q"], int(quest["d"]), quest["a"])
        questions.append(another_question)

    shuffle(questions)

    return questions
