# link: https://school.programmers.co.kr/learn/courses/30/lessons/42576


def solution(participant, completion):
    participant.sort()
    completion.sort()

    for a, b in zip(participant, completion):
        if a != b:
            return a

    return participant[-1]


def print_result():
    TC = [
        [["leo", "kiki", "eden"], ["eden", "kiki"]],
        [
            ["marina", "josipa", "nikola", "vinko", "filipa"],
            ["josipa", "filipa", "marina", "nikola"],
        ],
        [["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]],
    ]

    RESULT = ["leo", "vinko", "mislav"]

    for i in range(len(TC)):
        answer = solution(*TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
