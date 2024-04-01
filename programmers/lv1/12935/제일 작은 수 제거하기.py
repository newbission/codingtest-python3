# link: https://school.programmers.co.kr/learn/courses/30/lessons/12935


def solution(arr):
    m = min(arr)
    return [n for n in arr if n != m] or [-1]


def print_result():
    TC = [[4, 3, 2, 1], [10]]

    RESULT = [[4, 3, 2], [-1]]

    for i in range(len(TC)):
        answer = solution(TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
