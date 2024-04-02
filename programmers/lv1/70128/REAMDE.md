# [내적](https://school.programmers.co.kr/learn/courses/30/lessons/70128)

## 개요
> ### 문제
> 길이가 같은 두 1차원 정수 배열 `a`, `b`가 매개변수로 주어집니다. `a`와 `b`의 내적을 `return` 하도록 `solution` 함수를 완성해주세요.
> 
> 이때, `a`와 `b`의 내적은 `a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1]` 입니다. (`n`은 `a`, `b`의 길이)
>
> **요약**: 두 1차원 정수 배열 `a`, `b`가 주어질 때 두 배열의 내적을 구하기

> ### 주요 제한사항
> .

<h1 align="center"><br><br><br>❗️❗️ 스포주의 ❗️❗️<br><br><br></h1>

## 풀이
### 접근
- 내적을 몰라도 문제에 내적을 하는 방법이 나와있음

### 코드
```python
def solution(a, b):
    return sum(aa * bb for aa, bb in zip(a, b))
```

### 설명
1. 문제에 주어진 내적 공식대로 `a`, `b`를 `zip`으로 묶어 하나씩 차례대로 받은 뒤 곱해주었음

### 다른 사람 풀이 보고 느낀점
> .
