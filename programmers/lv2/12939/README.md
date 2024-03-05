# [최댓값과 최솟값](https://school.programmers.co.kr/learn/courses/30/lessons/12939)

## 개요
> [!NOTE] 문제
> 문자열 s에는 공백으로 구분된 숫자들이 저장되어 있습니다. str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 "(최소값) (최대값)"형태의 문자열을 반환하는 함수, solution을 완성하세요.
> 예를들어 s가 "1 2 3 4"라면 "1 4"를 리턴하고, "-1 -2 -3 -4"라면 "-4 -1"을 리턴하면 됩니다.
>
> 요약: 입력된 숫자 문자열 내의 최솟값과 최댓값 구하기

> [!IMPORTANT] 주요 제한사항
> .

# <center>❗️❗️ 스포주의 ❗️❗️<center>

## 풀이
> [!TIP] 접근
> - 공백을 기준으로 숫자들이 주어지므로 `split` 떠오름
> - 최소값, 최대값 $\to$ `max`, `min` 사용

> [!WARNING] 풀이
> ```python
> def solution(s):
>     split_s = list(map(int, s.split()))
>     return f"{min(split_s)} {max(split_s)}"
> ```
> 1. 주어진 문자열을 공백을 기준으로 나누면서 숫자 형식으로 변환하여 `list`로 저장
> 2. `list`의 최소, 최대값 구해서 리턴