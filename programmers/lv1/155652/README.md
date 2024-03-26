# [둘만의 암호](https://school.programmers.co.kr/learn/courses/30/lessons/155652)

## 개요
> ### 문제
> 두 문자열 `s`와 `skip`, 그리고 자연수 `index`가 주어질 때, 다음 규칙에 따라 문자열을 만들려 합니다. 암호의 규칙은 다음과 같습니다.
> 
> - 문자열 `s`의 각 알파벳을 `index`만큼 뒤의 알파벳으로 바꿔줍니다.
> - `index`만큼의 뒤의 알파벳이 `z`를 넘어갈 경우 다시 `a`로 돌아갑니다.
> - `skip`에 있는 알파벳은 제외하고 건너뜁니다.
> 
> 예를 들어 `s = "aukks"`, `skip = "wbqd"`, `index = 5`일 때, `a`에서 5만큼 뒤에 있는 알파벳은 `f`지만 `[b, c, d, e, f]`에서 `'b'`와 `'d'`는 `skip`에 포함되므로 세지 않습니다. 따라서 `'b'`, `'d'`를 제외하고 `'a'`에서 5만큼 뒤에 있는 알파벳은 `[c, e, f, g, h]` 순서에 의해 `'h'`가 됩니다. 나머지 `"ukks"` 또한 위 규칙대로 바꾸면 `"appy"`가 되며 결과는 `"happy"`가 됩니다.
> 
> 두 문자열 `s`와 `skip`, 그리고 자연수 `index`가 매개변수로 주어질 때 위 규칙대로 s를 변환한 결과를 `return`하도록 `solution` 함수를 완성해주세요.
>
> 요약: `s`의 각 알파벳을 `index`만큼 뒤에 오는 알파벳으로 교환하는데 이 사이에 `skip`에 포함된 알파벳이 나오면 그 수만큼 더 뒤로 간다. 이 때 `z`를 넘어가면 다시 `a`로 간다.

> # 주요 제한사항
> .

<h1 align="center"><br><br><br>❗️❗️ 스포주의 ❗️❗️<br><br><br></h1>

## 풀이
### 접근
- 알파벳을 `skip`을 제외하고 리스트로 만들기
- `index()`로 접근해서 해당 알파벳 찾기

### 코드
```python
def solution(s, skip, index):
    alpha = [chr(i) for i in range(97, 97+26) if chr(i) not in skip]
    answer = ''
    for c in s:
        answer += alpha[(alpha.index(c) + index) % len(alpha)]
        
    return answer
```

### 설명
1. `alpha`: `skip`에 있는 알파벳을 제외한 알파벳 리스트
2. `s`를 순회하면서 인덱스를 가지고 치환할 알파벳을 찾아  `answer`에 추가하기

### 다른 사람 풀이 보고 느낀점
> .
