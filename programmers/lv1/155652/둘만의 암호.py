# link: https://school.programmers.co.kr/learn/courses/30/lessons/155652


def solution(s, skip, index):
    alpha = [chr(i) for i in range(97, 97 + 26) if chr(i) not in skip]
    answer = ""
    for c in s:
        answer += alpha[(alpha.index(c) + index) % len(alpha)]

    return answer


def print_result():
    TC = [["aukks", "wbqd", 5]]

    RESULT = ["happy"]

    for i in range(len(TC)):
        answer = solution(*TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
