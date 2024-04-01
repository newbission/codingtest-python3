# link: https://school.programmers.co.kr/learn/courses/30/lessons/131127


def solution(want, number, discount):
    want_d = {key: i for i, key in enumerate(want)}
    answer = 0
    for i in range(len(discount) - 9):
        temp = [*number]
        cnt = 0
        for d in discount[i : i + 10]:
            if d not in want_d:
                break
            if not temp[want_d[d]]:
                break
            temp[want_d[d]] -= 1
            cnt += 1
        if cnt == 10:
            answer += 1
    return answer


def print_result():
    TC = [
        [
            ["banana", "apple", "rice", "pork", "pot"],
            [3, 2, 2, 2, 1],
            [
                "chicken",
                "apple",
                "apple",
                "banana",
                "rice",
                "apple",
                "pork",
                "banana",
                "pork",
                "rice",
                "pot",
                "banana",
                "apple",
                "banana",
            ],
        ],
        [
            ["apple"],
            [10],
            [
                "banana",
                "banana",
                "banana",
                "banana",
                "banana",
                "banana",
                "banana",
                "banana",
                "banana",
                "banana",
            ],
        ],
    ]

    RESULT = [3, 0]

    for i in range(len(TC)):
        answer = solution(*TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
