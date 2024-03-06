# [짝수와 홀수](https://school.programmers.co.kr/learn/courses/30/lessons/12937)

## 개요
> ### 문제
> 정수 `num`이 짝수일 경우 `"Even"`을 반환하고 홀수인 경우 `"Odd"`를 반환하는 함수, `solution`을 완성해주세요.
>
> 요약: 

> # 주요 제한사항
> .

<h1 align="center"><br><br><br>❗️❗️ 스포주의 ❗️❗️<br><br><br></h1>

## 풀이
### 접근
- 특별한 계산식 없이 바로 답이 둘 중 하나로 나오니까 삼항연산자 가능하겠다.

### 코드
```python
def solution(num):
    return "Even" if num % 2 == 0 else "Odd"

solution = lambda num: "Even" if num % 2 == 0 else "Odd"

# 닮고  싶은 코드
["Even", "Odd"][num & 1]
```

### 설명
1. `num & 1` 같이 비트연산자를 잘 다루면 좋을 거 같음
