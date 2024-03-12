# [숫자의 표현](https://school.programmers.co.kr/learn/courses/30/lessons/12924)

## 개요
> ### 문제
> Finn은 요즘 수학공부에 빠져 있습니다. 수학 공부를 하던 Finn은 자연수 `n`을 연속한 자연수들로 표현 하는 방법이 여러개라는 사실을 알게 되었습니다. 예를들어 15는 다음과 같이 4가지로 표현 할 수 있습니다.
>
> - 1 + 2 + 3 + 4 + 5 = 15
> - 4 + 5 + 6 = 15
> - 7 + 8 = 15
> - 15 = 15
> 
> 자연수 `n`이 매개변수로 주어질 때, 연속된 자연수들로 `n`을 표현하는 방법의 수를 `return`하는 `solution`를 완성해주세요.
>
> 요약: `n`을 연속된 자연수들의 합으로 만드는 방법의 수

> # 주요 제한사항
> `n` <= 10,000

<h1 align="center"><br><br><br>❗️❗️ 스포주의 ❗️❗️<br><br><br></h1>

## 풀이
### 접근
- 1부터 `n`까지 다 해보면 되겠다

### 코드
```python
def solution(n):
    answer = 0
    for i in range(1, n+1):
        temp = 0
        while(temp < n):
            temp += i
            i += 1
        if temp == n:
            answer += 1

        # while 대신 방법
        for j in range(i, n+1):
            temp += j
            if temp >= n:
                answer += temp == n
                break
    return answer
```

### 설명
1. 시작 숫자를 1부터 `n`까지 순회
2. `temp`에 `i`부터 `n`보다 크거나 같아질때까지 더하기
3. `temp`가 `n`이랑 같으면 `answer`에 1추가
4. `while` 대신 `for`문으로 할 때:  
 $\to$ `answer += temp == n`: `temp`가 `n`이랑 같으면 `+1` 아니면 `+0`

### 다른 사람 풀이 보고 느낀점
> .
