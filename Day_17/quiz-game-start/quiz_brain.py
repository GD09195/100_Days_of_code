class QuizBrain:
    def __init__(self, new_question_list):
        self.question_number = 0
        self.question_list = new_question_list

    def next_question(self):

        following_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {following_question.question} (True/False): ").lower()

        if answer == following_question.answer.lower():
            print("Correct answer")
        else:
            print("incorrect answer")



