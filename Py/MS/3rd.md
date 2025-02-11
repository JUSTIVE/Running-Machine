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

가끔은 if 하나만 필요할 수 도 있지만, 다른 때는 두 가지 이상의 분기를 다뤄야 할 때가 있다. 다음의 코드를 보자.

```python
# taxes.py
income = 15000
if income < 10000:
    tax_coefficient = 0.0 #1
elif income < 30000:
    tax_coefficient = 0.2 #2
elif income < 100000:
    tax_coefficient = 0.35 #3
else:
    tax_coefficient = 0.45 #4
print('I will pay:', income * tax_coefficient, 'in taxes')
```

위의 결과는 다음과 같이 나올 것이다.

```cmd
$ python taxes.py
I will pay: 3000.0 in taxes
```

### 삼항 연산자

삼항 연산자는 if/else문의 짧은 표현이다. 만약 이름의 값이 조건에 따라 다르게 배정되어야 한다면, 삼항 연산자를 쓰는 것이 if문을 쓰는 것보다 가독성이 좋을 수 있다. 다음의 예제를 보자.

```python
# ternary.py
order_total = 247 #GBP

# classic if/else form
if order_total > 100:
    discount = 25 #GBP
else:
    discount = 0 #GBP
print(order_total, discount)

#ternary operator
discount = 25 if order_total>100 else 0
```

## Looping

다른 프로그래밍 언어에서 반복문을 다뤄 본 경험이 있다면, 파이썬의 반복문은 조금 다르게 느껴질 것이다. 우선 `반복문`이란 무엇인가?
> `반복문`이란 주어진 반복 제어변수를 통해 코드 블럭을 한 번 이상 실행할 수 있는 것을 말한다.

### for 반복문

*`for`* 반복문은 리스트, 튜플, 혹은 객체의 콜렉션을 따라 반복할 때 사용된다. cpp 스타일의 예제를 보자.

```python
# simple.for.py
for number in [0,1,2,3,4]:
    print(number)
```

위의 예제는 0에서 4까지의 수를 출력할 것이다. for 반복문은 [0,1,2,3,4] 리스트에 적용되고, 매 회차마다, number는 시퀀스에서 주어진 값이 된다.

#### range를 따라 반복하기

때로는 우리는 숫자들의 범위를 따라 반복해야 할 때가 있다. 그리고 리스트를 하드코딩하는 것은 매우 불쾌한 일이 될 것이다. 이런 경우, `range` 함수가 구해줄 것이다. 다음의 코드를 보자.

```python
# simple.for.py
for number in range(5):
    print(number)
```

`range`함수는 파이썬에서 시퀀스를 만들 때에 널리 쓰인다.우리는 `stop` 값 하나만을 넘겨줄 수도 있고(이 경우 0부터 시작한다), 두 개의 값을 넘겨줄 수도 있고(시작, 끝), 그리고 심지어 세 개의 값도 넘겨줄 수 있다(시작, 끝, 단계). 다음의 예제를 보자.

```python
>>> list(range(10)) # one value : from 0 to value (excluded)
[0,1,2,3,4,5,6,7,8,9]
>>> list(range(3,8)) # two values : from start to stop (excluded)
[3,4,5,6,7]
>>> list(range(-10,10,4)) # three values : step is added
[-10,-6,-2,2,6]
```

여기서 `range(...)`를 `list`로 묶은 것은 무시하자. `range`객체는 조금 특별하나, 이 경우에서는 어떤값들이 반환되어지는 지만 확인하자.

#### 시퀀스를 따라 반복하기

이제 우리는 시퀀스를 따라 반복할 모든 도구가 있다. 다음의 예제를 보자.

```python
# simple.for.2.py
surnames = ['Rivest','Shamir','Adleman']
for position in range(len(surnames)):
    print(position, surnames[position])
```

위의 반복은 Java나 C++에 더 가까운 스타일이다. 파이썬에서는 이렇게 코딩하는 것은 드물다. 다음의 예를 보자.

```python
# simple.for.3.py
surnames = ['Rivest','Shamir','Adleman']
for surname in surnames:
    print(surname)
```

위의 예제에서 반복문은 surnames 리스트를 반복하며 각 반복마다 순서에 맞는 원소를 돌려준다. 훨씬 가독성이 좋지 않은가!

만약 위치도 출력하고 싶다면? 다시 range(len(...))의 형태로 돌아가야 하는가? 아니다. 우리는 `enumerate`내장함수를 이용할 수 있다. 보라:

```python
# simple.for.4.py
surnames = ['Rivest','Shamir','Adleman']
for position, surname in enumerate(surnames):
    print(position,surname)
```

위의 코드는 매우 흥미롭다. `enumerate`가 2-튜플을 반환하는 것을 주목하라. 우리는 enumerate(iterable,start)와 같이 enumerate에 start 인자를 넘겨줌으로써 0이 아닌 start부터 시작할 수 있게도 할 수 있다.

for 반복문을 이용하여 `리스트`, `튜플`, 그리고 파이썬에서 `iterable`이라 불리는 것들을 따라 반복할 수 있다. 이것은 매우 중요한 개념이니 자세히 보자.

#### Iterators and iterables

파이썬의 문서에 따르면 iterable은 다음과 같다.
> 스스로의 멤버를 한번에 하나씩 반환할 수 있는 객체를 의미한다. 예를 들어 iterables는 모든 시퀀스 타입(`list`,`str`,`tuple`)와, `dict`, `file`과 같은 몇몇 비-시퀀스 타입, 그리고 \_\_iter__( ) 혹은 \_\_getitem__( )이 정의된 모든 클래스를 포함한다. Iterables는 반복문과 시퀀스가 필요한 곳(zip( ),map( ),...)에서 쓰일 수 있다.

