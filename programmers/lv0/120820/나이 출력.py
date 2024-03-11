# link: https://school.programmers.co.kr/learn/courses/30/lessons/120820


def solution(age):
    return 2022 - age + 1


def print_result():
    TC = [40, 23]

    RESULT = [1983, 2000]

    for i in range(len(TC)):
        answer = solution(TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")

print_result()