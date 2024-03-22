# link: https://school.programmers.co.kr/learn/courses/30/lessons/76501


def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        answer += absolutes[i] if signs[i] else -absolutes[i]
    return answer


def print_result():
    TC = [[[4, 7, 12], [True, False, True]], [[1, 2, 3], [False, False, True]]]

    RESULT = [9, 0]

    for i in range(len(TC)):
        answer = solution(*TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
