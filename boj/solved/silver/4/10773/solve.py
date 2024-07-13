# link: https://www.acmicpc.net/problem/10773

TC = []
RESULT = list(map(int, open("file/result.txt").read().split("\n\n")))

testcase_file = open("file/testcase.txt").read().split("\n\n")
for tc in testcase_file:
    TC.append(tc.split("\n"))


tc_num = None
tc_line = None


def input() -> str:
    global tc_line
    tc_line += 1
    return TC[tc_num][tc_line]


def solution():
    k = int(input())
    stack = []
    for _ in range(k):
        n = int(input())
        if n == 0:
            stack.pop()
        else:
            stack.append(n)

    return sum(stack)
    # print(sum(stack))


def print_result():
    global tc_num, tc_line
    for i in range(len(TC)):
        tc_num = i
        tc_line = -1
        answer = solution()
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()

