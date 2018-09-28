
#h1 파이썬

스크립트언어이자 개발언어. -js,html 처럼 웹 개발가능.

중간에 c,java 등의 언어를 끼워넣기 가능. 

drawback(약점)인터프리터 형식이기에 다른 컴파일언어보다 느림.

소스코드->바이트코드 -인터프리터 실행.
그러나 이식성은 좋다. =그래서 끼워넣기 가능

하지만 오늘날엔 거의 문제가 없다.- ex)병렬

pypy 같은  고오급 기술로 평균 7배 빠르게 구현 가능

혹은 pandas나 numpy 같은 이미 구현된 라이브러리로 속도를 얻는다.

파이썬2 는 속도와는 거리가 멀다?

현재 대다수의 라이브러리는 파이썬3 버전에 포팅됨. 버전이 다르더라도 
6가지의 주요 라이브러리가 호환하긴 함.

-> 파이썬3가 최고다 이말이야.

대화형 쉘.

 >>> 후에 코드를 입력해야하며
 파이썬에서 한줄 이상의 코드가 필요할경우 
'...'로 시각적 단서를 줘서 여러줄 입력하라고 알림
->콘솔...

특별한 라이브러리를 쓰지않아도, c나 자바같은 놈들과는
 다르게 높은 자릿수 연산 가능.
ex)2의 1024승

초보자를 위한 개발환경중 IDLE도 있음. 멋진 그래픽 제공. +간단.

파이썬은 패키지라는 구조를 제공-모듈을 그룹화, init.py파일을 원래는 포함해야하나
3.3부터는 엄격하게 쳌x ->일부 폴더가아니라 실제 패키지라고 알리는 역할.

대략적인 구조.

example/ 
├── core.py 
├── run.py 
└── util   
    ├── __init__.py    
    ├── db.py    
    ├── math.py    
    └── network.py

core는 핵심로직, run은 시작로직 utill은 유틸도구
 math, network는 말그대로.

 구조체-파이선의 경우 dictionary 라고 함..
 
 여러줄에 걸쳐 정의하기에 >>>에서 ...로 교체.

>>> employee = { 
...     'age': 45, 
...     'role': 'CTO', 
...     'SSN': 'AB1234567', 
... } 

     파이썬이 네임스페이스를 검색하는 순서:
     local, enclosing, global, built-in (LEGB).

     이름이 정의 안됬으면 nameerror 발생.

파이썬은 코드를 들여쓰기 해서 범위를 정의한다.
scopes1.py # Local versus Global
# we define a function, called local 
def local():
    m = 7   
    print(m)

m = 5 
print(m)
# we call, or `execute` the function local local() 


local 이라는 함수의 정의에 속하는 코드를 보면 띄어쓰기가 된걸 볼수있음.
권장 공백수는 네개.

+ 네임스페이스, 즉 변수 이름에 따라 
정수형 char형 등을 설정 안해도 됨. 동적할당 안해도 자동으로 하는듯

29p 의문, 로컬이 먼저나와도 일단 전역부터 실행? 혹은 위에enclosing 이 아직 
호출되지 않아서인가.

파이썬의 모든 것은 객체이다. 세가지 기능을 가진, 이름. 유형. 값.

클래스 자체도 객체,-> 메타클래스, 6장에서 설명.

pep8 = 코드 컨벤션(보기 좋게 씀)을 공부하는게 좋다리.

pythonic이라는 개념?

보통의 언어는 32단일float, 64이중double 을 지원하지만,
파이썬은 이중 배정도만 지원 =64비트.
즉 float 형을 지원하지않고 전부 double임. 덕분에 근사치 문제가있다.

3.0*0.1-0.3=0이 아닌 5.551115123125783e-17 라는 거지같은 값이나옴.

근사치 문제가 있지만, 우리에겐 소수(demical)이란 것이 있다.

파이썬은 허수를 직접 지원한다. i  =-1의 제곱근.

>>> c = 3.14 + 2.73j 
>>> c.real  # real part 
3.14 
>>> c.imag  # imaginary part 
2.73
>>> c.conjugate()  # conjugate of A + Bj is A - Bj 
(3.14-2.73j) 
>>> c * 2  # multiplication is allowed 
(6.28+5.46j) 
>>> c ** 2  # power operation as well 
(2.4067000000000007+17.1444j) 
>>> d = 1 + 1j  # addition and subtraction as well 
>>> c - d 
(2.14+1.73j) 

real=실수부 imag 허수부 표현인듯. 객체 자체가 구조체여서 개꿀이넹.

