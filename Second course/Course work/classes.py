class BasicWord:
    def __init__(self, word, subwords):
        self.word = word
        self.subwords = subwords

    def __repr__(self):
        return self.word.upper()

    def subwords_count(self):
        return len(self.subwords)

    def check_word(self, user_word):
        if user_word in self.subwords:
            return True
        return False


class Player:
    def __init__(self, name):
        self.name = name
        self.used_words = []

    def __repr__(self):
        return self.name

    def used_coun(self):
        return len(self.used_words)

    def add_word(self, user_word):
        self.used_words.append(user_word)

    def check_used(self, user_word):
        if user_word in self.used_words:
            return True
        return False
