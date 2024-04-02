# link: https://school.programmers.co.kr/learn/courses/30/lessons/70128


def solution(a, b):
    return sum(aa * bb for aa, bb in zip(a, b))


def print_result():
    TC = [[[1, 2, 3, 4], [-3, -1, 0, 2]], [[-1, 0, 1], [1, 0, -1]]]

    RESULT = [3, -2]

    for i in range(len(TC)):
        answer = solution(*TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
