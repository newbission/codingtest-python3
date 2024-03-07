# [신고 결과 받기](https://school.programmers.co.kr/learn/courses/30/lessons/92334)

## 개요
> ### 문제
> 신입사원 무지는 게시판 불량 이용자를 신고하고 처리 결과를 메일로 발송하는 시스템을 개발하려 합니다. 무지가 개발하려는 시스템은 다음과 같습니다.
>
> - 각 유저는 한 번에 한 명의 유저를 신고할 수 있습니다.  
>   - 신고 횟수에 제한은 없습니다. 서로 다른 유저를 계속해서 신고할 수 있습니다.  
>   - 한 유저를 여러 번 신고할 수도 있지만, 동일한 유저에 대한 신고 횟수는 1회로 처리됩니다.  
> - `k`번 이상 신고된 유저는 게시판 이용이 정지되며, 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송합니다.  
>   - 유저가 신고한 모든 내용을 취합하여 마지막에 한꺼번에 게시판 이용 정지를 시키면서 정지 메일을 발송합니다.
> 
> 다음은 전체 유저 목록이 `["muzi", "frodo", "apeach", "neo"]`이고, `k` = 2`(즉, 2번 이상 신고당하면 이용 정지)인 경우의 예시입니다.
> 
> | 유저 ID  | 유저가 신고한 ID | 설명                               |
> | :------- | :--------------- | :--------------------------------- |
> | "muzi"   | "frodo"          | "muzi"가 "frodo"를 신고했습니다.   |
> | "apeach" | "frodo"          | "apeach"가 "frodo"를 신고했습니다. |
> | "frodo"  | "neo"            | "frodo"가 "neo"를 신고했습니다.    |
> | "muzi"   | "neo"            | "muzi"가 "neo"를 신고했습니다.     |
> | "apeach" | "muzi"           | "apeach"가 "muzi"를 신고했습니다.  |  
>
> 각 유저별로 신고당한 횟수는 다음과 같습니다.
> 
> | 유저 ID  | 신고당한 횟수 |
> | :------- | :------------ |
> | "muzi"   | 1             |
> | "frodo"  | 2             |
> | "apeach" | 0             |
> | "neo"    | 2             |
> 
> 위 예시에서는 `2`번 이상 신고당한 `"frodo"`와 `neo`의 게시판 이용이 정지됩니다. 이때, 각 유저별로 신고한 아이디와 정지된 아이디를 정리하면 다음과 같습니다.
> 
> | 유저 ID  | 유저가 신고한 ID  | 정지된 ID        |
> | :------- | :---------------- | :--------------- |
> | "muzi"   | \["frodo", "neo"\]  | \["frodo", "neo"\] |
> | "frodo"  | \["neo"\]           | \["neo"\]          |
> | "apeach" | \["muzi", "frodo"\] | \["frodo"\]    "neo"    |
> | "neo"    | 없음              | 없음             |
>
> 따라서 `"muzi"`는 처리 결과 메일을 `2`회, `"frodo"`와 `"apeach"`는 각각 처리 결과 메일을 `1`회 받게 됩니다.
> 
> 이용자의 ID가 담긴 문자열 배열 `id_list`, 각 이용자가 신고한 이용자의 ID 정보가 담긴 문자열 배열 `report`, 정지 기준이 되는 신고 횟수 `k`가 매개변수로 주어질 때, 각 유저별로 처리 결과 메일을 받은 횟수를 배열에 담아 `return` 하도록 `solution` 함수를 완성해주세요.
>
> 요약: 유저별로 `k`번 신고된 유저를 몇 명 신고했는가

> # 주요 제한사항
> - 동일한 유저를 여러번 신고할 수 있지만 1회로 간주
> - 자기 자신을 신고하는 경우는 없습니다.
> - return 하는 배열은 id_list에 담긴 id 순서대로 각 유저가 받은 결과 메일 수를 담으면 됩니다.

<h1 align="center"><br><br><br>❗️❗️ 스포주의 ❗️❗️<br><br><br></h1>

## 풀이
### 접근
- 유저별로 신고한 명단 $\to$ 여러번 가능하므로 `set`
  - ~~일단 `list`로 쭉 받은 뒤에 `set`으로 변경~~
  - 그냥 처음부터 `set`
- 유저별로 신고받은 명단 $\to$ 여러번 가능하므로 `set`
  - ~~마찬가지로 `list`로 쭉 받은 뒤에 `set`으로 변경~~
  - 그냥 처음부터 `set`
- 신고받은 명단을 토대로 정지 대상자 추리기
- 정지대상자를 토대로 유저별로 감지하기

### 코드
```python
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
```

### 설명
1. `report_id`에는 자신이 신고한 `id` 저장
2. `reported_id`에는 자신을 신고한 `id` 저장
3. 저장된 내용을 토대로 `k`이상 신고된 `id` `suspended_id`에 저장
4. 유저별로 `report_id` 중 `suspended_id`에 속한 `id` 개수 파악

### 다른사람 풀이 보고 느낀점
> 애초에 `report` 자체를 `set`으로 만드는 방법을 떠올리지 못했음  
> 신고 받은 내역만 파악 후 다시 정지된 사람을 신고한 `id`만 파악하면 되는 문제였음 

```python
for r in set(report):
    reports[r.split()[1]] += 1

for r in set(report):
    if reports[r.split()[1]] >= k:
        answer[id_list.index(r.split()[0])] += 1
```