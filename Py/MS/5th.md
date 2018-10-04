# 시간과 메모리 아끼기

이 장에서는 몇 개의 비교와 측정을 수행하고, 이에 대한 최적화의 내용을 다룬다. 우선 다음의 코드를 보라.

```python
# squares.py
def square1(n):
    return n**2
def square(n):
    return n*n
```

두 함수는 n의 제곱을 반환하지만, 두번째가 조금 더 빠르다.

우리가 코드를 짤 때 이런 걸 신경써야 하는가? 대부분은 아니다. 그러나 전자상거래처럼 많은 수와 계산, 각 페이지당 적은 시간에 제공해야 하는 경우에는 필요할 것이다.

## map, zip 그리고 filter

### map

우리는 `위치적 인자를 받고 튜플을 반환하는 람다함수`를 사용할 것이다. 또한, map은 `iterator`를 반환하며, 우리는 매 호출마다 리스트로 변환하기 위해 list 생성자로 감쌀 것이다. 다음의 예제를 보자.

```python
# map.example.py
>>> map(lambda *a:a,range(3)) # without wrapping in list...
<map object at 0x7f563513b518>  # we get the iterator object

>>> list(map(lambda *a: a, range(3)))  # wrapping in list...
[(0,), (1,), (2,)]  # we get a list with its elements

>>> list(map(lambda *a: a, range(3), 'abc'))  # 2 iterables
[(0, 'a'), (1, 'b'), (2, 'c')]

>>> list(map(lambda *a: a, range(3), 'abc', range(4, 7)))  # 3
[(0, 'a', 4), (1, 'b', 5), (2, 'c', 6)]
>>> # map stops at the shortest iterator
>>> list(map(lambda *a: a, (), 'abc'))  # empty tuple is shortest
[]

>>> list(map(lambda *a: a, (1, 2), 'abc'))  # (1, 2) shortest
[(1, 'a'), (2, 'b')]

>>> list(map(lambda *a: a, (1, 2, 3, 4), 'abc'))  # 'abc' shortest
[(1, 'a'), (2, 'b'), (3, 'c')]
```

여기서 결과물을 리스트 형태로 가지기 위해 list 생성자를 쓴 것을 보라. 그렇지 않으면 map 객체를 받을 것이다.

map은 콜렉션의 모든 요소에 같은 함수를 적용해야 할때 매우 유용하다.

### zip

앞에서 다뤘음

### filter

다음의 예제를 보자.

```python
# filter.py
>>> test = [2,5,8,0,0,1,0]
>>> list(filter(None,test))
[2,5,8,1]
>>> list(filter(lambda x:x,test)) # equivalent to previous one
[2,5,8,1]
>>> list(filter(lambda x:x>4,test)) # keep only items > 4
[5,8]
```

위의 코드에서 filter에 인자를 그대로 반환하는 람다를 쓴 경우, 인자의 평가값이 참인 요소만 반환하는 것을 확인할 수 있다.

## Comprehensions

파이썬에서는 다음의 타입의 `comprehension`을 제공한다.

list comprehension은 리스트를 만다는 빠른 방법이다. 다음의 예제를 보자.

