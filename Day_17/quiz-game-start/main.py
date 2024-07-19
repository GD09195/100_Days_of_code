from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank: list = [Question(question['text'], question['answer']) for question in question_data]
quizz_logic = QuizBrain(question_bank)

quizz_logic.next_question()