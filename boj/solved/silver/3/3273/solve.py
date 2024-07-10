# link: https://www.acmicpc.net/problem/3273

TC = [["9", "5 12 7 10 9 1 2 3 11", "13"]]
RESULT = [3]

tc_num = None
tc_line = None

def input() -> str:
    global tc_line
    tc_line += 1
    return TC[tc_num][tc_line]

def solution():
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    x = int(input()) 

    l, r = 0, n - 1
    res = 0

    while l < r:
        sum = arr[l] + arr[r]
        if sum > x:
            r -= 1
        elif sum < x:
            l += 1
        else:
            res += 1
            l += 1
            r -= 1
    
    return res


def print_result():
    global tc_num, tc_line
    for i in range(len(TC)):
        tc_num = i
        tc_line = -1
        answer = solution()
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()