# link: https://school.programmers.co.kr/learn/courses/30/lessons/120956


def solution(babbling):
    words = ("aya", "ye", "woo", "ma")
    answer = 0
    for i in babbling:
        for word in words:
            if word in i:
                i = i.replace(word, " ")
        if len(i.replace(" ", "")) == 0:
            answer += 1
    return answer


def print_result():
    TC = [
        ["aya", "yee", "u", "maa", "wyeoo"],
        ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"],
    ]

    RESULT = [1, 3]

    for i in range(len(TC)):
        result = solution(TC[i])
        print(f"TESTCASE {i+1} :: {result == RESULT[i]}")


print_result()
