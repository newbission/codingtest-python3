# link: https://school.programmers.co.kr/learn/courses/30/lessons/76502


def solution(s):
    answer = len(s)
    brackets = {
        "(": 1,
        "{": 2,
        "[": 3,
        "]": -3,
        "}": -2,
        ")": -1,
    }
    a = 0
    for o in s:
        a += brackets[o]
    if a != 0:
        return 0

    for i in range(len(s)):
        l = []
        for o in s:
            if brackets[o] > 0:
                l.append(o)
            elif len(l) == 0 or brackets[o] + brackets[l.pop()] != 0:
                answer -= 1
                break
        s = [*s[1:], s[0]]

    return answer


def print_result():
    TC = ["[](){}", "}]()[{", "[)(]", "}}}"]

    RESULT = [3, 2, 0, 0]

    for i in range(len(TC)):
        answer = solution(TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
