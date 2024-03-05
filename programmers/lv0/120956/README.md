# [옹알이 1](https://school.programmers.co.kr/learn/courses/30/lessons/120956)

## 개요
> [!NOTE] 문제
> 머쓱이는 태어난 지 6개월 된 조카를 돌보고 있습니다. 조카는 아직 `"aya", "ye", "woo", "ma"`네 가지 발음을 최대 한 번씩 사용해 조합한(이어 붙인) 발음밖에 하지 못합니다. 문자열 배열 `babbling`이 매개변수로 주어질 때, 머쓱이의 조카가 발음할 수 있는 단어의 개수를 `return`하도록 `solution` 함수를 완성해주세요.
>
> 요약: `babbling`에서 머쓱이가 발음 가능한 단어의 개수

> [!IMPORTANT] 주요 제한사항
> - `babbling`의 단어들은 머쓱이가 발음 가능한 발음들이 최대 1번씩만 등장한다.
> - 문자열은 알파벳 소문자로만 이루어져 있다.

# <center>❗️❗️ 스포주의 ❗️❗️<center>

## 풀이
> [!TIP] 접근
> - 부분문자열 찾는 문제
> - find, in, replace 떠오름

> [!WARNING] 풀이
> ```python
> words = ("aya", "ye", "woo", "ma")
>     answer = 0
>     for i in babbling:
>         for word in words:
>             if word in i:
>                 i = i.replace(word, " ")
>         if len(i.replace(" ", "")) == 0:
>             answer += 1
> ```
> 1. `babbling`의 각 단어들은 발음이 최대 한 번씩만 사용되므로 `words`를 순회하면서 포함된다면 공백으로 바꿔준다.  
>       - 공백이 아닌 빈칸으로 바꿀시 `yayae`같은 케이스가 통과됨
> 2. `words`를 순회하고 나온 단어의 공백을 제거해준다.
> 3. 단어의 길이가 0이라면 발음을 한 것이라고 판단하여 개수를 1 올린다.
>

