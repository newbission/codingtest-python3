# link: https://school.programmers.co.kr/learn/courses/30/lessons/150370


def solution(today, terms, privacies):
    exp = {key: int(month) * 28 for key, month in (_.split() for _ in terms)}
    y, m, d = map(int, today.split("."))
    today = (28 * 12 * y) + (28 * m) + d
    answer = []

    for i in range(len(privacies)):
        date, term = privacies[i].split()
        y, m, d = map(int, date.split("."))
        date = (y * 28 * 12) + (m * 28) + d + exp[term]
        if date - today <= 0:
            answer.append(i + 1)

    return answer


def print_result():
    TC = [
        [
            "2022.05.19",
            ["A 6", "B 12", "C 3"],
            ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"],
        ],
        [
            "2020.01.01",
            ["Z 3", "D 5"],
            [
                "2019.01.01 D",
                "2019.11.15 Z",
                "2019.08.02 D",
                "2019.07.01 D",
                "2018.12.28 Z",
            ],
        ],
    ]

    RESULT = [[1, 3], [1, 4, 5]]

    for i in range(len(TC)):
        answer = solution(*TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
