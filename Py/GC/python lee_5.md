## 5.과시작

이 과에서는 코드를 더 깔끔하고 우아하게 씀. -시간, 메모리 절약부

### map,zip and filter

에 대해서 배울것

#### map

map (function, iterable, ...)은 iterable의 모든 항목에 함수를 적용하여 결과를 산출하는 반복자를 반환합니다.

추가 iterable 인수가 전달되면 함수는 많은 인수를 취해야하며 모든 iterable의 항목에 병렬로 적용됩니다.

다중 iterator를쓸경우 길이가 가장 짧은 iterable이 모두 소모되면 멈 춥니 다.

map(기능,반복or함수등) 개꿀따리.

### zip

zip (* iterables)은 튜플의 반복자를 반환하는데, 여기서 i 번째 튜플은 각 인수 시퀀스 또는 iterables의 i 번째 요소를 포함합니다.

반복자는 가장 짧은 입력 iterable이 모두 소모되면 멈춤. 하나의 반복 가능한 인수를 사용하면 1 튜플의 반복자를 반환. 인수가 없으면 빈 반복자를 반환.

-그냥 짝지어주는 친구임.

map과 zip을 결합하여 사용하는 간단한 예는 시퀀스 사이의 요소 별 최대 값을 계산하는 방법.

즉, 각 시퀀스의 첫 번째 요소의 최대 값, 두 번째 요소의 최대 값 등.

### filter

filter (function, iterable) 함수가 True를 반환하는 iterable 요소로부터 반복자를 구성합니다. iterable은 시퀀스, 반복을 지원하는 컨테이너 또는 반복자 일 수 있습니다. function이 None이면 ID 함수가 가정됩니다. 즉, false 인 iterable의 모든 요소가 제거됩니다.

### COMPREHENSIONS (보완성)

list comprehension은 리스트를 만드는 빠른 방법임.

~~~python

square = []

for n in range(10):
    square.append(n ** 2)

print("\n",list(square))

squares = map(lambda n:n**2, range(10))

print("\n",list(squares))


[n ** 2 for n in range(10)]#이것이 comprehensions

sq1 = list(    filter(lambda n: not n % 2, map(lambda n: n ** 2, range(10))))

sq2 = [n ** 2 for n in range(10) if not n % 2]#이것과 sq1는 같다
~~~

뻐킹 대괄호에 넣는다. 끝

### nested comprehensions

중첩맨
items = 'ABCDE'
pairs = []
for a in range(len(items)):
    for b in range(a, len(items)):
        pairs.append((items[a], items[b]))

items='ABCDE'
pairs =[(items[a],items[b]) for a in range(len(items)) for b in range(a, len(items))]

### filtering a comprehension

필터랑 사용한것. 어썸함

~~~python
from math import sqrt
# this will generate all possible pairs
mx = 10
legs = [(a, b, sqrt(a**2 + b**2))
    for a in range(1, mx) for b in range(a, mx)]
# this will filter out all non pythagorean triples
legs = filter(lambda triple: triple[2].is_integer(), legs)
#print(legs)  

legs = list(
    map(lambda triple: triple[:2]
+ (int(triple[2]),),  legs))
print(legs)  # prints: [(3, 4, 5), (6, 8, 10)]

#이게 위에 긴거랑 같음
ms = 10
leg = [(a, b, sqrt(a**2 + b**2))
for a in range(1, ms) for b in range(a, ms)]
# here we combine filter and map in one CLEAN list comprehension
leg = [(a, b, int(c)) for a, b, c in leg if c.is_integer()]
print(leg)  
# prints: [(3, 4, 5), (6, 8, 10)]
~~~

### dict compre

또네 시부랄.

dict와 set compre는 목록과 정확히 동일하게 작동하지만 구문에 약간의 차이가 있다

~~~python
from string import ascii_lowercase

lettermap = dict((c, k) for k, c in enumerate(ascii_lowercase, 1))

print(lettermap)

lettermap2 = {c: k for k, c in enumerate(ascii_lowercase, 1)}

print(lettermap2)
~~~

### set comprehensions

셋컴프는 list나 dict와 유사함. set() or{}로 사용.

~~~python
word = 'Hello'
letters1 = set(c for c in word)
letters2 = {c for c in word}
print(letters1)  # prints: {'l', 'o', 'H', 'e'}
print(letters1 == letters2)  # prints: True
~~~

이것도 중복안됨 l 하나임.

### generators -생성자

두개로 노뉨

생성자 함수: 일반함수와 유사, 그러나 리턴으로 결과대신 yield를 사용해서 각 호출 사이에서 상태를 일시중단하고 다시 시작 가능.

생성자 표현식: list comprehensions 와 유사하지만 목록대신 결과를
하나씩 생성하는 객체를 반환.

### 씨벌 생성자함수

yield 를 통해 만듬

결과를 수집하고 즉시 반환하는 대신 계산을 시작하고 하나의 값을 산출하고 다시 상태를 재개 할 수 있도록 필요한 모든 것을 저장하고 다른 단계를 다시 시작하고 수행 할 수 있습니다.