분수 소수
>>> from fractions import Fraction 
>>> Fraction(10, 6)  # mad hatter? 
Fraction(5, 3)  # notice it's been reduced to lowest terms 
>>> Fraction(1, 3) + Fraction(2, 3)  # 1/3 + 2/3 = 3/3 = 1/1 
Fraction(1, 1) 
>>> f = Fraction(10, 6) 
>>> f.numerator //분자
5 
>>> f.denominator//분모
3
 + decimal.getcontext().prec에 액세스해 직접 정밀도 설정 가능.

 >>> from decimal import Decimal as D  # rename for brevity 
 >>> D(3.14)  # pi, from float, so approximation issues 
 Decimal('3.140000000000000124344978758017532527446746826171875') 
 >>> D('3.14')  # pi, from a string, so no approximation issues 
 Decimal('3.14') 
 >>> D(0.1) * D(3) - D(0.3)  # from float, we still have the issue 
 Decimal('2.775557561565156540423631668E-17')
  >>> D('0.1') * D(3) - D('0.3')  # from string, all perfect 
  Decimal('0.0')

  strings, tuples, and bytes = 불변.

  파이썬은 char가 없고 전부 str, 1자 글이면 1자짜리 str임.

  문자열 리터럴은 ','' 혹은 '''로 사용. 3중따옴표의 경우,
  문자열이 여러줄에 걸쳐져 있을 수 있다
 
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
  결과
  This too 
  is a multiline one 
  built with triple double-quotes.

  이때 딱히  아래 두줄을 쓰지 않아도 상관없음. 명시적으로 코드를 읽기 편하게 한것.
   즉 줄도 알아서 바꿔서 출력한다.
   len(객체)= 문자열 길이 출력해줌.

   문자열 앞에 b를 선언앞으로써 바이트 객체를 만든다.

   type(객체)= 현재 객체의 타입을 알려줌.
   >>> s = "This is üŋíc0de"  # unicode string: code points 
   >>> type(s) 
   <class 'str'> 
   >>> encoded_s = s.encode('utf-8')  
   # utf-8 encoded version of s 
   >>> encoded_s 
   b'This is \xc3\xbc\xc5\x8b\xc3\xadc0de'  # result: bytes object 
   >>> type(encoded_s)  # another way to verify it 
   <class 'bytes'>
   >>> encoded_s.decode('utf-8')  # let's revert to the original 'This is üŋíc0de' 
   >>> bytes_obj = b"A bytes object"  # a bytes object 
   >>> type(bytes_obj) 
   <class 'bytes'>


   인덱싱과 문자 분할= 배열과 같은 부분인덧.

    : 즉, 콜론으로 구분한다.my_sequence[start:stop:step].
   step은 그만큼 인덱스(주소)를 뜀, 여기도 0번이 처음주소.

   >>> s = "The trouble is you think you have time." 
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

튜플은 컴마로 구분, 

ex) 한줄에 여러 변수설정. 함수가 여러 객체를 반환(return)
즉, 단일명령으로 여러 요소를 만들어내는것. 이 모든예가 튜플인가/

튜플은 () 괄호로 둘러쌓음. 물론 괄호를 생략해도 무방하지만
(1,)처럼 하나의 원소일땐 뒤에 뭐가없어도 컴마 넣어줘야됨

이 친구는 a와 b의 값을 바꿀때 temp같은 추가 변수가 필요없다. 개꿀띠 

리스트와 다르게 튜플은 값의 변경이 불가능하다. -불변성.

>>> t = ()  # empty tuple 
>>> type(t) 
<class 'tuple'>
>>> one_element_tuple = (42, )  # you need the comma!
>>> three_elements_tuple = (1, 3, 5)
 >>> a, b, c = 1, 2, 3  
 # tuple for multiple assignment 
 >>> a, b, c  # implicit tuple to print with one instruction 
 (1, 2, 3) 
>>> 3 in three_elements_tuple  # membership test 
True

>>> a, b = b, a  # this is the Pythonic way to do it 
>>> a, b 
(1, 2)

근데 튜플할당 안해도 바뀌네..?-묻

리스트는 가변성있음. 그리고 튜플처럼 쉼표로 구분.

리스트 예제.

>>> []  # empty list 
[] 
>>> list()  # same as [] 
[] 
>>> [1, 2, 3]  # as with tuples, items are comma separated
[1, 2, 3] 
>>> [x + 5 for x in [2, 3, 4]]  # Python is magic //중요기능.
[7, 8, 9] 
>>> list((1, 3, 5, 7, 9))  # list from a tuple 
[1, 3, 5, 7, 9] 
>>> list('hello')  # list from a string 
['h', 'e', 'l', 'l', 'o']

파이썬의 매직.

>>> a = [1, 2, 1, 3]
>>> a.append(13) # we can append anything at the end
>>> a
[1, 2, 1, 3, 13]
>>> a.count(1) # how many '1' are there in the list?
2
>>>a.extend([5, 7]) #extend the list by another (or sequence)
>>>a
[1, 2, 1, 3, 13 , 5, 7]
>>>a.index(13) #position of '13' in the list (0-based indexing)
4
>>>a.insert(0,17) # insert '17' at position 0
>>>a
[17, 1, 2, 1, 3, 13, 5, 7]
>>>a.pop() # pop (remove and return) last element
7
>>>a.pop(3) # pop element at position 3
1
>>>a
[17, 1, 2, 3, 13, 5]
>>>a.remove(17) #remove '17' from the list
>>>a
[1, 2, 3, 13 ,5]
>>>a.reverse() # reverse the order of the elements in the list
>>>a
[5, 13, 3, 2, 1]
>>>a.sort() #sort the list
>>>a
[1, 2, 3, 5, 13]
>>>a.clear() #remove all elemnets from the list
>>>addition
[]

