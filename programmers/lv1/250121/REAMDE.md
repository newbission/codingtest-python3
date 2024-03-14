# [\[PCCE 기출문제\] 10번 - 데이터 분석](https://school.programmers.co.kr/learn/courses/30/lessons/250121)

## 개요
> ### 문제
> AI 엔지니어인 현식이는 데이터를 분석하는 작업을 진행하고 있습니다. 데이터는 `["코드 번호(code)", "제조일(date)", "최대 수량(maximum)", "현재 수량(remain)"]`으로 구성되어 있으며 현식이는 이 데이터들 중 조건을 만족하는 데이터만 뽑아서 정렬하려 합니다.
> 
> 예를 들어 다음과 같이 데이터가 주어진다면
> ```python
> data = [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]
> ```
> 이 데이터는 다음 표처럼 나타낼 수 있습니다.
> 
> | code | date     | maximum | remain |
> | ---- | -------- | ------- | ------ |
> | 1    | 20300104 | 100     | 80     |
> | 2    | 20300804 | 847     | 37     |
> | 3    | 20300401 | 10      | 8      |
> 
> 주어진 데이터 중 `"제조일이 20300501 이전인 물건들을 현재 수량이 적은 순서"`로 정렬해야 한다면 조건에 맞게 가공된 데이터는 다음과 같습니다.
> ```python
> data = [[3,20300401,10,8],[1,20300104,100,80]]
> ```
> 정렬한 데이터들이 담긴 이차원 정수 리스트 `data와` 어떤 정보를 기준으로 데이터를 뽑아낼지를 의미하는 문자열 `ext`, 뽑아낼 정보의 기준값을 나타내는 정수 `val_ext`, 정보를 정렬할 기준이 되는 문자열 `sort_by가` 주어집니다.
> 
> `data`에서 `ext` 값이 `val_ext`보다 작은 데이터만 뽑은 후, `sort_by`에 해당하는 값을 기준으로 오름차순으로 정렬하여 `return` 하도록 `solution` 함수를 완성해 주세요. 단, 조건을 만족하는 데이터는 항상 한 개 이상 존재합니다.
>
> 요약: `data`에서 `ext` 값이 `val_ext`보다 작은 데이터만 뽑은 후, `sort_by`에 해당하는 값을 기준으로 오름차순으로 정렬하기

> # 주요 제한사항
> - `data[i][1]`은 `yyyymmdd` 형태
> - `ext`, `sort_by`의 값은 `"code", "date", "maximum", "remain"` 중 하나
> - 정렬 기준에 해당하는 값이 서로 같은 경우는 없음

<h1 align="center"><br><br><br>❗️❗️ 스포주의 ❗️❗️<br><br><br></h1>

## 풀이
### 접근
- `filter`쓰고 `sort`해서 리턴하면 되겠다

### 코드
```python
def solution(data, ext, val_ext, sort_by):
    key = ["code", "date", "maximum", "remain"]
    ext, sort_by = key.index(ext), key.index(sort_by)
    return sorted([t for t in data if t[ext] < val_ext], key=lambda x: x[sort_by])
```

### 설명
1. `ext`와 `sort_by`를 해당값에 맞게 `key`를 통해 `index`로 바꿔줌
2. `[t for t in data if t[ext] < val_ext]`: `val_ext`보다 작은 데이터만 추출
3. `key=lambda x: x[sort_by]`: `sort_by` 기준으로 오름차순 정렬
    ```python
    filtered_data = []
    for item in data:
        if item[ext] < val_ext:
            filtered_data.append(item)
    
    filtered_data.sort(key=lambda item: item[sort_by])
    return filtered_data
    ```