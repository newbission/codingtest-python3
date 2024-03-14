# [주사위 게임 3](https://school.programmers.co.kr/learn/courses/30/lessons/181916)

## 개요
> ### 문제
> 1부터 6까지 숫자가 적힌 주사위가 네 개 있습니다. 네 주사위를 굴렸을 때 나온 숫자에 따라 다음과 같은 점수를 얻습니다.  
> - 네 주사위에서 나온 숫자가 모두 `p`로 같다면 `1111 × p`점을 얻습니다.  
> - 세 주사위에서 나온 숫자가 `p`로 같고 나머지 다른 주사위에서 나온 숫자가 `q(p ≠ q)`라면 `(10 × p + q)2` 점을 얻습니다.  
> - 주사위가 두 개씩 같은 값이 나오고, 나온 숫자를 각각 `p`, `q(p ≠ q)`라고 한다면 `(p + q) × |p - q|`점을 얻습니다.  
> - 어느 두 주사위에서 나온 숫자가 `p`로 같고 나머지 두 주사위에서 나온 숫자가 각각 `p`와 다른 `q, r(q ≠ r)`이라면 `q × r`점을 얻습니다.  
> - 네 주사위에 적힌 숫자가 모두 다르다면 나온 숫자 중 가장 작은 숫자 만큼의 점수를 얻습니다.  
> 
> 네 주사위를 굴렸을 때 나온 숫자가 정수 매개변수 `a`, `b`, `c`, `d`로 주어질 때, 얻는 점수를 `return` 하는 `solution` 함수를 작성해 주세요.
>
> 요약: 주사위를 굴렸을 때 나오는 숫자를 보고 규칙에 맞게 결과를 도출하기

> # 주요 제한사항
> .

<h1 align="center"><br><br><br>❗️❗️ 스포주의 ❗️❗️<br><br><br></h1>

## 풀이
### 접근
- `set`으로 만들어서 숫자 추리기
- `list`로 만들어서 해보기
- `len 1`: `1111 X a`
- `len 2`:
  - 3개 1개 경우: 
  - 2개 2개 경우: 

### 코드
```python
def solution(a, b, c, d):
    dice = set([a, b, c, d])
    dice_dict = {key: 0 for key in dice}
    dice_dict[a] += 1
    dice_dict[b] += 1
    dice_dict[c] += 1
    dice_dict[d] += 1

    size = len(dice)

    if size == 1:
        return 1111 * a
    
    if size == 2:
        a, b = dice
        if dice_dict[a] == 2:
            return (a + b) * abs(a - b)
        p, q = [a, b] if dice_dict[a] == 3 else [b, a]
        return (10 * p + q) ** 2

    if size == 3:
        a, b, c = dice
        q, r = [a, b] if dice_dict[c] == 2 else [a, c] if dice_dict[b] == 2 else [b, c]
        return q * r
    
    return min(dice)
```

### 설명
1. 주어진 `a`, `b`, `c`, `d`의 가짓수를 파악하기 위해 `set`으로 줄이기
2. a`, `b`, `c`, `d`가 각각 몇개 들어왔는지 `dict`로 파악
3. 각 상황에 맞게 구하기

### 다른 사람 풀이 보고 느낀점
```python
def solution(a, b, c, d):
    l = [a,b,c,d]
    c = [l.count(x) for x in l]
    if max(c) == 4:
        return 1111*a
    elif max(c) == 3:
        return (10*l[c.index(3)]+l[c.index(1)])**2
    elif max(c) == 2:
        if min(c) == 1:
            return eval('*'.join([str(l[i]) for i, x in enumerate(c) if x == 1]))
        else:
            return (max(l) + min(l)) * abs(max(l) - min(l))
    else:
        return min(l)
```
> - `count`를 사용해서 넣는 것이 인상적이었음
> - 아직 `min`, `max`를 잘 활용 못하는게 아쉬움
> - 무언가 코드를 더 줄일 수 있다고 생각했는데 실제로 가능한 걸 발견해서 좋았음
> - 왜 `a`, `b`, `c`, `d`를 `list`화 하면 별로라고 생각했는지 모르겠음
