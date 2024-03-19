# link: https://school.programmers.co.kr/learn/courses/30/lessons/120924


def solution(common):
    if common[2] - common[1] == common[1] - common[0]:
        return common[-1] + (common[2] - common[1])

    return common[-1] * (common[2] / common[1])


def print_result():
    TC = [[1, 2, 3, 4], [2, 4, 8]]

    RESULT = [5, 16]

    for i in range(len(TC)):
        answer = solution(TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
