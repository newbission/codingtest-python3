# [OX퀴즈](https://school.programmers.co.kr/learn/courses/30/lessons/120907)

## 개요
> ### 문제
> 덧셈, 뺄셈 수식들이 `'X [연산자] Y = Z'` 형태로 들어있는 문자열 배열 `quiz`가 매개변수로 주어집니다. 수식이 옳다면 `"O"`를 틀리다면 `"X"`를 순서대로 담은 배열을 `return`하도록 `solution` 함수를 완성해주세요.
>
> 요약: `'X [연산자] Y = Z'` 형태로 문자열이 주어질 때 수식이 맞으면 `"O"` 틀리면 `"X"`

> # 주요 제한사항
> - 연산 기호와 숫자 사이는 항상 하나의 공백이 존재합니다. 단 음수를 표시하는 마이너스 기호와 숫자 사이에는 공백이 존재하지 않습니다.
> - `[연산자]`는 `+` 와 `-` 중 하나입니다.

<h1 align="center"><br><br><br>❗️❗️ 스포주의 ❗️❗️<br><br><br></h1>

## 풀이
### 접근
- 문자열을 분해해서 `x`, `y`, `z`를 숫자로 변환한 뒤 수식에 적용해서 결과 도출하기

### 코드
```python
def solution(quiz):
    answer = []
    for q in quiz:
        q = q.split()
        x, y, z = map(int, (q[0], q[2], q[4]))
        if q[1] == "+":
            answer.append("O" if x + y == z else "X")
        else:
            answer.append("O" if x - y == z else "X")
    return answer
```

### 설명
1. `q`를 공백을 기준으로 분해
2. `x, y, z = map(int, (q[0], q[2], q[4]))`: 각 숫자 부분을 순서에 맞춰서 `x`, `y`, `z`에 숫자 형식으로 저장
3. 연산자에 따라서 수식 적용한 결과 `answer`에 저장

### 다른 사람 풀이 보고 느낀점
> .
