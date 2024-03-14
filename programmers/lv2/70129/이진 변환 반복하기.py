# link: https://school.programmers.co.kr/learn/courses/30/lessons/70129


def solution(s):
    cnt0 = 0
    cnt = 0

    while s != "1":
        x = ""
        for c in s:
            if c == "0":
                cnt0 += 1
            else:
                x += c
        s = bin(len(x))[2:]

        # 간단한 풀이
        # cnt0 += s.count("0")
        # s = bin(len(s.replace("0", "")))[2:]
        
        cnt += 1
    return [cnt, cnt0]


def print_result():
    TC = ["110010101001", "01110", "1111111"]

    RESULT = [[3, 8], [3, 3], [4, 1]]

    for i in range(len(TC)):
        answer = solution(TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
