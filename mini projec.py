import time
def wlcome():
    print('welcome to the game').upper()
user_name=input('enter your name')
wlcome()
#rules
def rules():
    print("1.there are 5 questions each questions have 4 options. the score of the each quesions is 1. each quesions have time limit  so you can answer the quesions wihin the time limit otherfise you will lose ")
rules()
#start the game
start=input('start or exit')
#define the question and answer
def quiz():
    questions=[
         "1.Which animal is known as the 'Ship of the Desert?'",
               "2.Which animal is known as the king of the jungle?",
               "3.Name the biggest continent in the world?",
               "4.Which colour symbolises peace?",
               "5.Name the largest planet of our Solar System?"
               ]
    options=[['a.camel','b.ostrich','c.zebra','d.horse'],
             ['a.tiger','b.lion','c.fox','d.cheetaha'],
             ['a.europe','b.asutralia','c.anaritica','d.asia'],
             ['a.white','b.black','c.orange','d.red'],
             ['a.earth','b.venus','c.jupitar','d.mercury']
             ]
    anwers=['a','b','d','a','c']
    score=0
    for i in range(len(questions)):
        print(questions[i])
        for j in range(len(options)):
              print(j[i])
        start_time=time.time()
        time_limit=10
        user=input(f'choose an option (a,b,c,d) within the {time_limit}')
        end_time=time.time()-start_time

