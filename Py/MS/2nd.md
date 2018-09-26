# Built-in Data Types

파이썬에서, 객체는 데이터의 추상화이고, 파이썬은 데이터를 표현할 수 있는 다양한 자료구조를 가지고 있고, 이것들을 자신만의 커스텀 데이터로 합칠 수 있다.

## 모든 것은 객체이다

파이썬 모듈에서 age=43와 같은 지시를 할때, 무슨 일이 일어나는가? 객체가 생성될 때, *id*를 부여받고, *타입*은 *int*(integer number)로 설정되고, *값*은 42로 설정된다. 이름 *age*는 전역 네임 스페이스에 위치하고, 해당 객체를 가리킨다.

## Mutable? Immutable? 그것이 문제로다

파이썬에서는 변하는 것들은 mutable, 변하지 않는 객체들은 immutable이라 부른다. 다음의 예제가 있다.

```python
>>> age = 42
>>> age
42
>>> age = 32 #A
>>> age
43
```

위의  #A 라인에서 우리는 age의 값을 바꾼 것이 아닌, 새 int 객체를 생성하여 age 에 연결한 것이다. 이 때, 새로 생성된 객체는 id가 다를 것이다. 다음의 예제를 보자.

```python
>>> age = 42
>>> id(age)
10456352
>>> age = 43
>>> id(age)
10456384
```

여기서 내장함수 `id`를 사용한 것에 주목하라. 예상했던 대로 두 객체는 다른 id 값을 가진다.

이제, 다음의 mutable 객체의 예제를 보자.

```python
>>> fab = Person(age=39)
>>> fab.age
39
>>> id(fab)
139632387887456
>>> fab.age = 29  # I wish!
>>> id(fab)
139632387887456  # still the same id
```

위의 경우, fab 객체의 type은 사용자 지정 클래스인 Person이다. 위의 경우 fab의 id는 변하지 않지만, 물론 fab.age의 id는 변했다 ^^

## 숫자들

파이썬의 내장 자료형을 숫자들로부터 시작해보자. 숫자는 불변객체:immutable object이다.

### 정수

파이썬 정수는 가용 가능한 가상 메모리 내의 무제한의 범위를 가진다. 정수는 음수, 0, 양수일 수 있다. 파이썬의 정수는 기본적인 수학 연산자를 지원한다.

```python
>>> a = 12
>>> b = 3
>>> a + b  # addition
15
>>> b - a  # subtraction
-9
>>> a // b  # integer division
4
>>> a / b  # true division
4.0
>>> a * b  # multiplication
36
>>> b ** a  # power operator
531441
>>> 2 ** 1024  # a very big number, Python handles it gracefully
179769313486231590772930519078902473361797697894230657273430081157732675805500963132708477322407536021120113879871393357658789768814416622492847430639474124377767893424865485276302219601246094119453082952085005768838150682342462881473913110540827237163350510684586298239947245938479716304835356329624224137216
```

파이썬에서는 두개의 나누기 연산자를 지원한다.

- true division (`/`): 소수점 아래자리까지 반환하는 나누기 연산자
- integer division (`//`): 소수점 아래자리를 버림하는 나누기 연산자

위의 두 나누기 연산자가 음수와 양수에서 어떻거 다르게 동작하는지 다음의 예제를 통해 확인해보자

```python
>>> 7 / 4  # true division
1.75
>>> 7 // 4  # integer division, flooring returns 1
1
>>> -7 / 4  # true division again, result is opposite of previous
-1.75
>>> -7 // 4  # integer div., result not the opposite of previous
-2
```

이는 매우 흥미로운 결과이다. 마지막 줄에서 -1을 기대했겠지만, 파이썬에서의 버림은 음수 무한대를 향한다. 버림 대신 깔끔하게 소수점 아래를 자르고 싶다면 내장 함수인 int를 사용하는 것을 추천한다.

또한 파이썬은 나누기의 나머지 값을 구하는 모듈로 연산자가 있다. 이는 (`%`)로 표현된다

### 부울

부울 대수는 대수의 부분집합으로, `True`와 `False`로 진리값을 나타내는 것이다. Boolean은 integer의 subclass로, 1과 0처럼 동작한다. `int` 클래스에 대응되는 Boolean 클래스는 `bool` 이며, `True` 혹은 `False`를 반환한다. 모든 파이썬의 내장 객체는 `bool` 내장함수를 통해 `True` 혹은 `False` 값으로 평가될 수 있다.

