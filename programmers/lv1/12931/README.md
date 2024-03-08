# [자릿수 더하기](https://school.programmers.co.kr/learn/courses/30/lessons/12931)

## 개요
> ### 문제
> 자연수 `N`이 주어지면, `N`의 각 자릿수의 합을 구해서 `return` 하는 `solution` 함수를 만들어 주세요.  
> 예를들어 `N= 123`이면 `1 + 2 + 3 = 6`을 `return` 하면 됩니다.
>
> 요약: 주어진 숫자의 각 자릿수 더하기

> # 주요 제한사항
> .

<h1 align="center"><br><br><br>❗️❗️ 스포주의 ❗️❗️<br><br><br></h1>

## 풀이
### 접근
- 10씩 나누면서 나머지 더하면 되겠다.

### 코드
```python
def solution(n):
    answer = 0
    while n:
        answer += n % 10
        n //= 10
    return answer
```

### 설명
1. `n`이 0이 될때까지 10으로 나눈 나머지를 `answer`에 더해주고 `n`을 10으로 나누는 것을 반복

### 다른 사람 풀이 보고 느낀점
```python
sum([int(i) for i in str(number)])
sum(map(int, str(number)))
```
> `n` 자체를 `str`로 변경 후 각 자리수를 `int`로 변경하는 방법을 떠올리지 못해서 쉬웠음
