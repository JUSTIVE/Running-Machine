
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
3.14 >>> c.imag  # imaginary part 
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