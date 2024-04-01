# link: https://school.programmers.co.kr/learn/courses/30/lessons/140108


def solution(s):
    answer = 0
    x = y = 0
    for c in s:
        if x == y:
            answer += 1
            start = c
            x = 1
            y = 0
            continue
        if c == start:
            x += 1
        else:
            y += 1
    return answer


def print_result():
    TC = [
        "banana",
        "abracadabra",
        "aaabbaccccabba",
    ]

    RESULT = [3, 6, 3]

    for i in range(len(TC)):
        answer = solution(TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
