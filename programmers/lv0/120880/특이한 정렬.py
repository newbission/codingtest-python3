# link: https://school.programmers.co.kr/learn/courses/30/lessons/120880


def solution(numlist, n):
    return sorted(numlist, key=lambda i: (abs(n - i), n - i))


def print_result():
    TC = [[[1, 2, 3, 4, 5, 6], 4], [[10000, 20, 36, 47, 40, 6, 10, 7000], 30]]

    RESULT = [[4, 5, 3, 6, 2, 1], [36, 40, 20, 47, 10, 6, 7000, 10000]]

    for i in range(len(TC)):
        answer = solution(*TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
