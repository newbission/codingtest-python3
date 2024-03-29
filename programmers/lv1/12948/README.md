# [핸드폰 번호 가리기](https://school.programmers.co.kr/learn/courses/30/lessons/12948)

## 개요
> ### 문제
> 프로그래머스 모바일은 개인정보 보호를 위해 고지서를 보낼 때 고객들의 전화번호의 일부를 가립니다.  
> 전화번호가 문자열 `phone_number`로 주어졌을 때, 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 `*`으로 가린 문자열을 리턴하는 함수, `solution`을 완성해주세요.
>
> **요약**: 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 `*`으로 바꾸기

> ### 주요 제한사항
> .

<h1 align="center"><br><br><br>❗️❗️ 스포주의 ❗️❗️<br><br><br></h1>

## 풀이
### 접근
- 원래 번호 길이를 토대로 뒤에 4자리 빼고 `*`을 입력하고 뒤에 4자리 붙이기

### 코드
```python
def solution(phone_number):
    return "*" * (len(phone_number) - 4) + phone_number[-4:]
```

### 설명
1. `phone_number` 길이에서 4 뺀만큼 `*` 찍어주기
2. `phone_number` 마지막 4자리 붙여주기

### 다른 사람 풀이 보고 느낀점
> .
