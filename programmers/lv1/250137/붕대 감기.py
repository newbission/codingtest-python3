# link: https://school.programmers.co.kr/learn/courses/30/lessons/250137


def solution(bandage, health, attacks):
    t, x, y = bandage
    current_health = health
    time = attacks[0][0] 

    for atk_time, damage in attacks:
        time_diff = atk_time - time
        recovery = (time_diff // t * y) + (time_diff * x)
        current_health = min(health, current_health + recovery) - damage
        if current_health <= 0:
            return -1
        time = atk_time + 1
    return current_health


def print_result():
    TC = [
        [[5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]]],
        [[3, 2, 7],	20,	[[1, 15], [5, 16], [8, 6]]],
        [[4, 2, 7],	20,	[[1, 15], [5, 16], [8, 6]]],
        [[1, 1, 1],	5,	[[1, 2], [3, 2]]]
    ]

    RESULT = [5, -1, -1, 3]

    for i in range(len(TC)):
        answer = solution(TC[i][0], TC[i][1], TC[i][2])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
