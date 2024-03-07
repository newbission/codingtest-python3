# link: https://school.programmers.co.kr/learn/courses/30/lessons/12944


def solution(arr):
    return sum(arr) / len(arr)


def print_result():
    TC = [[1, 2, 3, 4, 5], [5, 5]]

    RESULT = [3, 5]

    for i in range(len(TC)):
        answer = solution(TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
