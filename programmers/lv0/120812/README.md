# [최빈값 구하기](https://school.programmers.co.kr/learn/courses/30/lessons/120812)

## 개요
> ### 문제
> 최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 정수 배열 `array`가 매개변수로 주어질 때, 최빈값을 `return` 하도록 `solution` 함수를 완성해보세요. 최빈값이 여러 개면 -1을 `return` 합니다.
>
> 요약: 최빈값이 하나면 최빈값, 여러개면 -1 리턴

> # 주요 제한사항
> $0 < array의 \ 길이 < 100$  
> $0 \le array의 \ 원소 < 1,000$

<h1 align="center"><br><br><br>❗️❗️ 스포주의 ❗️❗️<br><br><br></h1>

## 풀이
### 접근
- 총 개수가 100개가 안되고 숫자의 범위가 1000개 이므로 단순히 리스트로 만들기
- 나중에 최빈값을 구하기 위해 개수를 기준으로 정렬하기 위한 `[인덱스, 개수]` 쌍 만들기

### 코드
```python
def solution(array):
    arr = [[i, 0] for i in range(1000)]

    for i in array:
        arr[i][1] += 1

    arr.sort(key=lambda a: a[1], reverse=True)

    return arr[0][0] if arr[0][1] != arr[1][1] else -1
```

### 설명
1. `array`의 원소 범위가 `0 ~ 1000` 이므로 1000개 짜리 리스트 생성
   1. 나중에 정렬하고 나서 최빈값의 번호를 알기 위해 `[인덱스, 0]` 으로 초기화
2. `array`를 순회하면서 해당하는 숫자의 개수 +1
3. 최빈값을 구하기 위해 정렬
4. 앞에 두개를 비교해서 다르면 맨 앞 숫자, 같으면 -1 리턴

### 다른 사람 풀이 보고 느낀점
> `while`문을 돌면서 현재 `array`안의 숫자들을 `set`으로 만들어 하나씩 지워가는 방법이 있었는데 흥미로웠음

```python
def solution(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0: return a
    return -1
```
