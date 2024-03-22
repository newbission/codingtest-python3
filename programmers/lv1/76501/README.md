# [음양 더하기](https://school.programmers.co.kr/learn/courses/30/lessons/76501)

## 개요
> ### 문제
> 어떤 정수들이 있습니다. 이 정수들의 절댓값을 차례대로 담은 정수 배열 `absolutes`와 이 정수들의 부호를 차례대로 담은 불리언 배열 `signs`가 매개변수로 주어집니다. 실제 정수들의 합을 구하여 `return` 하도록 `solution` 함수를 완성해주세요.
>
> 요약: `signs`를 토대로 `absolutes`의 값들을 더하기

> # 주요 제한사항
> .

<h1 align="center"><br><br><br>❗️❗️ 스포주의 ❗️❗️<br><br><br></h1>

## 풀이
### 접근
- 인덱스를 사용해서 `absolutes`와 `signs`의 값들에 접근해 더해주기

### 코드
```python
def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        answer += absolutes[i] if signs[i] else -absolutes[i]
    return answer
```

### 설명
1. `signs[i]`를 비교해 `absolutes[i]`를 `+`, `-` 해주기

### 다른 사람 풀이 보고 느낀점
```python
def solution(absolutes, signs):
    answer=0
    for absolute,sign in zip(absolutes,signs):
        if sign:
            answer+=absolute
        else:
            answer-=absolute
    return answer
```
> `zip`을 활용하면 좀 더 편하게 작성할 수 있을 거 같음
