# link: https://school.programmers.co.kr/learn/courses/30/lessons/42578


def solution(clothes):
    category = {}
    for i, c in clothes:
        if not c in category:
            category[c] = 1
        category[c] += 1
    res = 1
    for n in category.values():
        res *= n
    return res - 1


def print_result():
    TC = [
        [
            ["yellow_hat", "headgear"],
            ["blue_sunglasses", "eyewear"],
            ["green_turban", "headgear"],
        ],
        [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]],
    ]

    RESULT = [5, 3]

    for i in range(len(TC)):
        answer = solution(TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
