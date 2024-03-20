# link: https://school.programmers.co.kr/learn/courses/30/lessons/120812


def solution(array):
    arr = [[i, 0] for i in range(1000)]

    for i in array:
        arr[i][1] += 1

    arr.sort(key=lambda a: a[1], reverse=True)

    return arr[0][0] if arr[0][1] != arr[1][1] else -1


def print_result():
    TC = []

    RESULT = []

    for i in range(len(TC)):
        answer = solution(TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
