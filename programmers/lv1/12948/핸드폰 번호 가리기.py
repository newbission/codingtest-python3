# link: https://school.programmers.co.kr/learn/courses/30/lessons/12948


def solution(phone_number):
    return "*" * (len(phone_number) - 4) + phone_number[-4:]


def print_result():
    TC = ["01033334444", "027778888"]

    RESULT = ["*******4444", "*****8888"]

    for i in range(len(TC)):
        answer = solution(TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