부울 값은 `and`, `or`, `not`과 같은 논리 연산자와 사용되어질 수 있다.

### 실수

파이썬에서의 실수, 혹은 부동 소수점 숫자는 IEEE-754를 따른다. 이는 64비트의 정보를 `부호`, `지수`, `가수`의 영역으로 구성된다.
일반적인 프로그래밍 언어는 개발자에게 단정도(single precision)와 배정도(double precision)의 선택지를 준다. 파이썬은 오로지 배정도의 정밀도를 지원한다.  

*`sys.float_info`* 구조체는 당신의 시스템에서 부동소수점이 동작할 지를 알려준다.

파이썬의 부동 소수점은 정확하지 않다. 다음의 예를 보자.

```python
>>> 3 * 0.1 - 0.3 # this should be 0!!!
5.551115123125783e-17
```

이러한 오차는 세밀한 값들을 다룰 때 큰 문제가 될 수 있다. 걱정말자. 파이썬은 `Decimal`자료형을 통해 이러한 문제를 해결한다.

### 복소수

파이썬은 복소수를 다룰 수 있는 기능들을 내장하고 있다. 다음의 예제를 보자.

```python
>>> c = 3.14 + 2.73j
>>> c.real # real part
3.14
>>> c.imag # imaginary part
2.73
>>> c.conjugate() # conjugate of A + Bj is A - Bj
(3.14-2.73j)
>>> c*2 # muliplication is allowed
(6.28+5.46j)
>>> c ** 2  # power operation as well
(2.4067000000000007+17.1444j)
>>> d = 1 + 1j  # addition and subtraction as well
>>> c - d
(2.14+1.73j)
```

### 분수와 소수

분수는 분자와 분모의 가장 작은 형태를 가지고 있다. 다음의 예제를 보자.

```python
>>> from fractions import Fraction
>>> Fraction(10, 6)  # mad hatter?
Fraction(5, 3)  # notice it's been reduced to lowest terms
>>> Fraction(1, 3) + Fraction(2, 3)  # 1/3 + 2/3 = 3/3 = 1/1
Fraction(1, 1)
>>> f = Fraction(10, 6)
>>> f.numerator
5
>>> f.denominator
3
```

이것은 매우 유용할 수 있으나, 상업용 소프트웨어에서는 보기 힘들다. 대신, 모든 면에서 정확함을 요구하는 상황에서 쓰이는 `decimal`을 사용한다. 다음의 예제를 보자.

```python
>>> from decimal import Decimal as D  # rename for brevity
>>> D(3.14)  # pi, from float, so approximation issues
Decimal('3.140000000000000124344978758017532527446746826171875')
>>> D('3.14')  # pi, from a string, so no approximation issues
Decimal('3.14')
>>> D(0.1) * D(3) - D(0.3)  # from float, we still have the issue
Decimal('2.775557561565156540423631668E-17')
>>> D('0.1') * D(3) - D('0.3')  # from string, all perfect
Decimal('0.0')
```

Decimal 객체를 float으로부터 생성했을 때, float에서 발생하는 오류를 그대로 받아오나, int 혹은 string을 통해 생성했을 때는 정확한 결과를 보여준다.

## 불변 시퀀스

### 문자열과 바이트

파이썬에서 텍스트 데이터는 str,혹은 string으로 잘 알려진 객체로 다뤄진다. 이들은 `unicode code points`의 불변 시퀀스이다. `unicode code points`는 문자를 나타낼 수 있으나, 데이터 형식과 같은 다른 의미를 포함할 수도 있다. 파이썬은 다른 언어들과 달리 `문자:character` 타입을 가지고 있지 않아 문자 하나는 길이가 1인 문자열로 표현된다. 유니코드는 데이터를 다루고 모든 프로그램에 사용되기에 적합하다. 파이썬에서의 문자열 상수는 하나부터 세 개까지의 작은 따옴표(2개는 큰 따옴표)를 이용해 만든다. 다음의 예제를 보자.

