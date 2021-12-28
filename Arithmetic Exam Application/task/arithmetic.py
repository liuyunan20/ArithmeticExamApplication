import random
import math


def generate_task_l1():
    question = [str(random.randint(2, 9)), random.choice("+-*"), str(random.randint(2, 9))]
    print(" ".join(question))
    return question


def generate_task_l2():
    question = random.randint(11, 29)
    print(question)
    return question


def calculation_l1(user_input):
    x = int(user_input[0])
    oper = user_input[1]
    y = int(user_input[2])
    if oper == "+":
        result = x + y

    elif oper == "-":
        result = x - y

    elif oper == "*":
        result = x * y

    return result


def calculation_l2(num):
    result = math.pow(num, 2)
    return result


def check_answer_format():
    while True:
        try:
            answer = int(input())
        except ValueError:
            print("Incorrect format.")
        else:
            return answer


def choose_level():
    while True:
        print('''Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29''')
        choice = input()
        if choice == "1" or choice == "2":
            return choice
        else:
            print("Incorrect format.")


score = 0
level = choose_level()
if level == "1":
    level_description = "simple operations with numbers 2-9"
    for x in range(5):
        task = generate_task_l1()
        r_answer = calculation_l1(task)
        u_answer = check_answer_format()
        if r_answer == u_answer:
            print("Right!")
            score += 1
        else:
            print("Wrong!")

if level == "2":
    level_description = "integral squares of 11-29"
    for x in range(5):
        task = generate_task_l2()
        r_answer = calculation_l2(task)
        u_answer = check_answer_format()
        if r_answer == u_answer:
            print("Right!")
            score += 1
        else:
            print("Wrong!")
print(f"Your mark is {score}/5. Would you like to save the result? Enter yes or no.")
save_result = input()
if save_result in ["yes", "YES", "y", "Yes"]:
    print("What is your name?")
    user_name = input()
    result_file = open("results.txt", "a")
    result_text = f"{user_name}: {score}/5 in level {level} ({level_description})."
    result_file.write(result_text)
    result_file.close()
    print('The results are saved in "results.txt".')
