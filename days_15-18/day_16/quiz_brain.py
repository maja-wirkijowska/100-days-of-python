class QuizBrain:
    def __init__(self, q_list):
        self.question_num = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_num]
        self.question_num += 1
        user_answer = input(f"Q{self.question_num}: {current_question.text} (True/False): ").lower()
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions_remaining(self):
        return self.question_num < len(self.question_list)

    def check_answer(self, user_a, correct_a):
        if user_a.lower() == correct_a.lower():
            print("Correct")
            self.score += 1
        else:
            print("Incorrect")
            print(f"The correct answer is: {correct_a}")
        print(f"Current score: {self.score}/{self.question_num}\n")
