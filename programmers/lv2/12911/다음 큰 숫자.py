# link: https://school.programmers.co.kr/learn/courses/30/lessons/12911


def solution(n):
    a = bin(n).count("1")
    for i in range(n + 1, n**2):
        b = bin(i).count("1")
        if a == b:
            return i


def print_result():
    TC = [78, 15]

    RESULT = [83, 23]

    for i in range(len(TC)):
        answer = solution(TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
