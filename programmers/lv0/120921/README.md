# [문자열 밀기](https://school.programmers.co.kr/learn/courses/30/lessons/120921)

## 개요
> ### 문제
> 문자열 `"hello"`에서 각 문자를 오른쪽으로 한 칸씩 밀고 마지막 문자는 맨 앞으로 이동시키면 `"ohell"`이 됩니다. 이것을 문자열을 민다고 정의한다면 문자열 A와 B가 매개변수로 주어질 때, `A`를 밀어서 `B`가 될 수 있다면 밀어야 하는 최소 횟수를 `return`하고 밀어서 `B`가 될 수 없으면 `-1`을 `return` 하도록 `solution` 함수를 완성해보세요.
>
> **요약**: `A`를 오른쪽으로 한 칸씩 밀 때(마지막 글자가 처음으로 `hello` $\to$ `ohell`) `B`와 똑같아지는 순간은 몇 번째인지 구하기. 단, 경우의 수가 없으면 `-1`

> ### 주요 제한사항
> .

<h1 align="center"><br><br><br>❗️❗️ 스포주의 ❗️❗️<br><br><br></h1>

## 풀이
### 접근
- 완탐으로 풀기

### 코드
```python
def solution(A, B):
    cnt = 0
    while cnt < len(A) and A != B:
        cnt += 1
        A = A[-1] + A[:-1]

    return cnt if cnt != len(A) else -1
```

### 설명
1. `cnt < len(A)`: `cnt`가 `A`의 글자수라 똑같다는 건 이미 한 바퀴를 돌았다는 뜻
2. `A != B`: `A`가 `B`와 같아질 때 까지 규칙에 맞게 `A`를 오른쪽으로 밀기

### 다른 사람 풀이 보고 느낀점
```python
return (b*2).find(a) or -1
```
> 부분에서 찾는 문제가 나오면 한 번 더 써서 찾으면 된다는걸 매번 까먹음...
