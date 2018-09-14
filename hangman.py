# Making a Hangman Game

def initialFigure():
    print("\t_________")
    print("\t|        |")
    print("\t|        |")
    print("\t|        O")
    for i in range(4):
        print("\t|")
        
def firstWrong():
    print("\t_________")
    print("\t|        |")
    print("\t|        |")
    print("\t|        O")
    print("\t|        |")
    for i in range(3):
        print("\t|")

def secondWrong():
    print("\t_________")
    print("\t|        |")
    print("\t|        |")
    print("\t|        O")
    print("\t|       /|")
    for i in range(3):
        print("\t|")

def thirdWrong():
    print("\t_________")
    print("\t|        |")
    print("\t|        |")
    print("\t|        O")
    print("\t|       /|\\")
    for i in range(3):
        print("\t|")

def fourthWrong():
    print("\t_________")
    print("\t|        |")
    print("\t|        |")
    print("\t|        O")
    print("\t|       /|\\")
    print("\t|        |")
    for i in range(2):
        print("\t|")

def fifthWrong():
    print("\t_________")
    print("\t|        |")
    print("\t|        |")
    print("\t|        O")
    print("\t|       /|\\")
    print("\t|        |")
    print("\t|       / ")
    for i in range(2):
        print("\t|")
  
def sixthWrong():
    print("\t_________")
    print("\t|        |")
    print("\t|        |")
    print("\t|        O")
    print("\t|       /|\\")
    print("\t|        |")
    print("\t|       / \\")
    for i in range(2):
        print("\t|")

question = {
    'E_L_PS_': ['c', 'i', 'e'],
    'P_ _H_R_': ['y', 'c', 'a', 'm'],
    'NE_ B_A_S': ['t', 'e', 'n'],
    'S_ _LI_ _': ['u', 'b', 'm', 'e'],
    '_O_ _A': ['k', 'a', 'l']
}

initialFigure()
print("\nWELCOME TO THE HANGMAN GAME\nBe ready to play!!!\n")

mistake = 0

for key, value in question.items():
    correct_guess = len(value) # to extract length of missing letters
    guessed_value = [] # letters that are already guessed
    
    while correct_guess > 0:
        print("====> " + key + " <====")
        answer = input("Guess the missing value: ")
        if answer in value: # check if answer is in the list
            if answer not in guessed_value: # check if the answer is guessed already or not
                guessed_value.append(answer)
                i = value.index(answer) # to get index of correctly guessed answer(position of answer in list)
                print("Your answer is correct. (*o*)")
                print("The letter '{}' lies in {}(th) missing position.\n".format(answer, i + 1))
                correct_guess -= 1
            else:
                print("Please try another letter.\n")
                continue
            
        else:
            mistake += 1
        
            if mistake == 1:
                firstWrong()
                print("Oops! Try Again!\n")
            elif mistake == 2:
                secondWrong()
                print("Oops! Try Again!\n")
            elif mistake == 3:
                thirdWrong()
                print("Oops! Try Again!\n")
            elif mistake == 4:
                fourthWrong()
                print("Oops! Try Again!\n")
            elif mistake == 5:
                fifthWrong()
            elif mistake == 6:
                sixthWrong()
                print("Sorry, You lost the game! (*~*)")
                exit()