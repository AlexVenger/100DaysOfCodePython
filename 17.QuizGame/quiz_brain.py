class Quiz:
    def __init__(self, questions_list):
        self.questions_list = questions_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        answer = input(f"Q.{self.question_number}: {self.questions_list[self.question_number].text} (True/False)?:")
        self.check_answer(answer)
        self.question_number += 1

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def check_answer(self, answer):
        if self.questions_list[self.question_number].answer == answer:
            print("You got it right!")
            self.score += 1
        else:
            print("Oh no, that's wrong!")
        print(f"The correct answer is {self.questions_list[self.question_number].answer}")
        print(f"Your score is {self.score}/{self.question_number + 1}")
        print()