간단히, 우리가 *for k in sequence: ... body ...* 를 쓸때 for문은 시퀀스의 다음 요소를 물어보고, 무언갈 받으면 k라 부르며 body를 실행하고 반복한다.

리스트, 튜플, 스트링과 같은 몇몇 자료구조에서는 반복을 할 때 그들의 요소를 순서대로 생성한다. 반면 sets나 dictionary같은 애들은 아니다.

#### 여러 시퀀스를 반복하기

두 개의 같은 길이를 가진 시퀀스가 있을 때 이 쌍을 구하기 위해 어떻게 해야 하는가? 우선 다음의 대충 만든 예제를 보고 조금씩 다듬자

```python
# multiple.sequence.py
people = ['Jonas','Julio','Mike','Mez']
ages= [25,30,31,39]
for position in range(len(people)):
    person = people[position]
    age = ages[position]
    print(person, age)
```

이 코드는 효율적이지도 않고 파이썬같지도 않다. 비효율적인 이유는 특정 위치의 요소를 가져오는 것이 비싼 작업이고, 이걸 매 반복마다 하고 있기 때문이다. 위의 코드를 `enumerate`를 이용해서 바꿔보자

```python
# multiple.sequence.enumerate.py
people = ['Jonas','Julio','Mike','Mez']
ages= [25,30,31,39]
for position, person in enumerate(people):
    age = ages[position]
    print(person,age)
```

좀 더 낫지만, 아직 완벽하진 않고 조금 못생겼다. 위의 예제에서 여전히 age의 값을 position으로 가져오고 있다. 파이썬의 zip을 이용해서 바꿔보자

```python
people = ['Jonas','Julio','Mike','Mez']
ages= [25,30,31,39]
for person, age in zip(people,ages):
    print(person, age)
```

훨씬 낫지 않은가!

### while 반복문

앞의 단원에서는 for 문의 사용법을 배웠다. 여기서 중요한 점은, for 문은 유한한 개수의 원소들을 반복할 때에만 끝내주기 때문에 어떤 반복 구조를 이용할 지 결정해야 한다는 것이다.

루프가 특정 조건이 만족되거나, 프로그램이 종료되지 전까지 진행되어야 하는 것처럼 for문이 필요한 때와 다른 상황이 올 수도 있다. 순회해야 할 대상이 없는 경우, for문은 매우 안좋은 선택이 될 것이다. 그러나 두려워마라, 이런 경우를 위해 파이썬은 `while` 반복문을 제공한다.

`while`문은 몸체 안의 명령문들을 실행하면서 반복한다는 점에서 `for`문과 유사하지만, `while`문은 시퀀스를 따라 반복하지 않는다(할 순 있는데 하지 마라 제발). 대신, 조건을 만족하는 한 반복한다. 조건을 만족하는 경우, 반복을 멈춘다.

평소와 같이, 예제를 통해 확인해보자. 우리는 양수의 이진 표현법을 확인하려 한다. 그러기 위해서, 우리는 주어진 숫자를 2로 나누고, 나머지를 모은 후 리스트의 역순을 출력해야 한다.

```python
# binary.py
remainders = []
while n > 0:
    remainder = n % 2 # remainder of division by 2
    remainders.append(remainder) # we keep track of remainders
    n//=2 # we devide n by 2

# reassign the list to its reversed copy and print it
remainders = remainders[::-1]
print(remainders)
```

위의 코드에서, 리스트를 역순으로 가져오는 부분을 주목하라. 위의 코드는 파이썬에서의 `divmod` 함수를 이용해 조금 더 줄일 수 있다. `divmod`는 (나머지,몫)의 튜플을 반환한다.

```python
# binary.2.py
n = 39
remainders = []
while n > 0:
    n, remainder = divmod(n,2)
    remainders.append(remainder)

# reassign the list to its reversed copy and print it
remainders = remainders[::-1]
print(remainders)
```

위의 코드에서 우리는 n을 2로 나누고, 나머지를 받아오는 과정을 한 줄에서 해결했다.

위의 while반복문의 조건이 루프를 계속할 조건임을 확인하라. 이의 평가값이 `True`인 경우, `False`가 될 때까지 몸체가 실행되며, 이후에는 몸체를 즉시 탈출한다.

만약 조건이 절대 `False`로 평가되지 않는다면, 이 루프는 무한 루프라 불리게 된다.

### break 문과 continue 문

~~c 언어와 동일~~

## itertools 모듈 개요

### 무한 반복자

무한 반복자는 `for`문을 `while`문처럼 사용할 수 있게 한다.

```python
# infinite.py
from itertools import count
for n in count(5,3):
    if n > 20:
        break
    print(n,end=", ")
```

`count` 팩토리 클래스는 계속 반복하는 반복자를 만든다. 위의 예제에서는 5부터 시작하여 계속 3을 더할 것이다. 무한반복을 원치 않는다면 수동으로 `break`를 지정해야 한다.

### 조합 생성기

예를 들어, ABC의 순열은 다음의 6개이다.

- ABC
- ACB
- BAC
- BCA
- CAB
- CBA

만약 N개의 원소가 있다면, 이들의 순열은 총 N!이다. 이를 파이썬에서 해보자.

```python
# permutations.py
from itertools import permutations
print(list(permutations('ABC')))

[('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]
```