# [달리기 경주](https://school.programmers.co.kr/learn/courses/30/lessons/178871)

## 개요
> ### 문제
> 얀에서는 매년 달리기 경주가 열립니다. 해설진들은 선수들이 자기 바로 앞의 선수를 추월할 때 추월한 선수의 이름을 부릅니다. 예를 들어 1등부터 3등까지 `"mumu", "soe", "poe" `선수들이 순서대로 달리고 있을 때, 해설진이 `"soe"`선수를 불렀다면 2등인 `"soe"` 선수가 1등인 `"mumu"` 선수를 추월했다는 것입니다. 즉 `"soe"` 선수가 1등, `"mumu"` 선수가 2등으로 바뀝니다.
>
> 선수들의 이름이 1등부터 현재 등수 순서대로 담긴 문자열 배열 `players`와 해설진이 부른 이름을 담은 문자열 배열 `callings`가 매개변수로 주어질 때, 경주가 끝났을 때 선수들의 이름을 1등부터 등수 순서대로 배열에 담아 `return` 하는 `solution` 함수를 완성해주세요.
>
> 요약: 앞 선수를 제치면 자신의 이름이 불린다. 불린 이름을 토대로 최종 순위를 유추해라.

> # 주요 제한사항
> - 5 ≤ players의 길이 ≤ 50,000
> - 2 ≤ callings의 길이 ≤ 1,000,000


<h1 align="center"><br><br><br>❗️❗️ 스포주의 ❗️❗️<br><br><br></h1>

## 풀이
### 접근
- 길이가 각각 5만, 백만이라 `for`문을 조금만 돌려도 시간이 오래걸림
- 데이터에 빠른 접근을 위해 `dict`활용

### 코드
```python
def solution(players, callings):
    r1 = {player: i for i, player in enumerate(players)}
    r2 = {i: player for i, player in enumerate(players)}
    
    for call in callings:
        rank = r1[call] - 1
        temp = r2[rank]
        r2[rank] = call
        r2[rank + 1] = temp
        r1[call] = rank
        r1[temp] = rank + 1
    answer = [*r2.values()]
    return answer
```

### 설명
- `r1`: `{선수: 등수}`로 이름을 통해 등수를 찾기 위한 딕셔너리
- `r2`: `{등수: 선수}`로 등수별로 선수 관리

1. `plyers`를 통해 `r1`, `r2` 생성
2. `callings`를 순회하며 선수 이름이 불리면 `r1`에서 해당 선수의 등수 가져오기
3. `rank`에 등수를 계산하기 편하게 -1해서 저장
4. `rank`를 토대로 `r2` 수정
5. 마찬가지로 `r1` 수정
6. 반복이 끝나면 `answer`에 `r2`의 값들만 뽑아서 저장
   - 정리하면서 딕셔너리는 순서 보장이 안되는데 어떻게 통과했지? 라는 생각이 들었음
   - 찾아보니 파이썬 3.5 버전 까지는 입력한 순서 보장이 안되었지만 3.6 버전 이후부터는 보장이 된다함
   - 내가 제출했을 때 프로그래머스 컴파일 옵션이 3.8.5 버전이어서 통과됨

### 다른 사람 풀이 보고 느낀점
```python
def solution(players, callings):
    rank_dict = {player: i for i, player in enumerate(players)}
    for call in callings:
        rank = rank_dict[call]
        rank_dict[call] -= 1
        rank_dict[players[rank - 1]] += 1
        players[rank], players[rank-1] = players[rank-1], players[rank]
    return players
```
- 어차피 직접 접근하는걸 원했다면 굳이 `r2`를 만들 필요 없이 `rank`를 통해서 `players`를 변경 시켜주는 것이 더 깔끔하고 시간복잡도도 똑같은데 왜 더 오래걸릴거라고 생각했는지 모르겠음
- `players[rank], players[rank-1] = players[rank-1], players[rank]` 이런 식으로 `swap`기능이 있는걸 알고 있었으면서 까먹고 `temp` 만들고 따로따로 코드 짠게 좀 부끄러웠음