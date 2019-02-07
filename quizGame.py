# Making a Quiz Game


import json
import random

# to deduct any two wrong answers. Parameters to receive question dictionary ani rightAnswer count
def choice_fifty_fifty(question_dict, rightAnswer):
    # to hold key of every option (answer)
    key_list = []
    c_ans = question_dict['ca'] # correct answer

    for key in question_dict.keys():
        key_list.append(key)
        if key == c_ans:
            correctAns = c_ans

    # to remove the last key ('ca') that is not needed
    key_list.pop(5)
    # to remove the first key ('q') that is not needed
    key_list.pop(0)

    # to generate a random option
    while True:
        # choose one of the wrong answer randomly
        rand_wrong_choice = random.choice(key_list)

        if rand_wrong_choice == c_ans:
            continue
        else:
            break

    # compare the ascii value of keys to display options in correct order
    if ord(correctAns) < ord(rand_wrong_choice):
        print("\n{}) {}\n{}) {}\n".format(correctAns, question_dict[correctAns], rand_wrong_choice, question_dict[rand_wrong_choice]))
        answer = input("\nEnter your answer here ({}/{}) : ".format(correctAns, rand_wrong_choice))
    else:
        print("\n{}) {}\n{}) {}\n".format(rand_wrong_choice, question_dict[rand_wrong_choice], correctAns, question_dict[correctAns]))
        answer = input("\nEnter your answer here ({}/{}) : ".format(rand_wrong_choice, correctAns))


    if question_dict['ca'] == answer:
        print("Correct answer.\t +10 points")
        print("------------------------------------------------------")
        rightAnswer += 1

    else:
        print("\nYour answer is wrong.")
        print("Correct answer is '{}'.".format(question_dict['ca']))
        print("------------------------------------------------------")

    return rightAnswer


with open("quizQues.json", "r") as qa:
    # read json file
    questionSet = qa.read()
    # load content of file in list form
    questionList = json.loads(questionSet)
    rightAnswer = 0
    player_name = input("Enter your name: ")

    print("WELCOME {}, be ready for your questions\n".format(player_name))

    for i in range(len(questionList)):
        # access the first item of list (first question of quiz)
        question_dict = questionList[i]

        # print question
        print("\n{questionNo}.  {question}".format(questionNo = i+1, question = question_dict['q']))
        # print options
        print(" a) {}\n b) {}\n c) {}\n d) {}".format(question_dict['a'], question_dict['b'], question_dict['c'], question_dict['d']))
        print("\nLifelines: \n1) 50/50")

        answer = input("\nEnter your choice here (a/b/c/d)/(1) : ")

        if question_dict['ca'] == answer:
            print("Correct answer.\t +10 points")
            print("------------------------------------------------------")
            rightAnswer += 1

        # user asks for 50/50 lifeline
        elif answer == '1':
            rightAnswer = choice_fifty_fifty(question_dict, rightAnswer)

        else:
            print("\nYour answer is wrong.")
            print("Correct answer is '{}'.".format(question_dict['ca']))
            print("------------------------------------------------------")
        #os.system('cls')

    else:
        print("\nGame Over!!!")
        print("You made {} right. Your score is {} out of 100\n".format(rightAnswer, str(rightAnswer*10)))


with open("record.txt", "a") as f:
    f.write("Name = {}\t Score = {}\n".format(player_name, str(rightAnswer*10)))

choice = input("Do yo want us to show the dashboard? (y/n)")
if choice == 'y':
    with open("record.txt", "r") as f:
        print(f.read())
