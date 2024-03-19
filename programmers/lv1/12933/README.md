# [정수 내림차순으로 배치하기](https://school.programmers.co.kr/learn/courses/30/lessons/12933)

## 개요
> ### 문제
> 함수 `solution`은 정수 `n`을 매개변수로 입력받습니다. `n`의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 예를들어 `n`이 `118372`면 `873211`을 리턴하면 됩니다.
>
> 요약: 정수 `n`의 각 자리수를 내림차순으로 바꾸기

> # 주요 제한사항
> .

<h1 align="center"><br><br><br>❗️❗️ 스포주의 ❗️❗️<br><br><br></h1>

## 풀이
### 접근
- 문자열 변환 $\to$ 배열화 $\to$ 정렬 $\to$ 조인 $\to$ 숫자 변환

### 코드
```python
solution = lambda n: int(''.join(sorted(list(str(n)), reverse=True)))
```

### 설명
1. 숫자를 문자열로 변경 후 배열로 만들고 정렬을 해서 문자열로 만든 뒤 숫자로 변환

### 다른 사람 풀이 보고 느낀점
```python
solution = lambda n: int(''.join(sorted(str(n), reverse=True)))
```
> 문자열을 `sorted` 하면 자동으로 배열을 해서 배열화 할 필요가 없음
