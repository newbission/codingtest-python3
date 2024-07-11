# link: https://www.acmicpc.net/problem/10950

TC = [
    [
        "5",
        "1 1",
        "2 3",
        "3 4",
        "9 8",
        "5 2",
    ]
]
RESULT = [
"""2
5
7
17
7"""
]

tc_num = None
tc_line = None


def input() -> str:
    global tc_line
    tc_line += 1
    return TC[tc_num][tc_line]


def solution():
    t = int(input())
    res = []
    for _ in range(t):
        res.append(sum(map(int, input().split())))

    return "\n".join(map(str,res))
    # print("\n".join(map(str,res)))


def print_result():
    global tc_num, tc_line
    for i in range(len(TC)):
        tc_num = i
        tc_line = -1
        answer = solution()
        print(RESULT[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
