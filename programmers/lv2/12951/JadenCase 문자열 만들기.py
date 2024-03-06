# link: https://school.programmers.co.kr/learn/courses/30/lessons/12951


solution = lambda s: " ".join([word.capitalize() for word in s.split(" ")])


def print_result():
    TC = [
        "3people unFollowed me",
        "for the last week",
    ]

    RESULT = ["3people Unfollowed Me", "For The Last Week"]

    for i in range(len(TC)):
        answer = solution(TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