```python
>>> # 4 ways to make a string
>>> str1 = 'This is a string. We built it with single quotes.'
>>> str2 = "This is also a string, but built with double quotes."
>>> str3 = '''This is built using triple quotes,
... so it can span multiple lines.'''
>>> str4 = """This too
... is a multiline one
... built with triple double-quotes."""
>>> str4  #A
'This too\nis a multiline one\nbuilt with triple double-quotes.'
>>> print(str4)  #B
This too
is a multiline one
built with triple double-quotes.
```

모든 시퀀스에는 길이가 있다. 이는 `len`함수를 통해 구할 수 있다.

```python
>>> len(str1)
49
```

### 문자열 인코딩 및 디코딩

`encode/decode`메소드를 통해 우리는 유니코드 문자열을 인코딩할 수 있고, 바이트 객체를 디코딩 할 수 있다. Utf-8은 가변 문자 인코딩이며, 모든 유니코드를 인코딩 할 수 있다. 또한 웹에서의 지배적인 인코딩이다. 다음의 예제를 보자. 문자열 생성 앞에 b 문자상수를 붙임으로써 byte 객체를 생성하는 데에 주목하자.

```python
>>> s = "This is üŋíc0de"  # unicode string: code points
>>> type(s)
<class 'str'>
>>> encoded_s = s.encode('utf-8')  # utf-8 encoded version of s
>>> encoded_s
b'This is \xc3\xbc\xc5\x8b\xc3\xadc0de'  # result: bytes object
>>> type(encoded_s)  # another way to verify it
<class 'bytes'>
>>> encoded_s.decode('utf-8')  # let's revert to the original
'This is üŋíc0de'
>>> bytes_obj = b"A bytes object"  # a bytes object
>>> type(bytes_obj)
<class 'bytes'>
```

### 문자열 자르기와 인덱싱

시퀀스를 다룰 때, 특정 지점에 접근하는 것(`인덱싱`)이나 서브-시퀀스를 얻는 것(`자르기`)은 매우 보편적이다. 불변 시퀀스에서 다룰 때, 두 연산은 읽기 전용이다.

인덱싱이 0-베이스의 하나의 형태를 제공하는 데에 반해, 자르기는 여러 형태를 제공한다. 시퀀스를 자를 때, 우리는 시작과 종료 지점, 그리고 단계를 지정할 수 있다. 이들은 `:`으로 구별되며, 다음과 같이 사용된다- `my_sequence[start:stop:step]` 모든 인자는 선택적이며, start는 포함이고, end는 제외이다. 다음의 예제를 보자.

```python
>> s = "The trouble is you think you have time."
>>> s[0]  # indexing at position 0, which is the first char
'T'
>>> s[5]  # indexing at position 5, which is the sixth char
'r'
>>> s[:4]  # slicing, we specify only the stop position
'The '
>>> s[4:]  # slicing, we specify only the start position
'trouble is you think you have time.'
>>> s[2:14]  # slicing, both start and stop positions
'e trouble is'
>>> s[2:14:3]  # slicing, start, stop and step (every 3 chars)
'erb '
>>> s[:]  # quick way of making a copy
'The trouble is you think you have time.'
```

인자를 지정하지 않은 경우, 파이썬은 기본적으로 채워 줄 것이다. 시작의 경우에는 문자열의 시작을, 끝은 문자열의 끝을, 단계는 1로 말이다.맨 마지막은 문자열을 복사하는 가장 쉬운 방법이다(같은 값, 다른 객체).

### 튜플

튜플은 임의의 파이썬 객체이다. 튜플에서 아이템은 쉼표로 구분된다. 튜플은 파이썬의 모든 곳에서 사용된다. 다음의 예제를 보자.

```python
>> t = ()  # empty tuple
>>> type(t)
<class 'tuple'>
>>> one_element_tuple = (42, )  # you need the comma!
>>> three_elements_tuple = (1, 3, 5)
>>> a, b, c = 1, 2, 3  # tuple for multiple assignment
>>> a, b, c  # implicit tuple to print with one instruction
(1, 2, 3)
>>> 3 in three_elements_tuple  # membership test
True
```

멤버쉽 연산자 `in`은 리스트, 문자열, 딕셔너리와 일반적인 시퀀스 객체에서도 사용된다는 것을 주목하자.

튜플 배정문이 허용하는 것 중 하나는, *`one-line swaps`*인데, 임시 변수 없이 가능하다.

