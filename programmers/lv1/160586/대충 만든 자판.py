# link: https://school.programmers.co.kr/learn/courses/30/lessons/160586


def solution(keymap, targets):
    answer = []
    keys = {}
    for key in keymap:
        for i, k in enumerate(key):
            if k not in keys:
                keys[k] = i + 1
                continue

            if keys[k] > i + 1:
                keys[k] = i + 1

    for target in targets:
        cnt = 0
        for c in target:
            if c not in keys:
                cnt = -1
                break
            cnt += keys[c]
        answer.append(cnt)
    return answer


def print_result():
    TC = [
        [["ABACD", "BCEFD"], ["ABCD", "AABB"]],
        [["AA"], ["B"]],
        [["AGZ", "BSSS"], ["ASA", "BGZ"]],
    ]

    RESULT = [[9, 4], [-1], [4, 6]]

    for i in range(len(TC)):
        answer = solution(*TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
