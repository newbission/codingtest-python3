# link: https://school.programmers.co.kr//learn/courses/30/lessons/12928


def solution(n):
    # res = 0
    # for i in range(1, int(n ** (1 / 2))+1):
    #     if n % i == 0:
    #         res += i
    #         if n / i != i:
    #             res += (n / i)

    # return res

    return sum([i + (n / i) for i in range(1, int(n**0.5) + 1) if n % i == 0]) - (
        (n**0.5 == int(n**0.5)) * n**0.5
    )


def print_result():
    TC = [12, 5, 9]

    RESULT = [28, 6, 13]

    for i in range(len(TC)):
        answer = solution(TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
