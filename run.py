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


def run_quiz():
    """
    function run the quiz and 
    once it iterates through all ten questions
    it calls the end card function and displays to the user to return to the main menu 
    """
    global qq
    global score
    global q_num
    global total
    total = len(qq)
    while len(qq) > 0:
        q = qq[0]
        give_question(q)

    if len(qq) == 0:
        score = 0
        q_num = 0
        qq = finished[::-1]

        end_card()
        print('\n')
        input("Press enter to return to main menu.")
        main_menu()


def show_rules():
    """
    function that gives the user an option 
    to view the rules of the quiz with print statments
    """
    os.system('clear')
    print("Rules:\n")
    print("You will be asked a series of questions about Harry Potter.")
    print("You will be presented with 4 possible answers.")
    print("You must enter the letter of the correct answer.")
    print("You will be told if you are correct or not.")
    print("\n")
    option = input("Press enter to return to main menu.")
    main_menu() # calls main menu 


def main_menu():
    """
    a function to for the main menu
    shuffle question randomly for future use of the quiz
    displays the start, rules, exit options
    
    """
    global qq
    global score

    random.shuffle(qq)

    os.system('clear')
    menu = ['Start', 'Rules', 'Exit']
    score = 0
    menustring = ""
    for i, a in enumerate(menu):
        iterator = indexes[i]
        menustring += f"{iterator}. {a}\n"

    print(menustring)

    menuselect = input(f"Please select an option: ").upper()

    if menuselect == "A":
        run_quiz()
    elif menuselect == "B":
        show_rules()
    elif menuselect == "C":
        print("Goodbye!")
        exit()


main_menu()





