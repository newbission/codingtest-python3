# [특이한 정렬](https://school.programmers.co.kr/learn/courses/30/lessons/120880)

## 개요
> ### 문제
> 정수 `n`을 기준으로 `n`과 가까운 수부터 정렬하려고 합니다. 이때 `n`으로부터의 거리가 같다면 더 큰 수를 앞에 오도록 배치합니다. 정수가 담긴 배열 `numlist`와 정수 n이 주어질 때 `numlist`의 원소를 `n`으로부터 가까운 순서대로 정렬한 배열을 `return`하도록 `solution` 함수를 완성해주세요.
>
> **요약**: 정수 `n`과 가까운 순으로 정렬, 거리가 같으면 더 큰 수가 앞으로 온다.

> ### 주요 제한사항
> - 중복원소는 없다.

<h1 align="center"><br><br><br>❗️❗️ 스포주의 ❗️❗️<br><br><br></h1>

## 풀이
### 접근
- `n`이 기준이므로 `n`에서 뺀 값의 절대값을 기준으로 정렬, 같으면 더 큰 숫자가 앞으로 오게 정렬

### 코드
```python
def solution(numlist, n):
    return sorted(numlist, key=lambda i: (abs(n - i), n - i))
```

### 설명
1. 절대값 기준으로 정렬
2. 같으면 `n - i`로 `i`가 더 크면 음수가 되어 내림 차순 정렬

### 다른 사람 풀이 보고 느낀점
> .
