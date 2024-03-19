# link: https://school.programmers.co.kr/learn/courses/30/lessons/118666


def solution(survey, choices):
    indicator = ["RT", "CF", "JM", "AN"]
    score = {key: 0 for key in ["R", "T", "C", "F", "J", "M", "A", "N"]}
    for i in range(len(survey)):
        s = survey[i]
        c = choices[i]
        if c < 4:
            score[s[0]] += abs(c - 4)
        elif c > 4:
            score[s[1]] += c - 4

    answer = ""
    for i in indicator:
        a, b = list(i)
        answer += a if score[a] >= score[b] else b

    return answer


def print_result():
    TC = [
        [["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]],
        [["TR", "RT", "TR"], [7, 1, 3]],
    ]

    RESULT = ["TCMA", "RCJA"]

    for i in range(len(TC)):
        answer = solution(*TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
