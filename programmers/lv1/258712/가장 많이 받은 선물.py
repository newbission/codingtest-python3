# link: https://school.programmers.co.kr//learn/courses/30/lessons/258712


def solution(friends, gifts):
    size = len(friends)
    friends_index = {}
    total_gift_score = [0] * size
    gift_list = [[0 for _ in range(size)] for _ in range(size)]
    result = [0] * size

    for i in range(size):
        friends_index[friends[i]] = i
    
    for gift in gifts:
        a, b = gift.split(' ')

        # 선물지수 수정
        total_gift_score[friends_index[a]] += 1
        total_gift_score[friends_index[b]] -= 1

        # 선물 준 것만 카운트
        gift_list[friends_index[a]][friends_index[b]] += 1

    
    for i in range(size-1): # size-1: 마지막 사람은 어차피 비교 대상이 없음
        for j in range(i+1, size): # i+1: 굳이 두번 돌 필요가 없음
            if i == j: continue

            # 주고 받은 선물 수가 같다면 선물지수 비교
            if gift_list[i][j] == gift_list[j][i]:
                result[i] += total_gift_score[i] > total_gift_score[j]
                result[j] += total_gift_score[j] > total_gift_score[i]

            # 더 많이 준 사람이 받기
            elif gift_list[i][j] > gift_list[j][i]:
                result[i] += 1
            else:
                result[j] += 1
    return max(result)


def print_result():
    TC = [
        [
            ["muzi", "ryan", "frodo", "neo"],
            [
                "muzi frodo",
                "muzi frodo",
                "ryan muzi",
                "ryan muzi",
                "ryan muzi",
                "frodo muzi",
                "frodo ryan",
                "neo muzi",
            ],
        ],
        [
            ["joy", "brad", "alessandro", "conan", "david"],
            [
                "alessandro brad",
                "alessandro joy",
                "alessandro conan",
                "david alessandro",
                "alessandro david",
            ],
        ],
        [
            ["a", "b", "c"],
            ["a b", "b a", "c a", "a c", "a c", "c a"]
        ],
    ]

    RESULT = [2, 4, 0]

    for i in range(len(TC)):
        answer = solution(TC[i][0], TC[i][1])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
