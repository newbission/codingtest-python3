# link: https://school.programmers.co.kr/learn/courses/30/lessons/64061


def solution(board, moves):
    board.reverse()
    box = []
    for x in range(len(board[0])):
        box.append([])
        for y in range(len(board)):
            if board[y][x]:
                box[x].append(board[y][x])

    answer = 0
    basket = []
    for i in moves:
        i -= 1
        if len(box[i]):
            pick = box[i].pop()
            if len(basket) and basket[-1] == pick:
                basket.pop()
                answer += 2
            else:
                basket.append(pick)
    return answer


def print_result():
    TC = [
        [
            [
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 3],
                [0, 2, 5, 0, 1],
                [4, 2, 4, 4, 2],
                [3, 5, 1, 3, 1],
            ],
            [1, 5, 3, 5, 1, 2, 1, 4],
        ]
    ]

    RESULT = [4]

    for i in range(len(TC)):
        answer = solution(*TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
