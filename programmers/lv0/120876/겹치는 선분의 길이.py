# link: https://school.programmers.co.kr/learn/courses/30/lessons/120876


def solution(lines):
    answer = 0
    arr = [0] * 202
    for a, b in lines:
        for i in range(a+100, b+100):
            arr[i] += 1
    
    for i in arr:
        if i > 1:
            answer += 1
    return answer

    return sum(1 for i in arr if i > 1)


def print_result():
    TC = []

    RESULT = []

    for i in range(len(TC)):
        answer = solution(TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")

print_result()