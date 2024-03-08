# link: https://school.programmers.co.kr/learn/courses/30/lessons/12909


def solution(s):
    cnt = 0
    for c in s:
        if c == "(":
            cnt += 1
        else:
            cnt -= 1

        if cnt < 0:
            return False

    return False if cnt else True


def print_result():
    TC = [
        "()()",
        "(())()",
        ")()(",
        "(()(",
    ]

    RESULT = [True, True, False, False]

    for i in range(len(TC)):
        answer = solution(TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
