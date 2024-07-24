class QuizBrain:
    def __init__(self, new_question_list):
        self.question_number = 0
        self.question_list = new_question_list
        self.score = 0

    def next_question(self):

        following_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {following_question.question} (True/False): ").lower()
        self.check_answer(answer, following_question.answer)

    def still_has_questions(self) -> bool:
        return self.question_number != len(self.question_list)

    def check_answer(self, user_answer, question_answer):
        if user_answer.lower() == question_answer.lower():
            self.score += 1
            print("Correct answer")
        else:
            print("Incorrect answer")

        print(f"Your current score is {self.score} / {self.question_number}\n")