원래 사용하던 방식을 보자.

```python
>>> a, b = 1, 2
>>> c = a  # we need three lines and a temporary var c
>>> a = b
>>> b = c
>>> a, b  # a and b have been swapped
(2, 1)
```

그리고 파이썬에서 사용되는 방법을 보자.

```python
>>> a, b = b, a # this is the Pythonic way to do it
>>> a, b
(1, 2)
```

튜플은 불변객체이기 때문에, 딕셔너리에서의 key로 사용되어질 수 있다. `dict`객체는 불변객체의 key를 필요로 한다. 튜플은 수학에서의 벡터에 가까운 표현이다. 튜플은 보통 다른 타입의 원소를 가진다.

## 가변 시퀀스

### 리스트

파이선의 리스트는 가변 시퀀스이다. 리스트는 보통 같은 타입의 객체의 집합을 저장하는 데에 사용되나 다른 타입을 저장하지 못할 이유는 없다. 다음의 예제를 보자.

```python
>>> []  # empty list[]
>>> list()  # same as []
[]
>>> [1, 2, 3]  # as with tuples, items are comma separated
[1, 2, 3]
>>> [x + 5 for x in [2, 3, 4]]  # Python is magic
[7, 8, 9]
>>> list((1, 3, 5, 7, 9))  # list from a tuple
[1, 3, 5, 7, 9]
>>> list('hello')  # list from a string
['h', 'e', 'l', 'l', 'o']
```

위의 magic이라 표현된 부분은 `list comprehension`이라 불리며, 파이썬의 강력한 함수형 기능 중 하나이다.

리스트에서 제공하는 함수들을 다음의 예제를 통해 확인하자.

```python
>>> a= [1,2,1,3]
>>> a.append(13) # we can append anything at the end
>>> a
[1, 2, 1, 3, 13]
>>> a.count(1)  # how many `1` are there in the list?
2>>> a.extend([5, 7])  # extend the list by another (or sequence)
>>> a
[1, 2, 1, 3, 13, 5, 7]
>>> a.index(13)  # position of `13` in the list (0-based indexing)
4
>>> a.insert(0, 17)  # insert `17` at position 0
>>> a
[17, 1, 2, 1, 3, 13, 5, 7]
>>> a.pop()  # pop (remove and return) last element
7
>>> a.pop(3)  # pop element at position 3
1
>>> a
[17, 1, 2, 3, 13, 5]
>>> a.remove(17)  # remove `17` from the list
>>> a
[1, 2, 3, 13, 5]
>>> a.reverse()  # reverse the order of the elements in the list
>>> a
[5, 13, 3, 2, 1]
>>> a.sort()  # sort the list
>>> a[1, 2, 3, 5, 13]
>>> a.clear()  # remove all elements from the list
>>> a[]

>>> a = list('hello')  # makes a list from a string
>>> a['h', 'e', 'l', 'l', 'o']
>>> a.append(100)  # append 100, heterogeneous type
>>> a
['h', 'e', 'l', 'l', 'o', 100]
>>> a.extend((1, 2, 3))  # extend using tuple
>>> a
['h', 'e', 'l', 'l', 'o', 100, 1, 2, 3]
>>> a.extend('...')  # extend using string
>>> a
['h', 'e', 'l', 'l', 'o', 100, 1, 2, 3, '.', '.', '.']

>>> a = [1, 3, 5, 7]
>>> min(a)  # minimum value in the list
1
>>> max(a)  # maximum value in the list
7
>>> sum(a)  # sum of all values in the list
16>>> len(a)  # number of elements in the list
4
>>> b = [6, 7, 8]
>>> a + b  # `+` with list means concatenation
[1, 3, 5, 7, 6, 7, 8]
>>> a * 2  # `*` has also a special meaning
[1, 3, 5, 7, 1, 3, 5, 7]
```

마지막의 두 줄은 연산자 오버로딩의 개념을 소개한다.다음은 파이썬의 정렬 메소드가 얼마나 강력한지 보여준다.

