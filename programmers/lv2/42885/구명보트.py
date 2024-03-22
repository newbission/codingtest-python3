# link: https://school.programmers.co.kr/learn/courses/30/lessons/42885


def solution(people, limit):
    answer = 0
    people.sort(key=lambda a: -a)
    l, r = 0, len(people) - 1
    while l <= r:
        answer += 1
        sum = people[l]
        if r > l and sum + people[r] <= limit:
            sum += people[r]
            r -= 1
        l += 1
    return answer


def print_result():
    TC = [[[70, 50, 80, 50], 100], [[70, 80, 50], 100]]

    RESULT = [3, 3]

    for i in range(len(TC)):
        answer = solution(*TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