Generator 함수는 Python에 의해 자동으로 iterator로 바뀌므로, 다음에 호출 할 수 있습니다.

~~~python
def get_squares(n):  # classic function approach
    return [x ** 2 for x in range(n)]
print(get_squares(10))

def get_squares_gen(n):  # generator approach
    for x in range(n):yield x ** 2  # we yield, we don't return
print(list(get_squares_gen(10)))
~~~

아직까진 뭔차인지 모르겄다. 다만yiled에 도착할때마다 일시중단됨!
리스트로 출력안했으면.. 오브젝트값뜬다

~~~python
def get_squares_gen(n):
    for x in range(n):
        yield x ** 2
squares = get_squares_gen(4)  # this creates a generator object
print(squares)  # <generator object get_squares_gen at 0x7f158...>
print(next(squares))  # prints: 0
print(next(squares))  # prints: 1
print(next(squares))  # prints: 4
print(next(squares))  # prints: 9
# the following raises StopIteration, the generator is exhausted,
# any further call to next will keep raising StopIteration
print(next(squares)) #요거있으면 스답 stopIteration.
~~~

우리가 다음에 처음 호출 할 때, 우리는 0, 1, 4, 그리고 9의 제곱 인 0을 얻습니다. 그리고 그 이후에 for 루프가 멈추고 (n은 4입니다), 생성기는 자연스럽게 끝남

일반 함수는 None을 반환 할 것이지만 반복 프로토콜을 따르기 위해 생성기는 대신 StopIteration 예외를 발생

즉 중간에 멈추기가 가능해서 모듈끼워넣기가능. 예를들어 4에서 멈춰+5해서 만든다던지.

무엇보다 반복범위를 넘어서면 멈추는게 핵꿀.

~~~python
def geometric(a,q):
    k =0
    while True:
        result = a * q**k

        if result <= 100000:
            yield result
        else:
            return
        k += 1

for n in geometric(2,5):
    print(n)

~~~

### going beyound next

next 작동방법

next(generator)를 호출하면 generator.___next___() 메서드가 호출.

메소드는 객체에 속한 함수일뿐인걸 기억 이것의 일은 반복의 다음요소 반환
혹은 더이상 반환요소가 업스면 stopiteration발생임.

파이썬에서 객체의 특별한 메소드는 마법 메소드 또는 dunder ( "double underscore") 메소드에서 호출됩니다
-이건 뭔 개소리지.

생성자에는 세가지 기능있다. send,thow,close.
send는 generator 객체에 값을 다시 전달할 수있게하며, throw 및 close는 각각 generator 내에서 예외를 발생시키고 닫는 것을 허용.

위의 next(squares)가 아니라.squares.__next__()를 쓸수도 있긴한데.

-사실상 그냥 next(squares)랑 다르진않은듯.

~~~python
def counter(start=0):
    n = start
    while True:
        yield n
        n += 1

c = counter()

print(next(c))  # prints: 0
print(next(c))  # prints: 1
print(next(c))  # prints: 2
~~~

이러면 영원히 생성 가능.
하지만 stop = false 그리고 while true: 대신 while not stop:를 하면
stop =  true면 스답한다.

허나 이건 구리다. 파이썬답지몬함 그레서 우린 generator.send()를 사용
가능하다.generator.send ()를 호출하면 우리가 보내는 피드 값이 생성기로 전달되고 실행이 다시 시작되며 yield 식을 통해 가져올 수 있다.

복잡하니 예제 봐야됨.

~~~python

def counter(start = 0):
    n = start
    while True:
        result = yield n #A
        print(type(result),result)#b
        if result == 'Q':
            break
        n += 1

c = counter()
print(next(c))
print(c.send('Wow!'))
print(next(c))
#print(c.send('Q'))#stopiteration.
~~~

쿨한데 시펄

### the yield from expression

이 표현식을 사용하면 하위 테스터로부터 값을 얻을 수 있습니다.

~~~python
def print_squares(start, end):
    for n in range(start, end):
        yield n ** 2

for n in print_squares(2, 5):
    print(n)
~~~

~~~python
def print_squares(start, end):
    yield from(n ** 2 for n in range(start, end))

for n in print_squares(2, 5):
    print(n)
~~~

둘다 같은결과를낸다. 아래것이 조금더 짧다. 사실 내가느끼기엔 from은 별차이가 없네.

### 생성자 표현식

한 번에 하나씩 값을 생성하는 다른 기술.

list compre와 문법은 동일하다. 대괄호 대신 ()
list compre와 다 같지만 하나달름. 단 하나의 반복만 허용하면 소모된다.

~~~python

cubes = [k**3 for k in range(10)] #regular list

print(cubes)

print(type(cubes))

cubes_gen = (k**3 for k in range(10)) #create as generator

print(cubes_gen)

print(type(cubes_gen))

print(list(cubes_gen))

