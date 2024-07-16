# [에디터](https://www.acmicpc.net/problem/1406)

## 개요
> ### 문제
> 한 줄로 된 간단한 에디터를 구현하려고 한다. 이 편집기는 영어 소문자만을 기록할 수 있는 편집기로, 최대 600,000글자까지 입력할 수 있다.
> 
> 이 편집기에는 '커서'라는 것이 있는데, 커서는 문장의 맨 앞(첫 번째 문자의 왼쪽), 문장의 맨 뒤(마지막 문자의 오른쪽), 또는 문장 중간 임의의 곳(모든 연속된 두 문자 사이)에 위치할 수 있다. 즉 길이가 L인 문자열이 현재 편집기에 입력되어 있으면, 커서가 위치할 수 있는 곳은 L+1가지 경우가 있다.
> 
> 이 편집기가 지원하는 명령어는 다음과 같다.
> 
> | 명령어 | 설명                                                                                                                                                                    |
> | :----: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> |  `L`   | 커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)                                                                                                             |
> |  `D`   | 커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)                                                                                                           |
> |  `B`   | 커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨) <br> 삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 실제로 커서의 오른쪽에 있던 문자는 그대로임 |
> | `P $`  | `$`라는 문자를 커서 왼쪽에 추가함                                                                                                                                       |
> 
> 초기에 편집기에 입력되어 있는 문자열이 주어지고, 그 이후 입력한 명령어가 차례로 주어졌을 때, 모든 명령어를 수행하고 난 후 편집기에 입력되어 있는 문자열을 구하는 프로그램을 작성하시오. 단, 명령어가 수행되기 전에 커서는 문장의 맨 뒤에 위치하고 있다고 한다.
>
> ### 입력
> 첫째 줄에는 초기에 편집기에 입력되어 있는 문자열이 주어진다. 이 문자열은 길이가 $이고, 영어 소문자로만 이루어져 있으며, 길이는 $100,000$을 넘지 않는다. 둘째 줄에는 입력할 명령어의 개수를 나타내는 정수 $M(1 ≤ M ≤ 500,000)$이 주어진다. 셋째 줄부터 M개의 줄에 걸쳐 입력할 명령어가 순서대로 주어진다. 명령어는 위의 네 가지 중 하나의 형태로만 주어진다.
>
> ### 출력
> 첫째 줄에 모든 명령어를 수행하고 난 후 편집기에 입력되어 있는 문자열을 출력한다.
> ### 요약
> 처음 문자열이 주어질 때 명령어 대로 처리하고 난 뒤에 편집기에 입력되어 있는 문자열을 출력하라

> ### 주요 제한사항
> - 문자열 길이: $100,000$
> - 명령어의 개수 $M$: $1 ≤ M ≤ 500,000$

<h1 align="center"><br><br><br>❗️❗️ 스포주의 ❗️❗️<br><br><br></h1>

## 풀이
### 접근
- 연결리스트를 통해 현재 위치 파악후 명령어 처리
- 기능은 맞게 구현했지만 시간초과로 `stdin` 사용

### 코드
```python
from sys import stdin
def solution():
    class Node:
        def __init__(self, value, prev=None, next=None):
            self.value = value
            self.prev = prev
            self.next = next

            if prev:
                prev.next = self
            if next:
                next.prev = self

    start = Node(None)
    now = start

    s = input()
    for c in s:
        new = Node(c, now)
        now = new

    n = int(input())
    for _ in range(n):
        cmd = stdin.readline().rstrip()

        if cmd == "L" and now != start:
            now = now.prev
        elif cmd == "D" and now.next:
            now = now.next
        elif cmd == "B" and now != start:
            prev = now.prev
            next = now.next
            if prev:
                prev.next = next
            if next:
                next.prev = prev
            now = prev
        elif cmd[0] == "P":
            new = Node(cmd[2], now, now.next)
            now = new
            

    now = start.next
    res = ""

    while now:
        res += now.value
        now = now.next

    print(res)
```

### 설명
> 커서가 글자의 왼쪽, 오른쪽에 위치할 수 있는데 명령어는 커서의 왼쪽 글자를 지우므로 현재 글자(노드)가 커서의 위치라고 가정, 커서가 맨 앞으로 가는 경우를 대비해 `start`를 빈 노드로 생성해 지정

```python
class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

        if prev:
            prev.next = self
        if next:
            next.prev = self
```
`Node`를 직접 구현해 연결리스트의 각 노드로 사용

```python
s = input()
for c in s:
    new = Node(c, now)
    now = new
```
초기에 입력되어있는 문자열의 각 문자들을 노드화해서 연결리스트로 구성

```python
for _ in range(n):
    cmd = stdin.readline().rstrip()

    if cmd == "L" and now != start:
        now = now.prev
    elif cmd == "D" and now.next:
        now = now.next
    elif cmd == "B" and now != start:
        prev = now.prev
        next = now.next
        if prev:
            prev.next = next
        if next:
            next.prev = prev
        now = prev
    elif cmd[0] == "P":
        new = Node(cmd[2], now, now.next)
        now = new
```
명령어에 해당하는 기능 수행

```python
from sys import stdin
cmd = stdin.readline().rstrip()
``` 
명령어가 많으면 `input`으로는 속도에 한계가 있어 시간초과가 나므로 `stdin` 사용

```python
now = start.next
res = ""

while now:
    res += now.value
    now = now.next
```
`start`는 빈 노드이므로 `start`의 다음 노드부터 `res`에 저장

### 다른 사람 풀이 보고 느낀점
> 스택을 사용해 현재 커서 왼쪽에 있는 것은 `stack1`에 넣고 커서 오른쪽에 위치한 것은 `stack2`에 넣어서 마지막에 둘을 합치는 방법도 더 빠르고 간편한 거 같다.
>
> 하지만 이 방법은 문제가 원하는 방식은 아닌듯