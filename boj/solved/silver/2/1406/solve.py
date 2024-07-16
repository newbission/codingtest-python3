# link: https://www.acmicpc.net/problem/1406

TC = []
RESULT = open("data/result.txt").read().split("\n\n")
testcase_file = open("data/testcase.txt").read().split("\n\n")
for tc in testcase_file:
    TC.append(tc.split("\n"))

tc_num = None
tc_line = None


def input() -> str:
    global tc_line
    tc_line += 1
    return TC[tc_num][tc_line]

# from sys import stdin
def solution():
    class Node:
        def __init__(self, value, prev=None, next=None):
            self.value = value
            self.prev = prev
            self.next = next

            if prev:
                prev.next = self
            if next:
                next.prev = self

    start = Node(None)
    now = start

    s = input()
    for c in s:
        new = Node(c, now)
        now = new

    n = int(input())
    for _ in range(n):
        # cmd = stdin.readline().rstrip()
        cmd = input()

        if cmd == "L" and now != start:
            now = now.prev
        elif cmd == "D" and now.next:
            now = now.next
        elif cmd == "B" and now != start:
            prev = now.prev
            next = now.next
            if prev:
                prev.next = next
            if next:
                next.prev = prev
            now = prev
        elif cmd[0] == "P":
            new = Node(cmd[2], now, now.next)
            now = new
            

    now = start.next
    res = ""

    while now:
        res += now.value
        now = now.next

    print(res)

    return res
    # print(res)


def print_result():
    global tc_num, tc_line
    for i in range(len(TC)):
        tc_num = i
        tc_line = -1
        answer = solution()
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
