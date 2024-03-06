# link: https://school.programmers.co.kr/learn/courses/30/lessons/12937


def solution(num):
    return "Even" if num % 2 == 0 else "Odd"

solution = lambda num: "Even" if num % 2 == 0 else "Odd"

def print_result():
    TC = [3, 4]

    RESULT = ["Odd", "Even"]

    for i in range(len(TC)):
        answer = solution(TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
