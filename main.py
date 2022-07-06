from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_list = []

for data in question_data:
    question_text = data["question"]
    question_answer = data["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_list.append(new_question)

quiz = QuizBrain(question_list)

while quiz.still_has_questions():
    quiz.next_question()

print("You have come to the end of the quiz")
print(f"Your score is: {quiz.score}/{quiz.question_number}")
