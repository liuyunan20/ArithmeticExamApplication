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


def check_answer_format():
    while True:
        try:
            answer = int(input())
        except ValueError:
            print("Incorrect format.")
        else:
            return answer


score = 0
for x in range(5):
    task = generate_task()
    r_answer = calculation(task)
    u_answer = check_answer_format()

    if r_answer == u_answer:
        print("Right!")
        score += 1
    else:
        print("Wrong!")
print(f"Your mark is {score}/5.")
