# [최솟값 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/12941)

## 개요
> ### 문제
> 길이가 같은 배열 `A`, `B` 두개가 있습니다. 각 배열은 자연수로 이루어져 있습니다.
> 배열 `A`, `B`에서 각각 한 개의 숫자를 뽑아 두 수를 곱합니다. 이러한 과정을 배열의 길이만큼 반복하며, 두 수를 곱한 값을 누적하여 더합니다. 이때 최종적으로 누적된 값이 최소가 되도록 만드는 것이 목표입니다. (단, 각 배열에서 `k`번째 숫자를 뽑았다면 다음에 `k`번째 숫자는 다시 뽑을 수 없습니다.)
>
> 예를 들어 `A` = [1, 4, 2] , `B` = [5, 4, 4] 라면
> 
> `A`에서 첫번째 숫자인 1, `B`에서 첫번째 숫자인 5를 뽑아 곱하여 더합니다. (누적된 값 : 0 + 5(1x5) = 5)  
> `A`에서 두번째 숫자인 4, `B`에서 세번째 숫자인 4를 뽑아 곱하여 더합니다. (누적된 값 : 5 + 16(4x4) = 21)  
> `A`에서 세번째 숫자인 2, `B`에서 두번째 숫자인 4를 뽑아 곱하여 더합니다. (누적된 값 : 21 + 8(2x4) = 29)  
> 즉, 이 경우가 최소가 되므로 29를 `return` 합니다.
>
> 배열 `A`, `B`가 주어질 때 최종적으로 누적된 최솟값을 `return` 하는 `solution` 함수를 완성해 주세요.
>
> 요약: 두 배열 `A`, `B`에서 순서대로 숫자를 각각 뽑아서 곱한 값을 전부 더했을 때 가장 최소가 되게 하는 방법

> # 주요 제한사항
> .

<h1 align="center"><br><br><br>❗️❗️ 스포주의 ❗️❗️<br><br><br></h1>

## 풀이
### 접근
- 가장 큰거랑 가장 작은거 곱하면 최소
- 정렬 - 한 개는 오름차순, 한 개는 내림차순

### 코드
```python
def solution(A,B):
    A.sort()
    B.sort(reverse=True)

    return sum(a * b for a, b in zip(A, B))
    
    # 더 간략한 버전
    return sum(a * b for a, b in zip(sorted(A), sorted(B, reverse=True)))
```

### 설명
1. 두 리스트 정렬
2. 순서쌍으로 만들어서 하나씩 곱해주기
3. 더해서 리턴