내용정리 객체.append = 인덱스 끝에 삽입.
count = 그 값이 리스트에 몇개나 있는지 카운팅
extend =목록 확장, 다수개의 인덱스,
혹은 타 인덱스와 통합가능한가??-확인해볼일

index() =괄호안의 값이 몇번째 인덱스인지 찾는다.
pop() = 괄호안에 아무것도 없으면 마지막 인덱스 뺌. 있다면 그 인덱스
remove()= 괄호안의 값을 모든 리스트에서 제거

reverse() 인덱스 거꾸로.
sort() 정렬.
clear() 초기화.= 모두삭제.

+리스트 기능
min(객체이름),max,sum,len 가능.

타 리스트와 + 가능, *를 할시 *한만큼 자신의 인덱스 반복.

sorted(객체) 도 가능함. 그리고 이경우. 많은 기능을 사용 가능하다.
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


위의 예제를 보면 key를 이용한다. 

이떄 key는 list에서 사용불가= 가변성이기에, 튜플에서만 가능=불변
즉 리스트안에 튜플로 이루어진 것들이라면 가능한듯.

저렇게 해두면 key 값을 기준으로 정렬한다 튜플이 두가지 이기에 0,1 까지만 
가능하며 0이면 0번쨰 기준 1이면 1번째 기준 정렬이다. reverse도 가능한듯.


혹은 단지 튜플.

bytearray----

bytearry() 로 선언하는듯

[0 256) 대괄호는 값이 포함되어있음이고 소괄호는 제외다.
즉 위 괄호안의 정수의 범위는 0이상 256미만.

예제.
>>> bytearray()  # empty bytearray object 
bytearray(b'') 
>>> bytearray(10)  # zero-filled instance with given length 
bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00') 
>>> bytearray(range(5))  # bytearray from iterable of integers 
bytearray(b'\x00\x01\x02\x03\x04')
>>> name = bytearray(b'Lina')  # A - bytearray from bytes 
>>> name.replace(b'L', b'l') 
bytearray(b'lina') 
>>> name.endswith(b'na') 
True 
>>> name.upper() 
bytearray(b'LINA') 
>>> name.count(b'L') 
1 

배터리어레이(정수)를 선언하면 그만큼의 공간이 생김. 물론 0
range(정수) 한 만큼의 공간이 정수값만큼 나옴 -1,(인덱스)

replace 교체, a를 b로

endswith는 인덱스가 맞다면 true 아니면 false 를 반환하는 bool 형임.
count는 뭐..

대화형 모드(tty - >>>,...을 사용하는)에서 마지막에 출력된 표현식은 `_`를 쓰면 그 값에 대입된다.-콘솔만임..
ex)마지막 값이 15였다면 _는 15다.

--

set과 frozenset 두가지 유형, set 가변 fro 불변  

해시가능성이란, 사전에 대한 키 뿐만 아니라 객체를 집합 멤버로사용. 해시값이 불변하면 해시가능,

동일하게 비교되는 객체는 동일한 해시 값을 가져야함.
ex)
>>> small_primes = set()  # empty set 
>>> small_primes.add(2)  # adding one element at a time 
>>> small_primes.add(3) 
>>> small_primes.add(5)
>>> small_primes
{2, 3, 5}
>>> small_primes.add(1)  # Look what I've done, 1 is not a prime! 
>>> small_primes 
{1, 2, 3, 5}
>>> small_primes.remove(1)  # so let's remove it 
>>> 3 in small_primes  # membership test 
True 
>>> 4 in small_primes 
False 
>>> 4 not in small_primes  # negated membership test 
True 
>>> small_primes.add(3)  # trying to add 3 again 
>>> small_primes 
{2, 3, 5}  # no change, duplication is not allowed 
>>> bigger_primes = set([5, 7, 11, 13])  # faster creation 
>>> small_primes | bigger_primes  # union operator `|` 
{2, 3, 5, 7, 11, 13} 
>>> small_primes & bigger_primes  # intersection operator `&` 
{5} 
>>> small_primes - bigger_primes  # difference operator `-` 
{2, 3} 

세트를 만드는 다른방법-단지 중괄호. +중복되는 값은 세트에서 아무상관이읍다.
>>> small_primes = {2, 3, 5, 5, 3} 
>>> small_primes 
{2, 3, 5} 

아래는 frozenset.

>>> small_primes = frozenset([2, 3, 5, 7]) 
>>> bigger_primes = frozenset([5, 7, 11]) 
>>> small_primes.add(11)  # we cannot add to a frozenset 
Traceback (most recent call last):  
File "<stdin>", line 1, in <module> 
AttributeError: 'frozenset' object has no attribute 'add' 
>>> small_primes.remove(2)  # neither we can remove 
Traceback (most recent call last):  
File "<stdin>", line 1, in <module> 
AttributeError: 'frozenset' object has no attribute 'remove' 
>>> small_primes & bigger_primes  # intersect, union, etc. allowed 
frozenset({5, 7}) 

