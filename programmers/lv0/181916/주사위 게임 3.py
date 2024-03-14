# link: https://school.programmers.co.kr/learn/courses/30/lessons/181916


def solution(a, b, c, d):
    dice = set([a, b, c, d])
    dice_dict = {key: 0 for key in dice}
    dice_dict[a] += 1
    dice_dict[b] += 1
    dice_dict[c] += 1
    dice_dict[d] += 1

    size = len(dice)

    if size == 1:
        return 1111 * a

    if size == 2:
        a, b = dice
        if dice_dict[a] == 2:
            return (a + b) * abs(a - b)
        p, q = [a, b] if dice_dict[a] == 3 else [b, a]
        return (10 * p + q) ** 2

    if size == 3:
        a, b, c = dice
        q, r = [a, b] if dice_dict[c] == 2 else [a, c] if dice_dict[b] == 2 else [b, c]
        return q * r

    return min(dice)


def print_result():
    TC = [
        [2, 2, 2, 2],
        [4, 1, 4, 4],
        [6, 3, 3, 6],
        [2, 5, 2, 6],
        [6, 4, 2, 5],
    ]

    RESULT = [2222, 1681, 27, 30, 2]

    for i in range(len(TC)):
        answer = solution(*TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
