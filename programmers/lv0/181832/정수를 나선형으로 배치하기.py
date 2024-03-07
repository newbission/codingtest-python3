# link: https://school.programmers.co.kr/learn/courses/30/lessons/181832


def solution(n):
    if n == 1:
        return [[1]]
    arr = [[0] * n for _ in range(n)]
    y, x = 0, 0
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    d = 0
    num = 1

    while not arr[y][x]:
        arr[y][x] = num

        y, x = y + dy[d], x + dx[d]

        # 만약에 범위를 벗어나거나 해당위치에 이미 번호가 존재할 경우
        if y >= n or y < 0 or x >= n or x < 0 or arr[y][x]:
            # y, x를 다시 되돌리고
            y, x = y - dy[d], x - dx[d]
            # d를 올리기
            d = (d + 1) % 4
            # y, x에 적용
            y, x = y + dy[d], x + dx[d]
        num += 1

    return arr


def print_result():
    TC = [4, 5]

    RESULT = [
        [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]],
        [
            [1, 2, 3, 4, 5],
            [16, 17, 18, 19, 6],
            [15, 24, 25, 20, 7],
            [14, 23, 22, 21, 8],
            [13, 12, 11, 10, 9],
        ],
    ]

    for i in range(len(TC)):
        answer = solution(TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
