class Question:

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


new_q = Question("John", "is my name!")

print(new_q.answer)
