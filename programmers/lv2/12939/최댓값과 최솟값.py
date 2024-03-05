# link: https://school.programmers.co.kr/learn/courses/30/lessons/12939


def solution(s):
    split_s = list(map(int, s.split()))
    return f"{min(split_s)} {max(split_s)}"


def print_result():
    TC = ["1 2 3 4", "-1 -2 -3 -4", "-1 -1"]

    RESULT = ["1 4", "-4 -1", "-1 -1"]

    for i in range(len(TC)):
        answer = solution(TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
