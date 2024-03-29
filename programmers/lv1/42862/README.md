# [체육복](https://school.programmers.co.kr/learn/courses/30/lessons/42862)

## 개요
> ### 문제
> 점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다. 다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다. 학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다. 예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다. 체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.
> 
> 전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 `lost`, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 `reserve`가 매개변수로 주어질 때, 체육수업을 들을 수 있는 학생의 최댓값을 `return` 하도록 `solution` 함수를 작성해주세요.
>
> **요약**: 체육복을 도난당한 학생에게 여벌을 가져온 학생이 빌려줄 수 있는데 자신의 앞, 뒤 번호 학생에게만 빌려줄 수 있다. 최대한 많은 학생이 체육복을 입게하라

> ### 주요 제한사항
> .

<h1 align="center"><br><br><br>❗️❗️ 스포주의 ❗️❗️<br><br><br></h1>

## 풀이
### 접근
- 리스트화 해서 현재 체육복 현황 파악
- 재귀로 앞사람 빌려줬을 때, 뒷사람 빌려줬을 때 파악
- 둘 중 맥스 가져오기

### 코드
```python
def solution(n, lost, reserve):
    c = [1] * n
    for i in lost:
        c[i - 1] -= 1
    for i in reserve:
        c[i - 1] += 1

    def go(i, arr):
        if i == n:
            s = 0
            for j in arr:
                s += 1 if j else 0
            return s
        s1 = s2 = s3 = 0
        if arr[i] == 2:
            if i - 1 >= 0 and arr[i - 1] == 0:
                temp = [*arr]
                temp[i - 1] = temp[i] = 1
                s1 = go(i + 1, [*temp])
            if i + 1 < n and arr[i + 1] == 0:
                temp = [*arr]
                temp[i + 1] = temp[i] = 1
                s2 = go(i + 1, [*temp])
            else:
                s3 = go(i + 1, [*arr])
        else:
            s3 = go(i + 1, [*arr])
        return max(s1, s2, s3)

    answer = go(0, c)

    return answer
```

### 설명
1. `c`: 번호별 체육복 현황
2. `go` 함수를 돌면서 현재 체육복 상황에 맞춰 앞 뒤 번호에게 체육복 빌려준 상황을 시뮬레이션
3. `s1`: 왼쪽 사람에게 빌려준 경우
4. `s2`: 오른쪽 사람에게 빌려준 경우
5. `s3`: 빌려주지 않은 경우
6. `s1`, `s2`, `s3` 중 가장 많은 학생이 입은 경우 `return`

### 다른 사람 풀이 보고 느낀점
> 뭔가 내가 좀 복잡하게 푼 거 같다...