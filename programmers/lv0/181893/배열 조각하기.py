# link: https://school.programmers.co.kr/learn/courses/30/lessons/181893


def solution(arr, query):
    for idx, i in enumerate(query):
        if idx % 2 == 0:
            arr = arr[: i + 1]
        else:
            arr = arr[i:]
    return arr


def print_result():
    TC = [[[0, 1, 2, 3, 4, 5], [4, 1, 2]]]

    RESULT = [[1, 2, 3]]

    for i in range(len(TC)):
        answer = solution(*TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
