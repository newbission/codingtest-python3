# link: https://school.programmers.co.kr/learn/courses/30/lessons/250121


def solution(data, ext, val_ext, sort_by):
    key = ["code", "date", "maximum", "remain"]
    ext, sort_by = key.index(ext), key.index(sort_by)
    return sorted([t for t in data if t[ext] < val_ext], key=lambda x: x[sort_by])

    filtered_data = []
    for item in data:
        if item[ext] < val_ext:
            filtered_data.append(item)
    
    filtered_data.sort(key=lambda item: item[sort_by])
    return filtered_data

def print_result():
    TC = [
        [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]],
        "date",
        20300501,
        "remain",
    ]

    RESULT = [[[3, 20300401, 10, 8], [1, 20300104, 100, 80]]]

    for i in range(len(TC)):
        answer = solution(TC[i])
        print(f"TESTCASE {i+1} :: {answer == RESULT[i]}")


print_result()
