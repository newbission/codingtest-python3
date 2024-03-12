# link: https://school.programmers.co.kr/learn/courses/30/lessons/120866


def solution(board):
    direction = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    cnt_zero = 0
    bomb = []
    n = len(board)

    for y in range(n):
        for x in range(n):
            if board[y][x]:
                bomb.append((y, x))
            else:
                cnt_zero += 1

    for y, x in bomb:
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < n and board[ny][nx] == 0:
                board[ny][nx] = -1
                cnt_zero -= 1

    return cnt_zero


def print_result():
    TC = [
        [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
        ],
        [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0],
        ],
        [
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
        ],
    ]

    RESULT = [16, 13, 0]

    for i in range(len(TC)):
        answer = solution(TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
