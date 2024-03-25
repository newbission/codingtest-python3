# [완주하지 못한 선수](https://school.programmers.co.kr/learn/courses/30/lessons/42576)

## 개요
> ### 문제
> 수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
>
> 마라톤에 참여한 선수들의 이름이 담긴 배열 `participant`와 완주한 선수들의 이름이 담긴 배열 `completion`이 주어질 때, 완주하지 못한 선수의 이름을 `return` 하도록 `solution` 함수를 작성해주세요.
>
> 요약: 한 명을 제외한 모든 선수가 완주 했을 때 완주하지 못한 선수의 이름 찾기

> # 주요 제한사항
> - 동명이인 존재
> - `completion` 길이 < `participant` 길이

<h1 align="center"><br><br><br>❗️❗️ 스포주의 ❗️❗️<br><br><br></h1>

## 풀이
### 접근
- 정렬 후 이름이 다른 지점에서 반환

### 코드
```python
def solution(participant, completion):
    participant.sort()
    completion.sort()

    for a, b in zip(participant, completion):
        if a != b:
            return a

    return participant[-1]
```

### 설명
1. 이름순으로 정렬하기
2. 두 리스트를 `zip`으로 묶어서 앞에서부터 비교
3. 다르면 해당 선수가 완주하지 못한것으로 `a` 반환
4. 순회가 끝날때까지 전부 똑같으면 마지막 선수가 완주 못한 것으로 마지막 선수 반환

### 다른 사람 풀이 보고 느낀점
```python
import collections
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
```
> `Counter`에 대해서 알아보면 좋을 것 같음
