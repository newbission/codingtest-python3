# link: https://school.programmers.co.kr/learn/courses/30/lessons/161989


def solution(n, m, section):
    answer = 1
    roll = section[0] + m
    for i in section:
        if i >= roll:
            roll = i + m
            answer += 1
    return answer


def print_result():
    TC = [[8, 4, [2, 3, 6]], [5, 4, [1, 3]], [4, 1, [1, 2, 3, 4]]]

    RESULT = [2, 1, 4]

    for i in range(len(TC)):
        answer = solution(*TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