사전(dictionary)-가장 흥미로운 유형??

유일한 표준, 모든 파이썬 객체의 백본

키는 해시가능 객체여야 하고 값은 임의의 유형일 수 있다.
ex) 사전을 만드는 다섯가지 방법{'A': 1, 'Z': -1}

>>> a = dict(A=1, Z=-1) 
>>> b = {'A': 1, 'Z': -1} 
>>> c = dict(zip(['A', 'Z'], [1, -1])) 
>>> d = dict([('A', 1), ('Z', -1)]) 
>>> e = dict({'Z': -1, 'A': 1}) 
>>> a == b == c == d == e  # are they all the same? 
True  # indeed!

더블이콜을

객체가 할당 될떄 하나, 다른 객체와 동일한지 검사할때 하나, 이렇게 더블이콜씀

다른 방법도 있는데 id가 같을경우 비교 가능,근데 안그러면 걍'=='

>>> list(zip(['h', 'e', 'l', 'l', 'o'], [1, 2, 3, 4, 5])) 
[('h', 1), ('e', 2), ('l', 3), ('l', 4), ('o', 5)] 
>>> list(zip('hello', range(1, 6)))  # equivalent, more Pythonic 
[('h', 1), ('e', 2), ('l', 3), ('l', 4), ('o', 5)] 


zip은 리스트가 아닌 반복자(iterator)를 반환한다.


ex)basic oper???사전으로 돌아감??

>>> d = {}
>>> d['a'] = 1  # let's set a couple of (key, value) pairs 
>>> d['b'] = 2 
>>> len(d)  # how many pairs? 
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
>>> 3 in d  # not the value.. 값으론 매칭이 안되나??
False 
>>> 'e' in d 
False 
>>> d.clear()  # let's clean everything from this dictionary 
>>> d 
{}

수행중인 작업 유형에 관계없이 사전 키를 액세스하는 방법은 대괄호를 통해 수행됩니다.

문자열, 목록 및 튜플을 기억하십니까? 대괄호를 사용하여 일부 위치의 요소에 액세스하고있었습니다. 파이썬의 일관성에 대한 또 다른 예입니다.

키,값,항목(key,values,item)의 특수한 세가지 항목에 대해 알아보자.

이 세가지는 사전의 동적보기-dynamic view. 를 제공, 사전이 변경될떄 변경된다.

key()는 사전에 있는 모든 키를 반환하고, value()은 사전의 모든 값을 반환하며, items()은 사전의 모든 (key, values) 쌍을 반환합니다.

사전이 본질적으로 정렬되지 않은 경우에도 Python 설명서에 따라 다음과 같이 알아야합니다. "키와 값은 무작위 순서가 아닌 임의 순서로 반복되며 Python 구현에 따라 다르며 사전의 기록에 따라 다릅니다 키, 값 및 항목보기가 사전에 개입하지 않고 반복되는 경우 항목 순서가 직접 일치합니다. "

>>> d = dict(zip('hello', range(5)))
>>> d 
{'e': 1, 'h': 0, 'o': 4, 'l': 3} #가 2와3임. zip에 의해
>>> d.keys() 
dict_keys(['e', 'h', 'o', 'l'])#2와3이 쌍을 이룬다.
>>> d.values() 
dict_values([1, 0, 4, 3]) #사전에서 l의 두번째가 첫번쨰를 덮어씌움.
>>> d.items() 
dict_items([('e', 1), ('h', 0), ('o', 4), ('l', 3)]) 
>>> 3 in d.values() 
True 
>>> ('o', 4) in d.items() 
True

주목할 점은 뷰를 요청하면 원래의 순서가 손실된다. 그러나 뷰
내에서는 일관된다.- 내부가 어떻듯 보이는건 또옥같은듯.

그리고 다시 컴퓨터에서 코드를 돌리면 다른결과가 나올수도있음.
뷰가 제공되는 순서의 일관성만 보장한다고한다.

>>> d
{'e': 1, 'h': 0, 'o': 4, 'l': 3}
>>> d.popitem()  # removes a random item
('e', 1)
>>> d
{'h': 0, 'o': 4, 'l': 3}
>>> d.pop('l')  # remove item with key `l`
3
>>> d.pop('not-a-key')  # remove a key not in dictionary: KeyErrorTraceback (most recent call last):
  File "<stdin>", line 1, in <module>
  KeyError: 'not-a-key'
  >>> d.pop('not-a-key', 'default-value')  # with a default value?'default-value'  # we get the default value
  >>> d.update({'another': 'value'})  # we can update dict this way
  >>> d.update(a=13)  # or this way (like a function call)
  >>> d
  {'a': 13, 'another': 'value', 'h': 0, 'o': 4}
  >>> d.get('a')  # same as d['a'] but if key is missing no KeyError
  13
  >>> d.get('a', 177)  # default value used if key is missing
  13
  >>> d.get('b', 177)  # like in this case
  177
  >>> d.get('b')  # key is not there, so None is returned

