# link: https://school.programmers.co.kr/learn/courses/30/lessons/12931


def solution(n):
    answer = 0
    while n:
        answer += n % 10
        n //= 10
    return answer


def print_result():
    TC = [123, 987]

    RESULT = [6, 24]

    for i in range(len(TC)):
        answer = solution(TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
