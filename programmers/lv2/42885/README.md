# [구명보트](https://school.programmers.co.kr/learn/courses/30/lessons/42885)

## 개요
> ### 문제
> > 무인도에 갇힌 사람들을 구명보트를 이용하여 구출하려고 합니다. 구명보트는 작아서 한 번에 최대 2명씩 밖에 탈 수 없고, 무게 제한도 있습니다.
> 
> 예를 들어, 사람들의 몸무게가 `[70kg, 50kg, 80kg, 50kg]`이고 구명보트의 무게 제한이 100kg이라면 2번째 사람과 4번째 사람은 같이 탈 수 있지만 1번째 사람과 3번째 사람의 무게의 합은 150kg이므로 구명보트의 무게 제한을 초과하여 같이 탈 수 없습니다.
> 
> 구명보트를 최대한 적게 사용하여 모든 사람을 구출하려고 합니다.
> 
> 사람들의 몸무게를 담은 배열 `people`과 구명보트의 무게 제한 `limit`가 매개변수로 주어질 때, 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 `return` 하도록 `solution` 함수를 작성해주세요.
>
> 요약: 사람들의 무게가 주어지고, 무게 제한 `limit`이 있는 최대 2명만 탑승 가능한 구명보트가 있을 때 구명보트를 최소한으로 움직이는 횟수

> # 주요 제한사항
> - 탑승객은 최대 2명

<h1 align="center"><br><br><br>❗️❗️ 스포주의 ❗️❗️<br><br><br></h1>

## 풀이
### 접근
- ~~사람들을 무거운 순으로 정렬한 뒤 `limit` 전까지 보트에 태우고 다시 가벼운 순으로 `limit` 전까지 보트에 태우면 되지 않을까?~~ $\to$ 최대 2명 제한
- 가장 무거운 사람 태우고 가능하면 가장 가벼운 사람 태우는 방식으로 변경

### 코드
```python
def solution(people, limit):
    answer = 0
    people.sort(key=lambda a: -a)
    l, r = 0, len(people)-1
    while(l <= r):
        answer += 1
        sum = people[l]
        if r > l and sum + people[r] <= limit:
            sum += people[r]
            r -= 1
        l += 1
    return answer
```

### 설명
1. `people.sort(key=lambda a: -a)`: `poeple`을 내림차순으로 정렬
2. `l`, `r`: 이분 탐색을 위한 인덱스
3. `while(l <= r)`: `r`이 `l`보다 작다는건 이미 모든 사람을 태운거기 때문에 `l == r` 까지만 탐색, `l == r`인 이유는 마지막 한명이 남으면 두 인덱스가 같기 때문
4. `sum = people[l]`: 구조시 무조건 무게가 무거운 사람부터 태움 
5. `if r > l and sum + people[r] <= limit: sum += people[r]` 만약 자리가 남으면 무게가 제일 작은 사람부터 태움
6. `l += 1`이 제일 마지막에 나오는 이유는 두명 남았을 때 `sum = people[l]`을 하자 마자 `l += 1`을 하게되면 `l == r`이 된다. 이렇게 되면 `if r > l`에서 걸러지게 되어 마지막 남은 사람을 태우지 못하고 출발하여 다시 데리러 와야 하는 경우 발생

### 다른 사람 풀이 보고 느낀점
```python
def solution(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer
```
> 귀찮게 내림차순으로 정렬할 필요 없이 오름차순으로 정렬해서 `l`과 `r`의 정의만 바꾸면 되는 거였음  
> 짝지어지는 경우만 생각하면 된다는 걸 깨달음 그리고 `sum`조차 만들 필요가 없었음...
