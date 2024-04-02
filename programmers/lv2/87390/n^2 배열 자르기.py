# link: https://school.programmers.co.kr/learn/courses/30/lessons/87390


def solution(n, left, right):
    return [max(i // n, i % n) + 1 for i in range(left, right + 1)]


def print_result():
    TC = [[3, 2, 5], [4, 7, 14]]

    RESULT = [[3, 2, 2, 3], [4,3,3,3,4,4,4,4]]

    for i in range(len(TC)):
        answer = solution(*TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