print(list(cubes_gen)) #nothing more to give

~~~

위와 같이 리스트 두번쨰는 안됬음. 즉 한번 반복하면 뿌서진다.

생성자로 맵.

~~~python

def adder(*n):
    return sum(n)
s1 = sum(map(lambda n: adder(*n), zip(range(100), range(1, 101))))
s2 = sum(adder(*n) for n in zip(range(100), range(1, 101)))
~~~

나머진 generator_expressions.py 참조

s1 = sum([n**2 for n in range(10**6)])
s2 = sum((n**2 for n in range(10**6)))
s3 = sum(n**2 for n in range(10**6))
의  차이.
1.list compre
2.지금이거 (생성자 표현식)
3.걍 리스트.

1번 씹허터취. 쥰내오래걸림.

>s = sum([n**2 for n in range(10**8)])  # this is killed
s = sum(n**2 for n in range(10**8))  # this succeeds
print(s)

첫번째 문장은 수십만개 제곱목록이 합쳐진게 작성되야하는데 존나커서 걍
죽여버림.

### some performance considerations -성능 조언

시간과 공간.

목록 (또는 튜플)이 필요한지 또는 간단한 생성기 함수(gene func)가 제대로 작동하는지 스스로에게 질문.

대답이 '예'일 경우 로 가면 많은 공간을 절약 할 수 있습니다. 함수에서도 마찬가지입니다.

공간.

파이썬 for는 내장머신에서 바이트코드로 실행되지만.

map과 list는 c언어 속도로 계산

즉 for가 더느리다

time 함수를 사용. 작업시간계싼.

~~~python
from time import time

mx = 5500 # this is the max I could reach with my computer...
t = time()  # start time for the for loop
dmloop = []
for a in range(1, mx):
    for b in range(a, mx):
        dmloop.append(divmod(a, b))
print('for loop: {:.4f} s'.format(time() - t))  # elapsed time

t = time()  # start time for the list comprehension

dmlist = [divmod(a, b) for a in range(1, mx) for b in range(a, mx)]
print('list comprehension: {:.4f} s'.format(time() - t))
t = time()  # start time for the generator expression
dmgen = list(
    divmod(a, b) for a in range(1, mx) for b in range(a, mx))
print('generator expression: {:.4f} s'.format(time() - t))# verify correctness of results and number of items in each list
print(dmloop == dmlist == dmgen, len(dmloop))
~~~

>for < gene ex < list compr 순으로 빠르다.

생성자 표현식(gene ex)가 list compr보다 느린이유는 list()생성자에
피드를 제공해야하기 때문

하지만 결과를 유지하지 않는다면 gene ex가 더낫다

생성자는 매우빠르며 공간절약 가능.
리스트 컴프레헤시온은 일반적으로 더 빠르지만 공간 절약 x
for는 제일느림.
map은 2와 다툴정도로빠르다.

### Don't overdo comprehensions and generators

많이 쓰면 쓸수록 compre와 생성자는 존내어려워진다.

compre과 생성자 표현은 읽기 어렵고, 암묵적이며, 복잡하고, 설명하기 어렵습니다.

유클리드 기하학 스킵.


너모 많이 쓰지말고 리팩토링도 가능하다.

### name localization 지역이름

Python 3. *는 list, dict, set 및 generator 표현식의 네 가지 형태의 모든 내포 형식으로 루프 변수를 현지화합니다.

예시.

~~~python

A = 100
ex1 = [A for A in range(5)]
print(A)  # prints: 100
ex2 = list(A for A in range(5))
print(A)  # prints: 100
ex3 = dict((A, 2 * A) for A in range(5))
print(A)  # prints: 100
ex4 = set(A for A in range(5))
print(A)  # prints: 100
s = 0
for A in range(5):
    s += A
print(A)  # prints: 4

#ex1 = [A for A in range(5)]-local.
#print(A) 이러면 실행안됨
~~~

유일하게 for문만이 a를 바꿨다.

~~~python
s = 0
for A in range(5):
    s += A
print(A)  # prints: 4
#print(globals())
~~~

앞의 코드는 for 루프 다음에 루프 변수가 정의되지 않은 경우 전역 프레임에서 루프 변수를 찾을 수 있음을 보여줍니다.

### Generation behavior in built-ins 내장함수 생성동작

built-ins 타입에는 내장동작(generation behavior)가 일반적임.
2와 3의 주요 차이점 -python

map, zip 및 filter와 같은 많은 기능이 변형되어 iterable처럼 작동하는 객체를 반환합니다.

이 변경의 배경은 해당 결과의 목록을 만들어야하는 경우 list () 클래스에서 항상 호출을 래핑 할 수 있으며 완료된 것입니다. 반대로, 반복 할 필요가 있고 가능한 한 메모리에 미치는 영향을 최소화하려면 이러한 기능을 안전하게 사용할 수 있습니다.

파이썬 2는 xrange 지금은 range

### 5과 마지막문제

피보나치 수열.

fibo 참고