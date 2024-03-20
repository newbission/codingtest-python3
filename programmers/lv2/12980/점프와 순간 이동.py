# link: https://school.programmers.co.kr/learn/courses/30/lessons/12980


def solution(n):
    q = [(0, 0)]
    i = 0
    while True:
        k, c = q[i]
        a, b = k * 2, k + 1
        if a == n:
            return c
        elif b == n:
            return c + 1
        q.append((a,c))
        q.append((b,c+1))

        i += 1



def print_result():
    TC = [5, 6, 5000]

    RESULT = [2, 2, 5]

    for i in range(len(TC)):
        answer = solution(TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")

print_result()