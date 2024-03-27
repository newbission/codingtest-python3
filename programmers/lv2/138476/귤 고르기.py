# link: https://school.programmers.co.kr/learn/courses/30/lessons/138476


def solution(k, tangerine):
    tan_dict = {i: 0 for i in set(tangerine)}
    for i in tangerine:
        tan_dict[i] += 1
    sorted_tan = sorted(list(tan_dict.items()), key=lambda item: -item[1])

    cnt = 0
    idx = 0
    while cnt < k:
        cnt += sorted_tan[idx][1]
        idx += 1
    return idx


def print_result():
    TC = [
        [6, [1, 3, 2, 5, 4, 5, 2, 3]],
        [4, [1, 3, 2, 5, 4, 5, 2, 3]],
        [2, [1, 1, 1, 1, 2, 2, 2, 3]],
    ]

    RESULT = [3, 2, 1]

    for i in range(len(TC)):
        answer = solution(*TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
