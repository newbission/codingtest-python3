# [A+B - 3](https://www.acmicpc.net/problem/10950)

## 개요
> ### 문제
> 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
> 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
>
> 요약: `T` 수만큼 주어지는 `A`와 `B`의 합을 출력

> ### 주요 제한사항
> .

<h1 align="center"><br><br><br>❗️❗️ 스포주의 ❗️❗️<br><br><br></h1>

## 풀이
### 접근
`T`만큼 반복해서 입력받고 출력

### 코드
```python
def solution():
    t = int(input())
    res = []
    for _ in range(t):
        res.append(sum(map(int, input().split())))

    return "\n".join(map(str,res))
```

### 설명
- 입력 받은 값을 `map`으로 `int`로 변환한 뒤 `sum`함수를 바로 적용해 더함

### 다른 사람 풀이 보고 느낀점
> .