# link: https://school.programmers.co.kr/learn/courses/30/lessons/12985


def solution(n, a, b):
    answer = 1
    if a > b:
        a, b = b, a

    while True:
        if b - a == 1 and a % 2 and b % 2 == 0:
            return answer
        if a % 2: a += 1
        if b % 2: b += 1
        a /= 2
        b /= 2
        answer += 1


def print_result():
    TC = [[8, 4, 7]]

    RESULT = [3]

    for i in range(len(TC)):
        answer = solution(*TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
