# [배열 조각하기](https://school.programmers.co.kr/learn/courses/30/lessons/181893)

## 개요
> ### 문제
> 정수 배열 `arr`와 `query`가 주어집니다.
> 
> `query`를 순회하면서 다음 작업을 반복합니다.
> 
> - 짝수 인덱스에서는 `arr`에서 `query[i]`번 인덱스를 제외하고 배열의 `query[i]`번 인덱스 뒷부분을 잘라서 버립니다.
> - 홀수 인덱스에서는 `arr`에서 `query[i]`번 인덱스는 제외하고 배열의 `query[i]`번 인덱스 앞부분을 잘라서 버립니다.
> 
> 위 작업을 마친 후 남은 `arr`의 부분 배열을 `return` 하는 `solution` 함수를 완성해 주세요.
>
> 요약: 인덱스 `idx`가 있을 때 `i = query[idx]`라고 한다면 `idx`가 짝수면 `arr`의 `i`번 인덱스 뒷부분을, 음수면 `i`번 인덱스 앞부분을 자르기 

> # 주요 제한사항
> .

<h1 align="center"><br><br><br>❗️❗️ 스포주의 ❗️❗️<br><br><br></h1>

## 풀이
### 접근
- `arr`을 기준과 규칙에 맞게 슬라이싱하기

### 코드
```python
def solution(arr, query):
    for idx, i in enumerate(query):
        if idx % 2 == 0:
            arr = arr[:i+1]
        else:
            arr = arr[i:]
    return arr
```

### 설명
1. `enumerate`를 통해 `query`의 각 인덱스는 `idx`에 저장
2. `idx`를 통해 짝수면 뒤에거, 음수면 앞에서 자르기

### 다른 사람 풀이 보고 느낀점
> .
