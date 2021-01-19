from data import question_data
class Question:
    def __init__(self,  qu,a):
        
        self.qu=qu
        self.a=a
class QuestionBrain:
    def __init__(self,question_number,questions,score):
        self.question_number=0
        self.questions=questions
        self.score=0
    def still_question(self):
        if self.question_number!=len(self.questions):
            return True
    def next_question(self):
       current_question=self.questions[self.question_number]
       
       self.question_number+=1
       cho=input(f"Q{self.question_number}. {current_question.qu } (True/False):").lower()
       if cho==current_question.a.lower():
           self.score+=1
           
           print(f"That's right\nThe correct answer was: {current_question.a}\nYour current score is: {self.score}/{self.question_number}")
       else:
           print(f"That's wrong\nThe correct answer was: {current_question.a}\nYour current score is: {self.score}/{self.question_number}")
        
                      
questions=[]

for i in range(0,len(question_data)-1):
    questions.append(Question(question_data[i]["text"],question_data[i]["answer"]))

quizz=QuestionBrain(0,questions,0)
while quizz.still_question():
    quizz.next_question()
