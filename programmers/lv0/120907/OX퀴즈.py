# link: https://school.programmers.co.kr/learn/courses/30/lessons/120907


def solution(quiz):
    answer = []
    for q in quiz:
        q = q.split()
        x, y, z = map(int, (q[0], q[2], q[4]))
        if q[1] == "+":
            answer.append("O" if x + y == z else "X")
        else:
            answer.append("O" if x - y == z else "X")
    return answer


def print_result():
    TC = [
        ["3 - 4 = -3", "5 + 6 = 11"],
        ["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"],
    ]

    RESULT = [["X", "O"], ["O", "O", "X", "O"]]

    for i in range(len(TC)):
        answer = solution(TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
