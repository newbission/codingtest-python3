# link: https://www.acmicpc.net/problem/10828

TC = []
RESULT = open("file/result.txt").read().split("\n\n")

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
    n = int(input())
    stack = []
    res = []
    for _ in range(n):
        cmd = input()
        if cmd == 'top':
            res.append(stack[-1] if len(stack) else '-1')
        elif cmd == 'empty':
            res.append('0' if len(stack) else '1')
        elif cmd == 'size':
            res.append(str(len(stack)))
        elif cmd == 'pop':
            res.append(stack.pop() if len(stack) else '-1')
        else:
            stack.append(cmd[5:])

    return '\n'.join(res)
    # print('\n'.join(res))


def print_result():
    global tc_num, tc_line
    for i in range(len(TC)):
        tc_num = i
        tc_line = -1
        answer = solution()
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()

