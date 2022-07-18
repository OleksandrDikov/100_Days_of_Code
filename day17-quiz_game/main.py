from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for data in question_data:
    question_bank.append(Question(data["text"], data["answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You`re completed quiz!")
print(f"Your final score was {quiz.user_score}/{quiz.question_number}")
