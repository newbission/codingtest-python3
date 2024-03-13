# link: https://school.programmers.co.kr/learn/courses/30/lessons/161990


def solution(wallpaper):
    right = bottom = -1
    top = left = 55

    for y in range(len(wallpaper)):
        for x in range(len(wallpaper[y])):
            if wallpaper[y][x] == "#":
                top = min(top, y)
                bottom = max(bottom, y + 1)
                left = min(left, x)
                right = max(right, x + 1)

    return [top, left, bottom, right]

    """
    res_y = set()
    res_x = set()
    
    for y in range(len(wallpaper)):
        for x in range(len(wallpaper[y])):
            if wallpaper[y][x] == "#":
                res_y.add(y)
                res_x.add(x)
    
    return [min(res_y), min(res_x), max(res_y)+1, max(res_x)+1]
    """


def print_result():
    TC = [
        [".#...", "..#..", "...#."],
        ["..........", ".....#....", "......##..", "...##.....", "....#....."],
        [
            ".##...##.",
            "#..#.#..#",
            "#...#...#",
            ".#.....#.",
            "..#...#..",
            "...#.#...",
            "....#....",
        ],
        ["..", "#."],
    ]

    RESULT = [
        [0, 1, 3, 4],
        [1, 3, 5, 8],
        [0, 0, 7, 9],
        [1, 0, 2, 1],
    ]

    for i in range(len(TC)):
        answer = solution(TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
