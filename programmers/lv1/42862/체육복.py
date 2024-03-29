# link: https://school.programmers.co.kr/learn/courses/30/lessons/42862


def solution(n, lost, reserve):
    c = [1] * n
    for i in lost:
        c[i - 1] -= 1
    for i in reserve:
        c[i - 1] += 1

    def go(i, arr):
        if i == n:
            s = 0
            for j in arr:
                s += 1 if j else 0
            return s
        s1 = s2 = s3 = 0
        if arr[i] == 2:
            if i - 1 >= 0 and arr[i - 1] == 0:
                temp = [*arr]
                temp[i - 1] = temp[i] = 1
                s1 = go(i + 1, [*temp])
            if i + 1 < n and arr[i + 1] == 0:
                temp = [*arr]
                temp[i + 1] = temp[i] = 1
                s2 = go(i + 1, [*temp])
            else:
                s3 = go(i + 1, [*arr])
        else:
            s3 = go(i + 1, [*arr])
        return max(s1, s2, s3)

    answer = go(0, c)

    return answer


def print_result():
    TC = [[5, [2, 4], [1, 3, 5]], [5, [2, 4], [3]], [3, [3], [1]]]

    RESULT = [5, 4, 2]

    for i in range(len(TC)):
        answer = solution(*TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
