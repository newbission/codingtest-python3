# [다음에 올 숫자](https://school.programmers.co.kr/learn/courses/30/lessons/120924)

## 개요
> ### 문제
> 등차수열 혹은 등비수열 `common`이 매개변수로 주어질 때, 마지막 원소 다음으로 올 숫자를 `return` 하도록 `solution` 함수를 완성해보세요.
>
> 요약: 

> # 주요 제한사항
> - 공비가 0인 경우는 없다.

<h1 align="center"><br><br><br>❗️❗️ 스포주의 ❗️❗️<br><br><br></h1>

## 풀이
### 접근
- 등차 구해보고 아니면 등비로 반환

### 코드
```python
def solution(common):
    if common[2] - common[1] == common[1] - common[0]:
        return common[-1] + (common[2] - common[1])
    
    return common[-1] * (common[2] / common[1])
```

### 설명
1. 두 구간을 빼보고 등차면 마지막 값에 등차 적용, 아니면 등비 적용해서 결과 도출

### 다른 사람 풀이 보고 느낀점
> .
