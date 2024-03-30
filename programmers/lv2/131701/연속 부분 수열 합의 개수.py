# link: https://school.programmers.co.kr/learn/courses/30/lessons/131701


def solution(elements):
    res = []
    l = len(elements)
    elements += elements
    for i in range(1, l+1):
        for j in range(l):
            res.append(sum(elements[j:j+i]))
    return len(set(res))


def print_result():
    TC = [[7,9,1,1,4]]

    RESULT = [18]

    for i in range(len(TC)):
        answer = solution(TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")

print_result()