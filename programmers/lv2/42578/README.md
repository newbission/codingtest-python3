# [의상](https://school.programmers.co.kr/learn/courses/30/lessons/42578)

## 개요
> ### 문제
> 코니는 매일 다른 옷을 조합하여 입는것을 좋아합니다.
> 
> 예를 들어 코니가 가진 옷이 아래와 같고, 오늘 코니가 동그란 안경, 긴 코트, 파란색 티셔츠를 입었다면 다음날은 청바지를 추가로 입거나 동그란 안경 대신 검정 선글라스를 착용하거나 해야합니다.
> 
> | 종류 | 이름                       |
> | ---- | -------------------------- |
> | 얼굴 | 동그란 안경, 검정 선글라스 |
> | 상의 | 파란색 티셔츠              |
> | 하의 | 청바지                     |
> | 겉옷 | 긴 코트                    |
> 
> * 코니는 각 종류별로 최대 1가지 의상만 착용할 수 있습니다. 예를 들어 위 예시의 경우 동그란 안경과 검정 선글라스를 동시에 착용할 수는 없습니다.
> * 착용한 의상의 일부가 겹치더라도, 다른 의상이 겹치지 않거나, 혹은 의상을 추가로 더 착용한 경우에는 서로 다른 방법으로 옷을 착용한 것으로 계산합니다.
> * 코니는 하루에 최소 한 개의 의상은 입습니다.
> 
> 코니가 가진 의상들이 담긴 2차원 배열 `clothes`가 주어질 때 서로 다른 옷의 조합의 수를 `return` 하도록 `solution` 함수를 작성해주세요.
>
> **요약**: 코니가 최소 1개 이상의 의상을 입고, 의상은 종류별로 한 개씩만 입을 수 있을 때 주어진 `clothes`에서 가능한 조합의 개수

> ### 주요 제한사항
> - `clothes`의 각 행은 `[의상의 이름, 의상의 종류]`로 이루어져 있습니다.
> - 같은 이름을 가진 의상은 존재하지 않습니다.

<h1 align="center"><br><br><br>❗️❗️ 스포주의 ❗️❗️<br><br><br></h1>

## 풀이
### 접근
- 옷을 종류별로 구분하고 개수만큼 곱한거랑, 개수만큼 더하기 $\to$ 안 입는 것을 고려하지 않음
- 찾아보니 의상의 개수에 안 입는 경우를 `+1` 해서 전부 곱한 뒤 모두 안 입는 경우만 빼서 곱하면 된다함

### 코드
```python
def solution(clothes):
    category = {}
    for i, c in clothes:
        if not c in category:
            category[c] = 1
        category[c] += 1
    res = 1
    for n in category.values():
        res *= n
    return res - 1
```

### 설명
1. `category`에 `clothes`에서 주어진 의상의 카테고리별로 개수 세기
2. `if not c in category: category[c] = 1`: 카테고리가 없다면 카테고리를 추가하고 안 입는 경우를 위해 `+1`
3. `res`에 강 의상 개수 곱해주고 `-1`해서 리턴

### 다른 사람 풀이 보고 느낀점
> 안 입는 경우도 한가지 경우다!!