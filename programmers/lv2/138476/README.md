# [귤 고르기](https://school.programmers.co.kr/learn/courses/30/lessons/138476)

## 개요
> ### 문제
> 경화는 과수원에서 귤을 수확했습니다. 경화는 수확한 귤 중 `k`개를 골라 상자 하나에 담아 판매하려고 합니다. 그런데 수확한 귤의 크기가 일정하지 않아 보기에 좋지 않다고 생각한 경화는 귤을 크기별로 분류했을 때 서로 다른 종류의 수를 최소화하고 싶습니다.
>
> 예를 들어, 경화가 수확한 귤 8개의 크기가 `[1, 3, 2, 5, 4, 5, 2, 3]` 이라고 합시다. 경화가 귤 6개를 판매하고 싶다면, 크기가 `1, 4`인 귤을 제외한 여섯 개의 귤을 상자에 담으면, 귤의 크기의 종류가 `2, 3, 5`로 총 3가지가 되며 이때가 서로 다른 종류가 최소일 때입니다.
> 
> 경화가 한 상자에 담으려는 귤의 개수 `k`와 귤의 크기를 담은 배열 `tangerine`이 매개변수로 주어집니다. 경화가 귤 `k`개를 고를 때 크기가 서로 다른 종류의 수의 최솟값을 `return` 하도록 `solution` 함수를 작성해주세요.
>
> 요약: 담아야할 귤의 개수 `k`가 주어질 때 귤 크기의 가짓수 가 최소한이 되도록 하시오

> # 주요 제한사항
> .

<h1 align="center"><br><br><br>❗️❗️ 스포주의 ❗️❗️<br><br><br></h1>

## 풀이
### 접근
- 개수가 많은 순서대로 정렬해서 앞에서부터 자르면 된다고 생각함
- 귤의 개수를 딕셔너리로 만들어서 파악
- 다시 정렬된 리스트로 만들어서 앞에서부터 개수 파악해서 커트  


### 코드
```python
def solution(k, tangerine):
    tan_dict = {i: 0 for i in set(tangerine)}
    for i in tangerine:
        tan_dict[i] += 1
    sorted_tan = sorted(list(tan_dict.items()), key=lambda item: -item[1])
    
    answer = 0
    cnt = 0
    idx = 0
    while cnt < k:
        i, n = sorted_tan[idx]
        idx += 1
        cnt += n
        answer += 1
    return answer
```

### 설명
1. `tan_dict`: 귤의 크기를 `key`로 갖는 딕셔너리 생성
2. `tangerine`을 순회하면서 크기별 개수 파악
3. `sorted_tan`: `tan_dict`를 개수가 많은 순서대로 정렬
4. `sorted_tan`을 순회하면서 개수를 파악해 `cnt`에 더해주고 가짓수 `+1`
5. `cnt`가 `k`보다 크면 담을만큼 담은 것으로 반복 종료

### 다른 사람 풀이 보고 느낀점
```python
def solution(k, tangerine):
    tan_dict = {i: 0 for i in set(tangerine)}
    for i in tangerine:
        tan_dict[i] += 1
    sorted_tan = sorted(list(tan_dict.items()), key=lambda item: -item[1])
    
    cnt = 0
    idx = 0
    while cnt < k:
        cnt += sorted_tan[idx][1]
        idx += 1
    return idx
```
> `idx` 자체가 현재 귤의 가짓수를 표현하는 것이라 따로 `answer`가 필요 없었음
