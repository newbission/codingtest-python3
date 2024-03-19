# link: https://school.programmers.co.kr/learn/courses/30/lessons/12981


def solution(n, words):
    order = [0] * n
    order[1] = 1
    temp = [words[0]]
    for i in range(1, len(words)):
        word = words[i]
        if temp[-1][-1] != word[0] or word in temp:
            return [i%n + 1, i//n + 1]
        temp.append(word)
        order[i%n] += 1
    return [0, 0]



def print_result():
    TC = [
        [
            3,
            [
                "tank",
                "kick",
                "know",
                "wheel",
                "land",
                "dream",
                "mother",
                "robot",
                "tank",
            ],
        ],
        [
            5,
            [
                "hello",
                "observe",
                "effect",
                "take",
                "either",
                "recognize",
                "encourage",
                "ensure",
                "establish",
                "hang",
                "gather",
                "refer",
                "reference",
                "estimate",
                "executive",
            ],
        ],
        [2, ["hello", "one", "even", "never", "now", "world", "draw"]],
    ]

    RESULT = [[3, 3], [0, 0], [1, 3]]

    for i in range(len(TC)):
        answer = solution(*TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
