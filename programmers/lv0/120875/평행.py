# link: https://school.programmers.co.kr/learn/courses/30/lessons/120875


def solution(dots):
    [x1, y1], [x2, y2], [x3, y3], [x4, y4] = dots
    if (x1 - x2) / (y1 - y2) == (x3 - x4) / (y3 - y4):
        return 1
    if (x1 - x3) / (y1 - y3) == (x2 - x4) / (y2 - y4):
        return 1
    if (x1 - x4) / (y1 - y4) == (x2 - x3) / (y2 - y3):
        return 1
    return 0


def print_result():
    TC = [[[1, 4], [9, 2], [3, 8], [11, 6]], [[3, 5], [4, 1], [2, 4], [5, 10]]]

    RESULT = [1, 0]

    for i in range(len(TC)):
        answer = solution(TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
