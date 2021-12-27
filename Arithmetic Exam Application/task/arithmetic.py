import random


def generate_task():
    user_input = [str(random.randint(2, 9)), random.choice("+-*"), str(random.randint(2, 9))]
    print(" ".join(user_input))
    return user_input


def calculation(user_input):
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


task = generate_task()
r_answer = calculation(task)
u_answer = int(input())
if r_answer == u_answer:
    print("Right!")
else:
    print("Wrong!")
