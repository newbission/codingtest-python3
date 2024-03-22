# [\[PCCE 기출문제\] 9번 - 이웃한 칸](https://school.programmers.co.kr/learn/courses/30/lessons/250125)

## 개요
> ### 문제
> 칸의 개수를 구하려고 합니다.
> 
> 보드의 각 칸에 칠해진 색깔 이름이 담긴 이차원 문자열 리스트 `board`와 고른 칸의 위치를 나타내는 두 정수 `h`, `w`가 주어질 때 `board[h][w]`와 이웃한 칸들 중 같은 색으로 칠해져 있는 칸의 개수를 return 하도록 solution 함수를 완성해 주세요.
> 
> 이웃한 칸들 중 몇 개의 칸이 같은 색으로 색칠되어 있는지 확인하는 과정은 다음과 같습니다.
>
> ```
> 1. 정수를 저장할 변수 n을 만들고 board의 길이를 저장합니다.
> 2. 같은 색으로 색칠된 칸의 개수를 저장할 변수 count를 만들고 0을 저장합니다.
> 3. h와 w의 변화량을 저장할 정수 리스트 dh, dw를 만들고 각각 [0, 1, -1, 0], [1, 0, 0, -1]을 저장합니다.
> 4. 반복문을 이용해 i 값을 0부터 3까지 1 씩 증가시키며 아래 작업을 반복합니다.
>     4-1. 체크할 칸의 h, w 좌표를 나타내는 변수 h_check, w_check를 만들고 각각 h + dh[i], w + dw[i]를 저장합니다.
>     4-2. h_check가 0 이상 n 미만이고 w_check가 0 이상 n 미만이라면 다음을 수행합니다.
>         4-2-a. board[h][w]와 board[h_check][w_check]의 값이 동일하다면 count의 값을 1 증가시킵니다.
> 5. count의 값을 return합니다.
> ```
>
> -   위의 의사코드와 작동방식이 다른 코드를 작성해도 상관없습니다.
>
> 요약: 주어진 좌표의 상하좌우 칸을 비교해 색상이 같은 칸의 개수 구하기

> # 주요 제한사항
> .

<h1 align="center"><br><br><br>❗️❗️ 스포주의 ❗️❗️<br><br><br></h1>

## 풀이
### 접근
- 주어진 좌표의 상하좌우만 구하면 되니까 `dy`, `dx`로 탐색해서 비교하자

### 코드
```python
def solution(board, h, w):
    answer = 0
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    color = board[h][w]
    n = len(board)
    for i in range(4):
        ny, nx = h+dy[i], w+dx[i]
        if 0 <= ny < n and 0 <= nx < n and board[ny][nx] == color:
            answer += 1
    return answer
```

### 설명
1. `dy`, `dx`를 각각 생성
2. `ny`, `nx`를 구해서 `board` 범위 안에 들어오고, 색이 같다면 `answer += 1`

### 다른 사람 풀이 보고 느낀점
> .