파이썬은 기본적으로 모든 함수가 none을 반환(return)한다. 명시적으로 설정하지 않는한. 그러나 우리가 기능을 탐색할때 볼수있음.

false none 둘다 false를 가리키기는 함. 그러나 차이가있다.

사전의 setdefalut 기능 예제.

>>> d = {}
>>> d.setdefault('a', 1)  # 'a' is missing, we get default value
1
>>> d
{'a': 1}  # also, the key/value pair ('a', 1) has now been added
>>> d.setdefault('a', 5)  # let's try to override the value1
>>> d
{'a': 1}  # didn't work, as expected

>>>d = {}
>>>d.setdefault('a', P{}).setdefalut('b', []).append(1)

#h2 collection modeul.

nametuple()  네임필드를 써서 튜플 서브클래스를 만드는 공장함수.
deque 양쪽 끝에 빠른 팝과 추가기능이 있는 리스트 같은 컨테이너.
chainMap 멀티 맵핑에서 싱글 뷰를 만드는 딕트 같은 클래스.-여러가지 맵핑을 단일보기를 위해하는건가??
Counter 해시 오브젝트를 카운팅하는 딕트서브클래스
OrderedDict 추가된 주문 항목을 기억하는 딕트 서브클래스
defalutdict 누락된 값을 제공하는 공장 기능을 호출하는 딕트서브클래스
Userdict 용이한 딕트 서브클래스를 위한 근처 사전 포장?
UserList 리스트의 서브클래스를 쉽게 하기위한것.
UserString 문자열 서브클래싱을 위한 래퍼.



#h2 named tupels.

속성 검색을 통해 필드에 액세스가능하고 색인화 및 반복 가능한 튜플과 비슷한 개체(튜플의 서브클래스.)

>>> vision = (9.5, 8.8)
>>> vision
(9.5, 8.8)
>>> vision[0]  # left eye (implicit positional reference)
9.5
>>> vision[1]  # right eye (implicit positional reference)
8.8


>>> from collections import namedtuple
>>> Vision = namedtuple('Vision', ['left', 'right'])
>>> vision = Vision(9.5, 8.8)
>>> vision[0]
9.5
>>> vision.left  # same as vision[0], but explicit
9.5
>>> vision.right  # same as vision[1], but explicit
8.8

Vision = namedtuple('Vision', ['left', 'combined', 'right'])
vision = Vision(9.5, 9.2, 8.8)
vision.left  # still perfect
9.5
vision.right  # still perfect (though now is vision[2])
8.8
print(vision.combined)  # the new vision[1]
9.2

named tuple= 선언+이름으로인덱스에 접근하는 친구

#h2 Defalutdict

키가 사전에 있는지 검사하는 도구.

>>> d = {}
>>> d['age'] = d.get('age', 0) + 1  # age not there, we get 0 + 1
>>> d
{'age': 1}
>>> d = {'age': 39}
>>> d['age'] = d.get('age', 0) + 1  # d is there, we get 40
>>> d
{'age': 40}

>> from collections import defaultdict
>>> dd = defaultdict(int)  # int is the default type (0 the value)>>> dd['age'] += 1  # short for dd['age'] = dd['age'] + 1
>>> dd
defaultdict(<class 'int'>, {'age': 1})  # 1, as expected
>>> dd['age'] = 39
>>> dd['age'] += 1
>>> dd
defaultdict(<class 'int'>, {'age': 40})  # 40, as expected

#h2 chainmap

다수의 매핑을 연결해 단일유닛으로 취급.

>>>from collections import ChainMap
>>> default_connection = {'host': 'localhost', 'port': 4567}
>>> connection = {'port': 5678}
>>> conn = ChainMap(connection, default_connection) # map creation
>>> conn['port']  # port is found in the first dictionary
5678
>>> conn['host']  # host is fetched from the second dictionary
'localhost'
>>> conn.maps  # we can see the mapping objects
[{'port': 5678}, {'host': 'localhost', 'port': 4567}]
>>> conn['host'] = 'packtpub.com'  # let's add host
>>> conn.maps
[{'host': 'packtpub.com', 'port': 5678}, {'host': 'localhost', 'port': 4567}]
>>> del conn['port']  # let's remove the port information
>>> conn.maps
[{'host': 'packtpub.com'}, {'host': 'localhost', 'port': 4567}]
>>> conn['port']  # now port is fetched from the second dictionary
4567
>>> dict(conn)  # easy to merge and convert to regular dictionary
{'host': 'packtpub.com', 'port': 4567}


#h2 small values caching

값이 큰 두개의 다른 객체가 생성될때 그 값이 같다해도 id를 비교하면 다르게나오지만 만약 값이 작은 ex)5 라면 같게 나올수도있음..
id를 사용할때 작은값은 주의하자.


#h2 데이터 구조 선택

