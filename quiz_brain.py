#Asking the questions
#Checking if the answer was correct
#Checking if we're at the end of the quiz

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        quiz_length = len(self.question_list)
        return self.question_number < quiz_length

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        #Each current_question is a dictionary of each question in the question_list list
        user_answer = input(f"{self.question_number}: {current_question.text} (True/False)")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        # Convert both to lowercase just to be safe
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")

