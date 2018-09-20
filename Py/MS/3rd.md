# 반복과 결정 만들기

프로그램의 흐름을 조절하기 위해서는 두 개의 무기를 사용해야 한다.

- `조건 프로그래밍(branching)`
- `루프`

우리는 이것들을 다양한 조합과 변형으로 사용할 수 있다.

## Conditional Programming: 조건적 프로그래밍

조건적 프로그래밍, 혹은 branching 이라 불리는 것은 조건을 평가하는 것이다.
주된 도구는 *`if`* 지시어이다. 다음의 예제를 보자.

```python
# conditional.1.py
late = True
if late:
    print('I need to call my manager!')
```

*`if`* 조건문에서 `late`는 조건식의 역할을 맡는다. 만약 평가의 결과가 참인 경우, `if`문 바로 아래의 몸체로 들어가게 된다. 인덴트를 주시하라.

```python
# conditional.2.py
late = False
if late:
    print('I need to call my manager!') #1
else:
    print('No need to call my manager...') #2
```

`late`의 평가값에 따라 우리는 블록 1과 블록 2중 한 블록을 들어갈 수 있다.

### 전문화된 else : elif

가끔은 