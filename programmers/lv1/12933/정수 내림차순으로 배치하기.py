# link: https://school.programmers.co.kr/learn/courses/30/lessons/12933


solution = lambda n: int("".join(sorted(str(n), reverse=True)))


def print_result():
    TC = [118372]

    RESULT = [873211]

    for i in range(len(TC)):
        answer = solution(TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
