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
>>> c ** 2  # power operation as well(2.4067000000000007+17.1444j)>>> d = 1 + 1j  # addition and subtraction as well>>> c - d(2.14+1.73j)
```