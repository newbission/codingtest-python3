# link: https://school.programmers.co.kr/learn/courses/30/lessons/92334


def solution(id_list, report, k):
    if len(id_list) - 1 < k:
        return [0] * len(id_list)
    
    id_index = {key: i for i, key in enumerate(id_list)}

    answer = [0] * len(id_list)
    report_id = {key: set() for key in id_list}
    reported_id = {key: set() for key in id_list}

    for r in report:
        reporter, reported = r.split()
        report_id[reporter].add(reported)
        reported_id[reported].add(reporter)

    suspended_id = []
    for id in id_list:
        if len(reported_id[id]) >= k:
            suspended_id.append(id)
    
    for id in id_list:
        for suspended in suspended_id:
            if suspended in report_id[id]:
                answer[id_index[id]] += 1
    return answer


def print_result():
    TC = [
        [
            ["muzi", "frodo", "apeach", "neo"],
            ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi", "muzi frodo"],
            2,
        ],
        [["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3],
    ]

    RESULT = [[2, 1, 1, 0], [0, 0]]

    for i in range(len(TC)):
        answer = solution(*TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