```python
>>> from operator import itemgetter
>>> a = [(5, 3), (1, 3), (1, 2), (2, -1), (4, 9)]
>>> sorted(a)
[(1, 2), (1, 3), (2, -1), (4, 9), (5, 3)]
>>> sorted(a, key=itemgetter(0))
[(1, 3), (1, 2), (2, -1), (4, 9), (5, 3)]
>>> sorted(a, key=itemgetter(0, 1))
[(1, 2), (1, 3), (2, -1), (4, 9), (5, 3)]
>>> sorted(a, key=itemgetter(1))
[(2, -1), (1, 2), (5, 3), (1, 3), (4, 9)]
>>> sorted(a, key=itemgetter(1), reverse=True)
[(4, 9), (5, 3), (1, 3), (1, 2), (2, -1)]
```

다음은 위의 코드의 설명이다. 우선 a 는 튜플의 리스트이다.(정확히는 2-튜플) 우리는 `sorted(list)` 를 통해 `list`의 정렬된 버전을 얻을 수 있다. 이 경우, 정렬은 튜플의 첫 요소를 기준으로 정렬한 후, 첫 요소의 값이 같은 경우, 두 번째 요소에 대해서 정렬한다. 파이썬에서는 각 튜플에서 튜플 내의 정렬 우선순위를 정할 수 있게 할 수 있으며, 이는 `key=itemgetter(index)`와 같이 사용되어진다. 이 경우, 여러 인덱스가 들어갈 수 있으며 각 인덱스의 순별로 정렬의 우선순위가 결정된다.
또한 reverse의 값을 줌으로써 정렬을 역순으로 수행할 수 도 있다.

파이썬의 정렬 알고리즘은 `Tim Peters`에 의해 작성된 `Timsort`를 사용하며, 매우 강력한 합병정렬과 삽입정렬의 혼합으로 구성되어있다. 이 정렬 알고리즘은 대부분의 주요 언어들의 정렬보다 나은 속도를 가진다. Timsort는 안정된 알고리즘이며, 이는 여러 우선순위로 정렬할 때, 원본의 우선순위를 보존한다는 것이다.

### 바이트 배열

*`bytearray`*은 기본적으로 `bytes` 객체의 가변 버전이다. 이들은 대부분의 가변 기쿠너스의 유용한 메소드와 `bytes`타입의 메소드를 포함한다. 아이템은 `[0,256)`범위 내의 값을 가진다. 다음의 간단한 예제를 보자.

```python
>>> bytearray() # empty bytearray object
bytearray(b'')
>>> bytearray(10) # zero-filled instance with given length
bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
>>> bytearray(range(5)) # bytearray from iterable of integers
>>> bytearray(b'\x00\x01\x02\x03\x04')
>>> name = bytearray(b'Lina') # A - bytearray from bytes
>>> name.replace(b'L', b'l')
bytearray(b'lina')
>>> name.endswith(b'na')
True
>>> name.upper()
bytearray(b'LINA')
>>> name.count(b'L')
1
```

바이트 배열은 소켓을 통해 데이터를 받거나, 받은 데이터를 연결할 때 등 여러 상황에서 유용하게 쓰일 수 있다.

## Set 타입

파이썬은 `set`과 `frozenset`의 두 가지의 `set` 타입을 지원한다. `set`은 가변적이며, `frozenset`은 불변이다. 이들은 순서없는 불변객체의 콜렉션이다.
`Hashability`는 딕셔너리에 대한 키뿐만 아니라 객체를 집합 멤버로 사용할 수있게 해주는 특성이다.

비교값이 동등한 객체들은 같은 해쉬 값을 가진다. Set은 멤버쉽을 확인하는 데에 주로 쓰인다. 다음의 예제를 통해 `in` 연산자를 소개하도록 한다.

```python
>>> small_primes = set() # empty set
>>> small_primes.add(2) # adding one element at a time
>>> small_primes.add(3)
>>> small_primes.add(5)
>>> small_primes
{2, 3, 5}
>>> small_primes.add(1) # Look what I've done, 1 is not a prime!
>>> small_primes
{1, 2, 3, 5}
>>> small_primes.remove(1) # so let's remove it
>>> 3 in small_primes # membership test
True
>>> 4 in small_primes
False
>>> 4 not in small_primes # negated membership test
True
>>> small_primes.add(3) #trying to add 3 again
>>> small_primes
{2, 3, 5} # no change, duplication is not allowed
>>> bigger_primes = set([5,7,11,13]) # faster creation
>>> small_primes | bigger_primes # union operator `|`
{2, 3, 5, 7, 11, 13}
>>> small_primes & bigger_primes # intersection operator `&`
{5}
>>> small_primes - bigger_primes # difference operator `-`
{2,3}
```

