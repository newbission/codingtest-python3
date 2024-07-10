# [로또의 최고 순위와 최저 순위](https://school.programmers.co.kr/learn/courses/30/lessons/77484)

## 개요
> ### 문제
> `로또 6/45`(이하 '로또'로 표기)는 1부터 45까지의 숫자 중 6개를 찍어서 맞히는 대표적인 복권입니다. 아래는 로또의 순위를 정하는 방식입니다.
> 
> | 순위    | 당첨 내용            |
> | ------- | -------------------- |
> | 1       | 6개 번호가 모두 일치 |
> | 2       | 5개 번호가 일치      |
> | 3       | 4개 번호가 일치      |
> | 4       | 3개 번호가 일치      |
> | 5       | 2개 번호가 일치      |
> | 6(낙첨) | 그 외                |
> 
> 로또를 구매한 민우는 당첨 번호 발표일을 학수고대하고 있었습니다. 하지만, 민우의 동생이 로또에 낙서를 하여, 일부 번호를 알아볼 수 없게 되었습니다. 당첨 번호 발표 후, 민우는 자신이 구매했던 로또로 당첨이 가능했던 최고 순위와 최저 순위를 알아보고 싶어 졌습니다.  
> 알아볼 수 없는 번호를 `0`으로 표기하기로 하고, 민우가 구매한 로또 번호 6개가 `44, 1, 0, 0, 31, 25`라고 가정해보겠습니다. 당첨 번호 6개가 `31, 10, 45, 1, 6, 19`라면, 당첨 가능한 최고 순위와 최저 순위의 한 예는 아래와 같습니다.
> 
> | 당첨 번호      | 31  | 10   | 45  | 1   | 6   | 19  | 결과               |
> | -------------- | --- | ---- | --- | --- | --- | --- | ------------------ |
> | 최고 순위 번호 | 31  | 0→10 | 44  | 1   | 0→6 | 25  | 4개 번호 일치, 3등 |
> | 최저 순위 번호 | 31  | 0→11 | 44  | 1   | 0→7 | 25  | 2개 번호 일치, 5등 |
> 
> - 순서와 상관없이, 구매한 로또에 당첨 번호와 일치하는 번호가 있으면 맞힌 걸로 인정됩니다.
> - 알아볼 수 없는 두 개의 번호를 각각 10, 6이라고 가정하면 3등에 당첨될 수 있습니다.
>   - 3등을 만드는 다른 방법들도 존재합니다. 하지만, 2등 이상으로 만드는 것은 불가능합니다.
> - 알아볼 수 없는 두 개의 번호를 각각 11, 7이라고 가정하면 5등에 당첨될 수 있습니다.
> 5등을 만드는 다른 방법들도 존재합니다. 하지만, 6등(낙첨)으로 만드는 것은 불가능합니다.
> 
> 민우가 구매한 로또 번호를 담은 배열 `lottos`, 당첨 번호를 담은 배열 `win_nums`가 매개변수로 주어집니다. 이때, 당첨 가능한 최고 순위와 최저 순위를 차례대로 배열에 담아서 `return` 하도록 `solution` 함수를 완성해주세요.
> 
> 
>
> **요약**: 로또에 지워진 부분이 존재 할 때 지워지지 않은 부분과 지워진 부분을 조합해서 해당 로또의 최고 순위와 최저 순위를 구하기.  
> 지워진 부분은:`0`

> ### 주요 제한사항
> .

<h1 align="center"><br><br><br>❗️❗️ 스포주의 ❗️❗️<br><br><br></h1>

## 풀이
### 접근
- `0`을 제외한 숫자들의 맞은 개수를 구한 뒤 `0`의 개수를 더하거나 빼자

### 코드
```python
def solution(lottos, win_nums):
    z = lottos.count(0)
    cnt = 7
    lottos.sort()
    for i in lottos[z:]:
        if i in win_nums:
            cnt -= 1

    return [min(6, cnt - z), min(6, cnt)]
```

### 설명
1. `z`: `0`의 개수
2. `cnt`: 순위를 계산할 때 맞이 맞으면 숫자가 낮아지므로 `7`에서 시작
   1. `7`인 이유는 계산하기 편함
3. 배열을 순회할 때 순서대로 하려고 정렬 $\to$ 지금 생각해보니 굳이?
4. `for i in lottos[z:]`: 0이 아닌 부분 부터 시작
5. `min(6, ~)`: 만약 같은 것이 없거나 전부 `0`이면 `cnt`가 `7`이 되기 때문에 최대를 `6`으로 설정

### 다른 사람 풀이 보고 느낀점
> .