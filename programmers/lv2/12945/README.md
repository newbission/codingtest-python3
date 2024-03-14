# [파보나치 수](https://school.programmers.co.kr/learn/courses/30/lessons/12945)

## 개요
> ### 문제
> 피보나치 수는 `F(0) = 0`, `F(1) = 1`일 때, 1 이상의 n에 대하여 `F(n) = F(n-1) + F(n-2)` 가 적용되는 수 입니다.
> 
> 예를들어
> - F(2) = F(0) + F(1) = 0 + 1 = 1
> - F(3) = F(1) + F(2) = 1 + 1 = 2
> - F(4) = F(2) + F(3) = 1 + 2 = 3
> - F(5) = F(3) + F(4) = 2 + 3 = 5
> 
> 와 같이 이어집니다.
> 
> 2 이상의 `n`이 입력되었을 때, `n`번째 피보나치 수를 `1234567`으로 나눈 나머지를 리턴하는 함수, `solution`을 완성해 주세요.
>
> 요약: `n`번째 파보나치 수를 `1234567`로 나눈 나머지

> # 주요 제한사항
> `n`은 10만 이하 자연수

<h1 align="center"><br><br><br>❗️❗️ 스포주의 ❗️❗️<br><br><br></h1>

## 풀이
### 접근
- `n`까지 파보나치 수 구해서 `1234567`로 나눠야 겠다.

### 코드
```python
def solution(n):
    f = [None] * (n + 1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n + 1):
        f[i] = (f[i-1] + f[i-2]) % 1234567
    
    return f[n]
```

### 설명
1. `f(n)`을 구할 때 `1234567`을 나눈 나머지를 저장
   1. 모듈러 연산($a ≡ b \mod n과\ b ≡ c \mod n 은\ a ≡ c \mod n$) 적용
   2. $[(a \mod n)+(b \mod n)] \mod n = (a+b)\mod n$
   3. $[(a \mod n)-(b \mod n)] \mod n = (a-b) \mod n$
   4. $[(a \mod n)*(b \mod n)] \mod n = (a*b) \mod n$
   5. [출처 | 큰돌](https://blog.naver.com/jhc9639)