위의 예제에서 보듯, set은 아무 iterable로부터 만들고 더하고 뺄 수 있다.
set을 만드는 다른 방법은 중괄호를 쓰는 방법이다. 이는 다음과 같다.

```python
>>> small_primes = {2,3,5,5,3}
>>> small_primes
{2, 3, 5}
```

다음의 예제를 통해 set의 불변형인 `frozenset`을 보도록 하자.

```python
>>> small_primes = frozenset([2, 3, 5, 7])
>>> bigger_primes = frozenset([5, 7, 11])
>>> small_primes.add(11) # we cannot add to a frozenset
Traceback (most recdnt call lsat):
   File "<stdin>", line 1, in <module>
AttributeError: 'frozenset' object has no attribute 'add'
>>> small_primes.remove(2) # neither we can remove
Traceback (most recdnt call lsat):
   File "<stdin>", line 1, in <module>
AttributeError: 'frozenset' object has no attribute 'remove'
>>> small_primes & bigger_primes # intersect, union, etc. allowed
frozenset({5, 7})
```

위의 예제에서 보듯, `frozenset`은 가변형의 `set`에 비해 제한이 있다. 그러나 `frozenset`은 멤버쉽 테스트나, 교집합, 합집합, 차집합 연산을 지원하고, 성능상에서도 여전히 유리하다.

## 매핑 타입 - 딕셔너리

딕셔너리는 `key`를 `value`에 사상한다. `key`는 해쉬 가능한 객체여야 한다. 다음의 예제는 {'A':1, 'Z':-1}을 표현하는 다섯가지의 다른 방법이다.

```python
>>> a = dict(A=1,Z=-1)
>>> b = {'A':1,'Z':-1}
>>> c = dict(zip(['A','Z'],[1,-1]))
>>> d = dict([('A',1),('Z',-1)])
>>> e = dict({'Z':-1,'A':1})
>>> a == b == c == d == e # are they all the same?
True # indeed!
```

대입 연산은 하나의 등호로 이루어지고, 객체의 비교는 두개의 등호를 통해 이루어진다. 개게를 비교하는 방법은 `is`연산자를 이용하는 것을 비롯하여 여러가지가 있다. 하지만 별다른 이유가 없는 한, 두개의 등호를 통해 비교하라. 또한 위의 예제에서는 매우 좋은 `zip` 함수를 사용했다. 이는 현실 세계의 지퍼로부터 유래했으며, 두개의 각 요소를 하나씩 묶어서 붙이는 역할을 수행한다. 다음의 예제를 보자.

```python
>>> list(zip(['h', 'e', 'l', 'l', 'o'], [1, 2, 3, 4, 5]))
[('h', 1), ('e', 2), ('l', 3), ('l', 4), ('o', 5)]
>>> list(zip('hello', range(1, 6)))  # equivalent, more Pythonic
[('h', 1), ('e', 2), ('l', 3), ('l', 4), ('o', 5)]
```

위의 예제에서 같은 리스트를 두 개의 방법으로 만들었다. 하나는 좀 더 명시적이고, 나머지 하나는 파이썬같은 방법이다. zip 함수의 반환형은 list가 아닌 iterable형태이므로, list()로 감쌌다.

다음의 예는 딕셔너리의 기본 연산들이다.

```python
>>> d = {}>>> d['a'] = 1  # let's set a couple of (key, value) pairs
>>> d['b'] = 2>>> len(d)  # how many pairs?
2
>>> d['a']  # what is the value of 'a'?
1
>>> d  # how does `d` look now?
{'a': 1, 'b': 2}
>>> del d['a']  # let's remove `a`
>>> d
{'b': 2}
>>> d['c'] = 3  # let's add 'c': 3
>>> 'c' in d  # membership is checked against the keys
True
>>> 3 in d  # not the values
False
>>> 'e' in d
False
>>> d.clear()  # let's clean everything from this dictionary
>>> d
{}
```

딕셔너리가 대괄호를 통해 key에 접근하는 방법을 보라. 리스트와 튜플과 마찬가지로 이는 파이썬의 일관성 중 하나이다.

