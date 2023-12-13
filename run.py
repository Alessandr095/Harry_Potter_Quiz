import os # import of os module to manipulate files and directories.
import random # for the use of randomising answers.
from questions import questions # importing the questions from questions.py file for declutter.
import logging as # logging module to prevent user errors within the quiz.

qq = questions

#indexes the questions from the questions file, instead of adding the answers by letter to the questions file, for randomisation of answers.
total = len(qq)
indexes = ['A', 'B', 'C', 'D']
score = 0 
q_num = 0

def check_answer(answers, correct, response):
    """Function with if else statment to check if answer is correct or not according to the indexes"""
    global score
    global q_num

    os.system('clear') # clears console for better user interface

    pickedindex = indexes.index(response)
    correctindex = answers.index(correct)

    if pickedindex == correctindex:
        os.system('clear')
        print("Correct!")
        score += 1
    else:
        print("Answer was incorrect")

    input("Press enter to continue")

    q_num += 1

    qq.pop(0)

    
