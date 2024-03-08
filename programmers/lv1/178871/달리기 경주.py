# link: https://school.programmers.co.kr/learn/courses/30/lessons/178871


def solution(players, callings):
    r1 = {player: i for i, player in enumerate(players)}
    r2 = {i: player for i, player in enumerate(players)}
    
    for call in callings:
        rank = r1[call] - 1
        temp = r2[rank]
        r2[rank] = call
        r2[rank + 1] = temp
        r1[call] = rank
        r1[temp] = rank + 1
    answer = [*r2.values()]
    return answer


def print_result():
    TC = [[["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]]]

    RESULT = [["mumu", "kai", "mine", "soe", "poe"]]

    for i in range(len(TC)):
        answer = solution(*TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
