# link: https://school.programmers.co.kr/learn/courses/30/lessons/67256


def solution(numbers, hand):
    answer = ""
    hand = "L" if hand == "left" else "R"
    thumbs = {"L": (3, 0), "R": (3, 2)}

    coor = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2),
        0: (3, 1),
    }

    def getThumbByDist(n):
        ly, lx = thumbs["L"]
        ry, rx = thumbs["R"]
        ny, nx = coor[n]

        dl = abs(ny - ly) + abs(nx - lx)
        dr = abs(ny - ry) + abs(nx - rx)
        return "L" if dl < dr else "R" if dr < dl else hand

    for n in numbers:
        if n in (1, 4, 7):
            thumb = "L"
        elif n in (3, 6, 9):
            thumb = "R"
        else:
            thumb = getThumbByDist(n)
        answer += thumb
        thumbs[thumb] = coor[n]
    return answer


def print_result():
    TC = [
        [[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"],
        [[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"],
        [[1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"],
    ]

    RESULT = ["LRLLLRLLRRL", "LRLLRRLLLRR", "LLRLLRLLRL"]

    for i in range(len(TC)):
        answer = solution(*TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
