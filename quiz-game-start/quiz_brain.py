class QuizBrain:
    def __init__(self, list):
        self.question_num = 0
        self.score = 0
        self.question_list = list

    def still_has_questions(self):
        return self.question_num<len(self.question_list)

    def next_question(self):
        curr_question = self.question_list[self.question_num]
        self.question_num +=1
        user_answer = input(f"{self.question_num}. {curr_question.text} True/False")
        self.checkanswer(user_answer, curr_question.answer)

    def checkanswer(self,user_answer,ques_answer):
        if user_answer.lower() == ques_answer.lower():
            print("Correct")
            self.score+=1
        else:
            print("Incorrect")
            print(f"The correct answer is {ques_answer}")
        print(f"Your current score was: {self.score}/{self.question_num}")


