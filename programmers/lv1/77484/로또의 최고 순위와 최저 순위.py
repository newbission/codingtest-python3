# link: https://school.programmers.co.kr/learn/courses/30/lessons/77484


def solution(lottos, win_nums):
    z = lottos.count(0)
    cnt = 7
    lottos.sort()
    for i in lottos[z:]:
        if i in win_nums:
            cnt -= 1

    return [min(6, cnt - z), min(6, cnt)]


def print_result():
    TC = [
        [[44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]],
        [[0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]],
        [[45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]],
    ]

    RESULT = [[3, 5], [1, 6], [1, 1]]

    for i in range(len(TC)):
        answer = solution(*TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
