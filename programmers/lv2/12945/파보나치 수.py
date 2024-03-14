# link: https://school.programmers.co.kr/learn/courses/30/lessons/12945


def solution(n):
    f = [None] * (n + 1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n + 1):
        f[i] = (f[i-1] + f[i-2]) % 1234567
    
    return f[n]


def print_result():
    TC = [3, 5]

    RESULT = [2, 5]

    for i in range(len(TC)):
        answer = solution(TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")

print_result()