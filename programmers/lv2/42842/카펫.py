# link: https://school.programmers.co.kr/learn/courses/30/lessons/42842


def solution(brown, yellow):
    s = brown + yellow
    for i in range(1, s // 2):
        j = s / i
        if j % 1 == 0 and (i + j) * 2 - 4 == brown:
            return [j, i]


def print_result():
    TC = [[10, 2], [8, 1], [24, 24]]

    RESULT = [[4, 3], [3, 3], [8, 6]]

    for i in range(len(TC)):
        answer = solution(*TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
