# link: https://school.programmers.co.kr/learn/courses/30/lessons/120921


def solution(A, B):
    cnt = 0
    while cnt < len(A) and A != B:
        cnt += 1
        A = A[-1] + A[:-1]

    return cnt if cnt != len(A) else -1


def print_result():
    TC = [["hello", "ohell"], ["apple", "elppa"], ["atat", "tata"], ["abc", "abc"]]

    RESULT = [1, -1, 1, 0]
    for i in range(len(TC)):
        answer = solution(*TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