컬렉션이 추가or 축소 x = 튜플 o= 목록 이 좋다. 사전도 가능

기억하자. {} 객체, () 튜플 []리스트 {id:값} 사전

리스트는 o(n)이 걸린다.
-c,java언어를 기억하자 코드를내부에서 해주는 것일뿐 시간은 동등하다

사전의 경우 o(1)의 목록삽입,제거 기능이 있지만.. 각 속성으로 고유하게 식별(키) +해시가능해야함

>>> a = list(range(10))  # `a` has 10 elements. Last one is 9.
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> len(a)  # its length is 10 elements
10
>>> a[len(a) - 1]  # position of last one is len(a) - 1
9
>>> a[-1]  # but we don't need len(a)! Python rocks!
9
>>> a[-2]  # equivalent to len(a) - 2
8
>>> a[-3] #equivalent to lea(a) -3
7

#h2  4과
 
#h3 lterating and Making Decisions

흐름 제어를 위해서는 분기와 루핑이 있다.

#h3 conditional pro

조건부 프로그래밍 or 브랜칭

#h3 the ternary operator 삼 연산자


반복
surnames = ['Rivest', 'Shamir', 'Adleman']
for position, surname in enumerate(surnames):
    print(position, surname)

    인덱스, 요소값 전부 출력 개꿀따리

#h4 iterator.

파이썬 문서에 따르면 iterable은 "한 번에 하나씩 멤버를 반환 할 수있는 객체입니다. iterables의 예로는 모든 시퀀스 유형 (list, str 및 tuple과 같은)과 dict, file과 같은 일부 비 시퀀스 유형 객체 및 개체를 __iter __ () 또는 __getitem __ () 메서드로 정의 할 수 있습니다. 반복문은 for 루프 및 시퀀스가 필요한 많은 다른 위치에서 사용할 수 있습니다 (zip (), map (), ...). ).

  반복 가능한 객체가 내장 함수 iter ()에 인수로 전달되면 객체의 반복자를 반환합니다. 이 반복자는 값 집합에 대해 한 번만 수행하면 좋습니다. iterables를 사용할 때 iter ()를 호출하거나 iterator 객체를 직접 다룰 필요는 없다. for 문은 루프의 지속 기간 동안 반복자를 유지하기 위해 이름이 지정되지 않은 임시 변수를 생성하여 자동으로 수행합니다. "

for가 다음요소에 의해 zip을 요청하면 객체가아니라 튜플을 되찾는다.
zip에 공급하는 시퀀스만큼 튜플가져옴
people = ['Jonas', 'Julio', 'Mike', 'Mez']
ages = [25, 30, 31, 39]
for person, age in zip(people, ages):    
    print(person, age)

이때 객체들의 인덱스 크기가 다르면 같은 곳 까지만 가져옴
즉 모든 객체들의 인덱스 크기가 같은곳끼리만 반복.

remainders = remainders[::-1] #인덱스를 역순으로 바꿔버림.

raise 기능이 뭔지 알자.

count 클래스는 계산을 계속할 반복자를 만듭니다.

itertools lib count.
from itertools import count
for n in count(5, 3):    #(range(5,20+1 ,3))이랑 다른게뭐지
if n > 20:        
break    
print(n, end=', ')  # instead of newline, comma and space

이 반복자는 셀렉터의 해당 항목에 따라 데이터를 True 또는 False로 반환합니다. compress ( 'ABC', (1, 0, 1))는 'A'와 'C'를 반환합니다.

from itertools import compress
data = range(10)
even_selector = [1, 0] * 10
odd_selector = [0, 1] * 10

even_numbers = list(compress(data, even_selector))
odd_numbers = list(compress(data, odd_selector))

print(odd_selector)
print(list(data))
print(even_numbers)
print(odd_numbers)

문자열의 순열. abc=3! 3*2*1   

from itertools import permutations
print(list(permutations('ABC')))


#h2 4장 

파이썬은 반환 형식이 없어도 항상 무언가를 반환, 아무것도 안하면
NONE이 반환.

함수 존나좋음

전역,지역

nonlocal로 객체를 선언한다면 가장 인접한 바인딩까지 값 유지.(원래 내부함수를 벗어나면 사라지지만 외부함수까지 가능맨-글로벌 제외.)

만약 로컬 내에서 global로 선언한다면 전역객체

매개변수에 대해 중요한 3가지 사항

1.인수 전달은 객체를 지역 변수 이름에 할당하는 것입니다.
2.함수 내에서 인수 이름에 객체를 할당해도 호출자는 영향x
3.함수에서 변경 가능한 객체 인수를 변경하면 호출자가 영향o

5가지의 매개변수 입력방법이있음.

포지셔널.

왼쪽에서 오른쪽으로 넣기.
>def func(a, b, c):    
  print(a, b, c)
func(1, 2, 3)  # prints: 1 2 3

키드워 및 기본값.

name=valur구문을 사용,키워듭려로 할당
>def func(a, b, c):    
    print(a, b, c)
func(a=1, c=2, b=3)  # prints: 1 3 2


