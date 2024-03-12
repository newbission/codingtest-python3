# link: https://school.programmers.co.kr/learn/courses/30/lessons/12924


def solution(n):
    answer = 0
    for i in range(1, n+1):
        temp = 0
        while(temp < n):
            temp += i
            i += 1
        if temp == n:
            answer += 1

        # while 대신 방법
        # for j in range(i, n+1):
        #     temp += j
        #     if temp >= n:
        #         answer += temp == n
        #         break
    return answer


def print_result():
    TC = [15]

    RESULT = [4]

    for i in range(len(TC)):
        answer = solution(TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")

print_result()