딕셔너리 뷰라 불리는 특별한 객체-keys, values, items-들을 보자. 이들은 딕셔너리 진입의 동적인 시점을 보여주고, 딕셔너리가 변할 때 변한다. keys()는 딕셔너리의 모든 key를 반환하고, values()는 딕셔너리의 모든 value를 반환하고, items()는 딕셔너리의 모든 (key,value)를 반환한다. 다음의 코드를 통해 확인하자.

```python
>>> d = dict(zip('hello', range(5)))
>>> d
{'e': 1, 'h': 0, 'o': 4, 'l': 3}
>>> d.keys()
dict_keys(['e', 'h', 'o', 'l'])
>>> d.values()
dict_values([1, 0, 4, 3])
>>> d.items()
dict_items([('e', 1), ('h', 0), ('o', 4), ('l', 3)])
>>> 3 in d.values()
True
>>> ('o', 4) in d.items()
True
```

위의 예제에서 'hello'와 [0, 1, 2, 3, 4]를 zip 함수로 묶는 것을 보라. hello에는 두 개의 l이 있고 zip 함수에 의해 2와 3으로 짝지어진다. 이 때, 두번째 l이 처음의 대입을 덮어쓰는 것을 확인할 수 있다. 또한, 원래의 순서를 잃어버린 것을 볼 수 있다. 

우리는 뷰가 콜렉션을 반복하는 데에 필수적인 도구라는 것을 볼 것이다. 다음의 예제를 통해 파이썬의 dictionary에서 제공하는 다른 유용한 메소드들을 확인해보자.

```python
>>> d
{'e':1, 'h':0, '0':4, 'l':3}
>>> d.popitem() # removes a random item
('e',1)
>>> d
{'h':0, 'o':4, 'l':3}
>>> d.pop('l') # remove item with key 'l'
3
>>> d.pop('not-a-key') # remove a key not in dictionary: KeyError
Traceback (most recent call last) :
   File "<stdin>", line 1 in <module>
KeyError: 'not-a-key'
>>> d.pop('not-a-key', 'default-value') # with a default value?
'default-value' # we get the default value
>>> d.update({'another':'value'}) # we can update dict this way
>>> d.update(a=13) # or this way (like a function call)
>>> d
{'a':13, 'another':'value', 'h':0, 'o':4}
>>> d.get('a') # same as d['a'] but if key is missing no KeyError
13
>>> d.get('a',177) # default value used if key is missing
13
>>> d.get('b',177) # like in this case
177
>>> d.get('b') # key is not there, so None is returned
```

모든 파이썬의 함수는 명시적으로 return 문이 적혀있지 않은 한, None을 반환한다. None은 주로 함수에 기본 인자가 넘겨지지 않았을 때와 같이 값의 부재를 표현한다. False와 None은 False로 평가되어 차이가 없는 듯 하지만, False는 부정의 정보를 가지고 있고, None은 정보가 없다는 것이다.

딕셔너리에서 마지막으로 다룰 내용은 `setdefault`이다. 이는 `get`과 같은 동작을 수행하나, 주어진 value가 없는 경우 이를 설정하는 것이다. 다음의 예제를 통해 확인해보자.

```python
>>> d = {}
>>> d.setdefault('a',1) # 'a' is missing, we get default value
1
>>> d
{'a', 1} # also, the key/value pair ('a', 1) has now been added
>>> d.setdefault('a',5) # let's try to override the value
1
>>> d
{'a':1} # didn't work, as expected
```

### 콜렉션 모듈

파이썬에서는 일반적인 용도의 내장 컨테이너 뿐만 아니라, 전문화된 데이터 타입이 `collections` 모듈 안에 있다. 이는 다음과 같다.

데이터 타입|설명
:---|:---
namedtuple |`named` 필드를 가진 튜플을 만드는 팩토리 함수
deque      |양 끝에서의 빠른 append와 pop을 지원하는 list와 같은 컨테이너
ChainMap   |dict
Counter    |
OrderedDict|
defaultDict|
UserDict   |dict 서브클래스를 쉽게 만들기 위한 래퍼 클래스
UserList   |list 서브클래스를 쉽게 만들기 위한 래퍼 클래스
UserString |string 서브클래스를 쉽게 만들기 위한 래퍼 클래스