>def func(a, b=4, c=88):    
    print(a, b, c)
func(1)              # prints: 1 4 88
func(b=5, a=7, c=9)  # prints: 7 5 9
func(42, c=9)        # prints: 42 4 9
2가지 중요한점.

우선, 위치 지정 매개 변수 왼쪽에 기본 인수를 지정할 수 없습니다.
둘째, 예제에서 argument_name = value syntax를 사용하지 않고 인수가 전달되는 경우 목록의 첫 번째 인수 여야하며 항상 a에 할당됩니다.

가변 위치.
>def minimum(*n):
    # print(n)  # n is a tuple
    if n:  # explained after the code             mn = n[0]        
        for value in n[1:]:            
            if value < mn:                
                mn = value        
        print(mn)
        
minimum(1, 3, -7, 9)  # n = (1, 3, -7, 9) - prints: -7
minimum()             # n = () - prints: nothing

객체 이름 앞에 *를 붙이면 가변인수임.

def func(*args):    
    print(args)
     
values = (1, 3, -7, 9)
func(values)   # equivalent to: func((1, 3, -7, 9))
func(*values)  # equivalent to: func(1, 3, -7, 9)

*VALUE로 하면 튜플을 언패킹함.

가변 키워드

*대신 **로 됨+ 사전에 수집.

def func(**kwargs):    
    print(kwargs)
# All calls equivalent. They print: {'a': 1, 'b': 42}
func(a=1, b=42)
func(**{'a': 1, 'b': 42})
func(**dict(a=1, b=42))

def connect(**options):    
    conn_params = {
                'host': options.get('host', '127.0.0.1'),        'port': options.get('port', 5432),        'user': options.get('user', ''),        'pwd': options.get('pwd', ''),
    }
    print(conn_params)    
    # we then connect to the db (commented out)    
    # db.connect(**conn_params)
connect()
connect(host='127.0.0.42', port=5433)
connect(port=5431, user='fab', pwd='gandalf')

위의 예제를 보면 알겠지만 사전 매개변수가 들어가면 기존의 값을 덮기 가능.


키워드 온리

가변위치 인수 뒤 혹은 맨뒤에 *로 사용.

def kwo(*a, c):    
    print(a, c)kwo(1, 2, 3, c=7)  # prints: (1, 2, 3) 7
