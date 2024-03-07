# link: https://school.programmers.co.kr/learn/courses/30/lessons/12941


def solution(A,B):
    A.sort()
    B.sort(reverse=True)

    return sum(a * b for a, b in zip(A, B))
    
    # 더 간략한 버전
    # return sum(a * b for a, b in zip(sorted(A), sorted(B, reverse=True)))



def print_result():
    TC = [[[1, 4, 2], [5, 4, 4]], [[1, 2], [3, 4]]]

    RESULT = [29, 10]

    for i in range(len(TC)):
        answer = solution(TC[i][0], TC[i][1])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
