# link: https://school.programmers.co.kr/learn/courses/30/lessons/120841


def solution(dot):
    return [(2, 1), (3, 4)][dot[1] < 0][dot[0] > 0]


def print_result():
    TC = [[2, 4], [-7, 9]]

    RESULT = [1, 2]

    for i in range(len(TC)):
        answer = solution(TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
