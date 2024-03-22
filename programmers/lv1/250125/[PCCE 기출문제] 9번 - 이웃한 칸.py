# link: https://school.programmers.co.kr/learn/courses/30/lessons/250125


def solution(board, h, w):
    answer = 0
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    color = board[h][w]
    n = len(board)
    for i in range(4):
        ny, nx = h + dy[i], w + dx[i]
        if 0 <= ny < n and 0 <= nx < n and board[ny][nx] == color:
            answer += 1
    return answer


def print_result():
    TC = [
        [
            [
                ["blue", "red", "orange", "red"],
                ["red", "red", "blue", "orange"],
                ["blue", "orange", "red", "red"],
                ["orange", "orange", "red", "blue"],
            ],
            1,
            1,
        ],
        [
            [
                ["yellow", "green", "blue"],
                ["blue", "green", "yellow"],
                ["yellow", "blue", "blue"],
            ],
            0,
            1,
        ],
    ]

    RESULT = [2, 1]

    for i in range(len(TC)):
        answer = solution(*TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
