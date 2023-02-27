import requests
import json
import random
from classes import BasicWord


def load_random_word():
    data = json.loads(requests.get("https://www.jsonkeeper.com/b/OTVF").text)
    random_dict = random.choice(data)
    return BasicWord(random_dict["word"], random_dict["subwords"])