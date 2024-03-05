# [가장 많이 받은 선물](https://school.programmers.co.kr//learn/courses/30/lessons/258712)

## 개요

> [!NOTE] 문제
> 선물을 직접 전하기 힘들 때 카카오톡 선물하기 기능을 이용해 축하 선물을 보낼 수 있습니다. 당신의 친구들이 이번 달까지 선물을 주고받은 기록을 바탕으로 다음 달에 누가 선물을 많이 받을지 예측하려고 합니다.
>
> 두 사람이 선물을 주고받은 기록이 있다면, 이번 달까지 두 사람 사이에 더 많은 선물을 준 사람이 다음 달에 선물을 하나 받습니다.  
> 예를 들어 `A`가 `B`에게 선물을 5번 줬고, `B`가 `A`에게 선물을 3번 줬다면 다음 달엔 `A`가 `B`에게 선물을 하나 받습니다.  
> 두 사람이 선물을 주고받은 기록이 하나도 없거나 주고받은 수가 같다면, 선물 지수가 더 큰 사람이 선물 지수가 더 작은 사람에게 선물을 하나 받습니다.  
> 선물 지수는 이번 달까지 자신이 친구들에게 준 선물의 수에서 받은 선물의 수를 뺀 값입니다.  
> 예를 들어 `A`가 친구들에게 준 선물이 3개고 받은 선물이 10개라면 `A`의 선물 지수는 -7입니다. `B`가 친구들에게 준 선물이 3개고 받은 선물이 2개라면 `B`의 선물 지수는 1입니다. 만약 `A`와 `B`가 선물을 주고받은 적이 없거나 정확히 같은 수로 선물을 주고받았다면, 다음 달엔 `B`가 `A`에게 선물을 하나 받습니다.  
> 만약 두 사람의 선물 지수도 같다면 다음 달에 선물을 주고받지 않습니다.  
> 위에서 설명한 규칙대로 다음 달에 선물을 주고받을 때, 당신은 선물을 가장 많이 받을 친구가 받을 선물의 수를 알고 싶습니다.
>
> 친구들의 이름을 담은 1차원 문자열 배열 `friends` 이번 달까지 친구들이 주고받은 선물 기록을 담은 1차원 문자열 배열 `gifts`가 매개변수로 주어집니다. 이때, 다음달에 가장 많은 선물을 받는 친구가 받을 선물의 수를 `return` 하도록 `solution` 함수를 완성해 주세요.
>
> 요약: 규칙에 맞게 선물을 주고받을 때 가장 많은 선물을 받는 사람의 선물 개수  
> [규칙]
> 1. 둘 중 주고 받은 선물이 더 많은 사람이 받는다.
> 2. 두 사람이 주고 받은 선물 수가 같다면 선물 지수가 더 큰 사람이 받는다.
> 3. 선물 지수마저 같다면 주고 받지 않는다.
> 4. 선물 지수는 주면 `+1`, 받으면 `-1`이다.

> [!IMPORTANT] 주요 제한사항
> `gifts`의 원소는 `"A B"` 형식이고 `A`와 `B`는 같은 이름이 아니다.

# <center>❗️❗️ 스포주의 ❗️❗️<center>

## 풀이

> [!TIP] 접근
> - 선물 지수가 필요하므로 리스트로 만들기
> - 주고 받은 수를 파악하기 위해 리스트 or 딕셔너리로 만들기

> [!WARNING] 풀이
>
> ```python
> def solution(friends, gifts):
>     size = len(friends)
>     friends_index = {}
>     total_gift_score = [0] * size
>     gift_list = [[0 for _ in range(size)] for _ in range(size)]
>     result = [0] * size
> 
>     for i in range(size):
>         friends_index[friends[i]] = i
>     
>     for gift in gifts:
>         a, b = gift.split(' ')
> 
>         # 선물지수 수정
>         total_gift_score[friends_index[a]] += 1
>         total_gift_score[friends_index[b]] -= 1
> 
>         # 선물 준 것만 카운트
>         gift_list[friends_index[a]][friends_index[b]] += 1
> 
>     
>     for i in range(size-1): # size-1: 마지막 사람은 어차피 비교 대상이 없음
>         for j in range(i+1, size): # i+1: 굳이 두번 돌 필요가 없음
>             if i == j: continue
> 
>             # 주고 받은 선물 수가 같다면 선물지수 비교
>             if gift_list[i][j] == gift_list[j][i]:
>                 result[i] += total_gift_score[i] > total_gift_score[j]
>                 result[j] += total_gift_score[j] > total_gift_score[i]
> 
>             # 더 많이 준 사람이 받기
>             elif gift_list[i][j] > gift_list[j][i]:
>                 result[i] += 1
>             else:
>                 result[j] += 1
>     return max(result)
> ```
> > - `friends_index`: 배열 `index`에 대한 정보
> > - `total_gift_score`: 선물 지수
> > - `gift_list`: 각자 친구에게 준 선물 개수
> > - `result`: 다음 달 받을 선물 수
>
> 1. `gifts`를 토대로 준 선물 개수, 선물 지수 파악
> 2. 파악한 결과를 토대로 `result`에 받을 선물 개수 카운트
> 3. `result`에서 최대값 구하기