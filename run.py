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
    """
    Function with if else statment to check
    if answer is correct or not according to the indexes
    
    """
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


def give_question(ques):
    """ 
    prints current score.
    it shuffles the answers randomly with random module
    checks if user has put in correct letter
    if not print choice of correct answers(indexes)
    user input but pressing enter take user to next question
    """
    global score # for score to work globally throughout the code
    os.system('clear')

    print(f'Score: {score}\n')

    print(f'Question {q_num + 1}')

    question = ques["question"]

    answers = ques["answer"]
    random.shuffle(answers)

    correct = ques["correct_answer"]

    print(question)

    astring = ""
    for i, a in enumerate(answers):
        iterator = indexes[i]
        astring += f"{iterator}. {a}\n"

    print(astring)

    response = input("Please enter the correct letter: ").upper()

    if response in indexes:
        check_answer(answers, correct, response)
    else:
        os.system('clear')
        print("Please enter a valid answer (A, B, C or D)")
        input("Press enter to continue")


def end_card():
    """
    end_card function to display to the user 
    their incremented score of the total answers
    """
    os.system('clear')
    print("🏆🏆🏆")
    print(f"You have finished the quiz!\nYour final score was {score}/{total}")