```python
# squares.map.py

# If you code like this you are not a Python guy!
>>> squares = []
>>> for n in range(10):
...        squares.append(n**2)
...
>>> list(squares)
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# This is better, one line, nice and readable
>>> squares = map(lambda n: n**2,range(10))
>>> list(squares)
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

위의 코드를 list comprehension을 이용하면 다음과 같다.

```python
>>> [n**2 for n in range(10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

아름답지 않은가!

다음의 예제는 filter를 이용하여 홀수 제곱을 걸러낼 것이다.

```python
# using map and filter
sq1 = list(
    filter(lambda n : not n %2, map(lambda n:n**2,range(10)))
)
# equivalent, but using list comprehension
sq2 = [n**2, for n in range(10) if not n % 2]
```

### 중첩된 Comprehensions

중첩된 comprehension의 예를 보자. 우선은 간단한 for 문의 예제를 보자.

```python
# pairs.for.loop.py
items = 'ABCDE'
pairs = []
for a in range(len(items)):
    for b in range(a, len(items)):
        pairs.append((items[a],items[b]))
```

이제 이를 중첩된 list comprehension을 통해 바꿔보자.

```python
# pairs.list.comprehension.py
items = 'ABCDE'
pairs = [(items[a],items[b])
    for a in range(len(items)) for b in range(a, len(items))]
```

### comprehension 필터링

우리는 comprehension에 필터링을 적용할 수 있다. 예를 들어 짧은 선분이 10보다 작은 모든 피타고리안 트리플($a^2 + b^2 = c^2$를 만족하는 $(a,b,c)$)을 구해보자.

```python
# pythagorean.triple.py
from math import sqrt
# 10 이하의 모든 조합
mx = 10
legs = [(a,b,sqrt(a**2+b**2))
    for a in range(1,mx) for b in range(a, mx)]
legs = list(
    filter(lambda triple: triple[2].is_integer(), legs))
print(legs) # prints: [(3, 4, 5.0), (6, 8, 10.0)]
```

위의 코드는 모든 쌍을 구한 뒤 정수가 아닌 숫자를 걸러내는 방법이다. 나는 이 트리플이 두개의 정수와 하나의 실수를 가지는 것이 마음에 들지 않는다. 이를 map을 이용하여 고친 다음의 코드를 보라.

```python
# pythagorean.triple.int.py
mx = 10
legs = [(a,b,sqrt(a**2+b**2))
    for a in range(1,mx) for b in range(a,mx)]
legs = filter(lambda triple: triple[2].is_integer(),legs)
legs = list(
    map(lambda triple: triple[:2] + (int(triple[2]),), legs))
print(legs)
```

와 너무 더럽다. 이거를 list comprehension으로 고쳐보자.

```python
# pythagorean.triple.comprehension.py
from math import sqrt
# this step is the same as before
mx = 10
legs = [(a,b,sqrt(a**2+b**2))
    for a in range(1,mx) for b in range(a,mx)]
# here we combine filter and map in one CLEAN list comprehension
legs = [(a,b,int(c)) for a,b,c, in legs if c.is_integer()]
print(legs)
```

### dict comprehensions

dictionary와 set comprehension은 list와 똑같이 작동하나, 문법이 조금 다르다. 다음의 예제를 보자.

```python
from string import ascii_lowercase
lettermap = dict((c,k) for k, c in enumerate(ascii_lowercase,1))
```

위의 코드는 dict 생성자에 comprehension을 넣는 모습이다. 이를 dict comprehension으로 표현하면 짜잔!

```python
lettermap = {c:k for k, c in enumerate(ascii_lowercase,1)}
```

dictionary는 중복된 키를 지원하지 않는다. 이는 다음의 예제를 통해 확인 할 수 있다.

```python
# dictionary.comprehension.duplicates.py
word = 'Hello'
swaps = {c:c.swapcase() for c in word}
print(swaps) # prints: {'o': 'O', 'l': 'L', 'e': 'E', 'H': 'h'}
```

위의 예제에서 l이 하나밖에 없다는 것을 보라.

### set comprehension

set comprehension은 list와 dictionary의 그것과 매우 유사하다. 파이썬은 set() 생성자와 명시적 {} 문법을 지원한다. 다음의 예를 보라.

```python
# set. comprehension.py
word = 'Hello'
letters = set(c for c in word)
letters2 = {c for c in word}
print(letters1)  # prints: {'l', 'o', 'H', 'e'}
print(letters1 == letters2)  # prints: True
```

set comprehension이 dictionary와 마찬가지로 중복을 허용하지 않는 대신 4개의 아이템만을 가지는 것을 보라.

## 발생자

`발생자`는 파이썬이 우리에게 주는 매우 강력한 도구이다. 이들은 iteration의 개념에 기반하였으며, 효율적이고 아름다운 코드 패턴을 가능하게 한다.  
발생자는 다음의 두 종류가 있다.

- Generator functions: 이들은 일반 함수와 비슷하나, return 문을 통해 반환하는 것이 아니라,  호출마다 멈추고 재시작 할 수 있게 하는 `yield`키워드를 이용한다.
- Generator expressions: 이들은 list comprehension과 유사하나, 리스트를 반환하는 것이 아닌, 각각의 결과를 하나하나 반환한다.

### Generator functions

아몰랑 다음의 예제를 보자.

```python
# first.n.squares.py
def get_squares(n): # classic function approach
    return [x**2 for x in range(n)]
print(get_squares(10))

def get_squares_gen(n): # generator approach
    for x in range(n):
        yield x ** 2 # we yield, we don't return
print(list(get_squares_gen(10)))
```

인터프리터가 yield에 도달할 때마다, 실행이 중지된다. 두 실행 결과가 같은 이유는 get_squares_gen()함수가 list의 생성자에 들어갔기 때문이고, 이는 StopIteration이 발동할 때까지 모든 발생자를 소진하기 때문이다. 자세히 보자.

```python
# first.n.squares.manual.py
def get_squares_gen(n):
    for x in range(n):
        yield x**2
squares = get_squares_gen(4)
print(squares)
print(next(squares)) 0
print(next(squares)) 1
print(next(squares)) 4
print(next(squares)) 9

print(next(squares)) 16
```

이 시점에서 왜 발생자 함수를 일반 함수 대신 써야 하는지 궁금할 것이다. 10개의 원소의 조합을 구하는 문제는 n!의 문제이기 때문에, n에 따른 조합의 수가 팩토리얼로 증가한다. 이 때, 일반 함수를 사용한다면, 모든 결과를 리스트에 담아 반환해야 하는데, 이 때, 메모리를 초과할 수 있으며, 수행하는 데에 매우 오랜 시간이 걸린다. 이 경우, 발생자 함수를 이용하면, 메모리와 시간을 줄일 수 있다.

또한 발생자 함수에 return 문을 사용할 수 있다는 점도 주목할만 하다. 이는 StopIteration 예외를 발생할 것이며, 반복을 효율적으로 멈출 수 있다. 다음의 예제를 보자.

```python
def geometric_progression(a,q):
    k=0
    while True:
        return = a * q ** k
        if result <= 10000:
            yield result
        else:
            return
        k+=1
for n in geometric_progression(2,5):
    print(n)
```

#### 더 나아가기

우리가 next(generator)를 호출할 때, 우리는 generator.__next__() 메소드를 호출하는 것이다.

#### yield 표현

위에서의 또 다른 흥미로운 구조는 yield from 표현이다. 이 표현은 부 반복자에서 값을 받아올 수 있게 한다.