kwo(c=4)           # prints: () 4
(#) kwo(1, 2)  # breaks, invalid syntax, with the following error
(#) TypeError: kwo() missing 1 required keyword-only argument: 'c'
def kwo2(a, b=42, *, c):    
    print(a, b, c)
kwo2(3, b=7, c=99)  # prints: 3 7 99
kwo2(3, c=13)       # prints: 3 42 13
(#) kwo2(3, 23)  # breaks, invalid syntax, with the following error# TypeError: kwo2() missing 1 required keyword-only argument: 'c'



결합 입력 인수

다음의 규칙을 따르면 매개변수를 결합가능하다.
• 함수를 정의 할 때는 일반적인 위치 인수가 먼저오고 그 다음 기본 인수 (name = value), 변수 위치 인수 (* name 또는 간단히 *), 키워드 만있는 인수

(이름 또는 이름 = 값 형식이 좋음), 그리고 임의의 가변 키워드 인수 (** 이름).

• 함수를 호출 할 때 인수는 먼저 위치 인수 (값), 키워드 인수 (name = value), 가변 위치 인수 (* name), 변수 keyword 인수 (** 이름).

def func(a, b, c=7, *args, **kwargs):
    print('a, b, c:', a, b, c)
    print('args:', args)
    print('kwargs:', kwargs)
    
func(1, 2, 3, *(5, 7, 9), **{'A': 'a', 'B': 'b'})
func(1, 2, 3, 5, 7, 9, A='a', B='b')  # same as previous one


def func_with_kwonly(a, b=42, *args, c, d=256, **kwargs):
    print('a, b:', a, b)
    print('c, d:', c, d)
    print('args:', args)
    print('kwargs:', kwargs)
    # both calls equivalent
func_with_kwonly(3, 42, c=0, d=1, *(7, 9, 11), e='E', f='F')
func_with_kwonly(3, 42, *(7, 9, 11), c=0, d=1, e='E', f='F')

#h2 함정을 피해라, 변경가능기본값

디폴트 값이 Deftime에 생성된다는 것이다. 

따라서 동일한 기능에 대한 후속 호출은 해당 기본값의 변동에 따라 다르게 동작할 수 있다

def func(a=[], b={}):
    print(a)
    print(b)
    print('#' * 12)
    a.append(len(a))  # this will affect a's default value    
    b[len(a)] = len(a)  # and this will affect b's one
func()
func()
func()


#h2 리턴값

파이썬은 여러개의 리턴값(튜플)을 반환가능.

def func():
    pass

func()  # the return of this call won't be collected. It's lost.
a = func()  # the return of this one instead is collected into `a`
print(a)  # prints: None

예제와 같이 반환값이 없으면 none을 호출 

def factorial(n):
    if n in (0, 1):
        return 1    
    result = n    
    for k in range(2, n):        
        result *= k
    return result
f5 = factorial(5)  # f5 = 120

혹은
from functools import reduce
from operator import mul
def factorial(n):    
    return reduce(mul, range(1, n + 1), 1)
f5 = factorial(5)  # f5 = 120

#h2 반환 멀티값

튜플을 명시적으로 혹은 암시적으로 사용하면 가능.

def moddiv(a, b):
    return a // b, a % b
print(moddiv(20, 7))  # prints (2, 6)


#h2 여러가지 유용한 팁.

함수는 한가지를 해야한다.
기능은 작아야한다.
입력매개변수가 작으면 작을수록 좋다.
함수는 반환값에서 일관성을 가져야한다.
함수에는 부작용이 없어야한다, 즉 함수는 호출한 값에 영향을 미치지 않는다.

#h2 회귀(재귀) 함수.

def factorial(n):
    if n in (0, 1):  # base case        
        return 1    
    return factorial(n - 1) * n
print(factorial(5))


#h2 불명 함수.(람다)

이름이 필요없는 한줄짜리 코드함수.

5의 배수코드를 그냥짰을때

def is_multiple_of_five(n):    
    return not n % 5
def get_multiples_of_five(n):    
    return list(filter(is_multiple_of_five, range(n)))
print(get_multiples_of_five(50))

람다

def get_multiples_of_five(n):    
    return list(filter(lambda k: not k % 5, range(n)))
print(get_multiples_of_five(50))

 func_name = lambda [parameter_list]: expression. A function object is returned, which is equivalent to this: def func_name([parameter_list]): return expression

def adder(a, b):    
    return a + b
    # is equivalent to:
adder_lambda = lambda a, b: a + b


#h2 함수특징.

함수 호출

def multiplication(a, b=1):
    """Return a multiplied by b. """    
    return a * b
special_attributes = [    "__doc__", "__name__", "__qualname__", "__module__",    "__defaults__", "__code__", "__globals__", "__dict__",    "__closure__", "__annotations__", "__kwdefaults__",]

for attribute in special_attributes:
    print(attribute, '->', getattr(multiplication, attribute))

#h2 마지막문제

#h2 니 코드 문서화
def square(n):
"""Return the square of a number n. """
    return n ** 2
def get_username(userid):
    """Return the username of a user given their id. """
    return db.get(user_id=userid).username??

#객체 가져오기.

가장 흔한 두가지 방법.
import module_name and from module_name import function_name

form import module_name은 module_name 모듈을 찾고 import 문이 실행되는 로컬 네임 스페이스에서 그 모듈의 이름을 정의합니다.

from module_name import function_name 식별자의 형식은 그보다 조금 더 복잡하지만 기본적으로 동일한 작업을 수행합니다. module_name을 찾아 속성 (또는 서브 모듈)을 검색하고 식별자에 대한 참조를 로컬 이름 공간에 저장합니다.

두 양식 모두 as절을 잉용 오브젝트 이름변경 가능
from mymodule import myfunc as better_named_func

라이브러리 예제

import unittest  # imports the unittest module
from math import sqrt  # imports one function from math
from random import randint, sample  # two imports at once
from mock import patch
from nose.tools import (  # multiline import
    assert_equal,    
    assert_list_equal,
    assert_not_in,
)
from karma import nt, utils
??안되는걸 구버전꺼용인가


프로젝트의 루트에서 파일 구조가 시작되면 도트 표기법을 사용하여 패키지, 모듈, 클래스, 함수 또는 현재 네임 스페이스로 가져올 개체로 가져올 수 있습니다. 다른 것.

  from 모듈 가져 오기 구문을 사용하면 모듈의 모든 이름을 현재 네임 스페이스에 한 번에 가져 오는 데 사용되는 import * 모듈의 catch-all 절을 사용할 수도 있습니다.

그러나 몇 가지 이유 때문에 눈살을 찌푸리게됩니다.

공연, 다른 이름을 암묵적으로 가릴 위험 등이 있습니다.

각 모듈의 코드를 보여주기 전에 파이썬에게 실제로 패키지라는 것을 알리기 위해서는 __init__.py 모듈을 넣어야합니다.

예제

funcdef.py

    def square(n):    
        return n ** 2
    def cube(n):
        return n ** 3
        
    
위의 객체 모듈을 가져오는 두가지 형식

func_import.py

import lib.funcdef
print(lib.funcdef.square(10))
print(lib.funcdef.cube(10))

func_from.py
from lib.funcdef import square, cube
print(square(10))
print(cube(10))

가져온 방법에따라  액세스 방법이 틀림

#h2 relative imports

우리가 지금까지 한 import는 절대적이지만-전체 경로 정의. 객체 경로 정의- 상대적으로 import(가져오는 방법)도 있다.

상대적 수입은 우리가 찾고있는 것을 찾기 위해 역행해야 할 폴더의 수만큼 모듈 앞에 많은 점을 추가함으로써 이루어집니다.



from .mymodule import myfunc
