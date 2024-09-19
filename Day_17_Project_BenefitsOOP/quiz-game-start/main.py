from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank: list = [Question(question['question'], question['correct_answer']) for question in question_data]
quizz_logic = QuizBrain(question_bank)

while quizz_logic.still_has_questions():

    quizz_logic.next_question()

print("You've complete the quizz")
print(f"Your final score is {quizz_logic.score} / {quizz_logic.question_number}")