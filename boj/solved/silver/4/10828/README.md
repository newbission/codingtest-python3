# [스택](https://www.acmicpc.net/problem/10828)

## 개요
> ### 문제
> 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
> 
> 명령은 총 다섯 가지이다.
> 
> - `push X`: 정수 X를 스택에 넣는 연산이다.
> - `pop`: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
> - `size`: 스택에 들어있는 정수의 개수를 출력한다.
> - `empty`: 스택이 비어있으면 1, 아니면 0을 출력한다.
> - `top`: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
>
> ### 입력
> 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.
>
> ### 출력
> 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.
>
> 요약: 첫줄에 주어지는 `N`개의 명령에 대한 처리를 한 뒤 적절히 출력한다.

> ### 주요 제한사항
> - $1 ≤ N ≤ 10,000$

<h1 align="center"><br><br><br>❗️❗️ 스포주의 ❗️❗️<br><br><br></h1>

## 풀이
### 접근
- 각 커맨드를 if 문으로 구분해서 결과 저장

### 코드
```python
n = int(input())
stack = []
res = []
for _ in range(n):
    cmd = input()
    if cmd == 'top':
        res.append(stack[-1] if len(stack) else '-1')
    elif cmd == 'empty':
        res.append('0' if len(stack) else '1')
    elif cmd == 'size':
        res.append(str(len(stack)))
    elif cmd == 'pop':
        res.append(stack.pop() if len(stack) else '-1')
    else:
        stack.append(cmd[5:])

print('\n'.join(res))
```

### 설명
- 각 명령에 대해 조건을 걸어서 `res`에 저장한 뒤 한번에 출력

### 다른 사람 풀이 보고 느낀점
> .