# Functions, the building blocks of Code

이 장에서는 `함수`에 대해 다룬다. `함수`란, 하나의 작업을 하는 명령어의 묶음 단위이다.

파이썬에서의 함수는 `def 함수이름 ():`으로 정의된다. 그 이후 4개의 스페이스(PEP8기준)의 인덴트가 된 몸체가 있다.

함수는 반환값을 가질 수 도 있고 가지지 않을 수도 있다. 만약 반환값을 가진다면, `return`키워드를 사용한다. 사실 파이썬에서의 함수는 명시적으로 `return`문을 작성하지 않더라도 반환값 `None`을 가진다.

## 왜 함수써요

- 코드의 중복을 막을 수 있다
- 큰 문제를 작은 단위로 나눌 수 있다
- 구현체을 이용자로부터 숨길 수 있다
- 추적을 쉽게 한다
- 가독성을 높인다

## 범위와 이름 해상도

```python
# scoping.level.1.py
def my_function():
    test = 1 # this is defined in the local scope of the function
    print('my_function:',test) # 1

test = 0 # this is defined in the global scope
my_function()
print('global:',test) # 0
```

위의 예제에서는 전역 범위에서의 test = 0 과 지역 번위에서의 test = 1 를 사용했다.

```python
# scoping.level.2.py
def outer():
    test = 1 # outer scope  
    def inner():
        test = 2
        print('inner',test) # 2
    inner()
    print('outer',test) # 1
test = 0
outer()
print('global',test) # 0
```

앞에서 살펴본 LEGB를 다시 떠올리자. 그리고 파이썬에서 함수 안에 함수를 정의할 수 있게 하는 것도 확인하라.

## 전역과 비지역 선언

위의 예제들에서 섀도잉에서 발생하는 일들을 `global`과 `nonlocal`키워드를 이용해서 바꿀 수 있다. 다음의 예제를 보자.

```python
# scoping.level.2.nonlocal.py
def outer():
    test = 1 # outer scope
    def inner():
        nonlocal test
        test = 2 # nearest enclosing scope
        print('inner',test) # 2
    inner()
    print('outer',test) # 2
test = 0
outer()
print('global',test) # 0
```

위의 예제에서 사용된 `nonlocal`은 전역 범위를 제외한 나머지 영역에서만 사용이 가능하다. 다음의 예제를 통해 `global`키워드를 알아보자.

```python
# scoping.level.2.global.py
def outer():
    test = 1 #outer scope
    def inner():
        global test
        test = 2 # global scope
        print('inner',test) # 2
    inner()
    print('outer',test) # 1
test = 0 # global scope
outer()
print('global',test) # 2
```

## 입력 파라미터

함수에 파라미터를 넘긴다는 것을 이해하기 위해 다음의 내용들을 보라.

- 인자를 넘긴다는 것은 객체를 지역 변수 이름에 배정하는 것과 다를 바가 없다.
- 함수 내에서 인자 이름에 객체를 할당하는 것은 호출자에게 영향을 주지 않는다.
- 함수 내에서 가변 객체를 바꾸는 것은 호출자에게 영향을 준다.

### 입력 파라미터를 정의하는 법

#### 위치적 인자

위치적 인자는 왼쪽부터 오른쪽으로 읽으며 인자의 대표적인 종류이다.

```python
def func(a,b,c):
    print(a,b,c)
func(1,2,3) # prints 1 2 3
```

#### 키워드 인자와 기본값

`키워드 인자`는 `name=value`문법으로 키워드를 통해 배정하는 것이다.

```python
def func(a,b,c):
    print(a,b,c)
func(a=1, c=2, b=3) #prints 1 3 2
```

`키워드 인자`는 함수를 호출하 때 위치적 인자를 무시하고 수행된다. 키워드가 맞는다면, 위치가 맞지 않더라도 수행한다.

정의하는 쪽에서의 대응되는 개념으로는 `기본값`이 있다. 문법은 `name=value`형태로 똑같다.

```python
# arguments.default.py
def func(a, b=4, c= 88)
    print(a,b,c)
func(1)             # prints 1 4 88
func(b=5, a=7, c=9) # prints 7 5 9
func(42, c=9)       # prints 42 4 9
```

여기서 알아둬야 할 것이 두 가지 있다.

- 위치적 인자의 왼쪽에 기본값을 넘길 수 없다.
- name=value로 넘겨지지 않은 인자들은 왼쪽부터 채워진다.

#### 가변 위치적 인자

때로는 가변적인 수의 위치적 인자가 필요할 때가 있다. 다음의 예제를 보자.

```python
# arguments.variable.positional.py
def minimum(*n):
    # print (n) # n is a tuple
    if n:
        mn = n[0]
        for value in n[1:]:
            if value<mn:
                mn = value
        print(mn)
minimum(1,3,-7,9) # prints -7
minimum() # prints nothing
```

위에서 보듯, *를 이름앞에 붙임으로써 인자가 가변적인 개수를 가진 위치적 인자라는 것을 알려주었다. 함수 내에서 n은 튜플로 작동하였다.

위에서 n이 비어있는지 확인하기 위해 `if n:`을 사용한 것을 보았는가? 모든 콜렉션은 비어있지 않은 경우 `True`를, 비어있는 경우 `False`를 반환한다.

#### 가변 키워드 인자

가변 키워드 인자는 가변 위치적 인자와 매우 비슷하다. 단 하나의 차이점은 \*\*를 \* 대신 이용한다는 것이다. 다음의 예제를 보자.

```python
# arguments.variable.keyword.py
def func(**kwargs):
    print(kwargs)
#All calls equivalent. They print {'a':1, 'b':42}
func(a=1,b=42)
func(**{'a'=1,'b'=42})
func(**dict(a=1,b=42))
```

#### 키워드 전용 인자

파이썬 3는 새로운 종류의 인자인 `키워드-전용 인자`를 지원한다. 이는 주로 쓰이지 않는다. 이를 사용하는 방법은 두 가지인데, 첫 번째는 위치적 인자 뒤에 쓰는 것이나, 혹은 \*만을 쓰는 것이다. 두 가지의 예제를 보자.

```python
# arguments.keyword.only.py
def kwo(*a,c):
    print(a, c)
kwo(1,2,3,c=7)  # prints (1,2,3) 7
kwo(c=4)        # prints () 4
# kwo(1,2)      # breaks, invalid syntax, with the following error
# TypeError: kwo missing 1 required keyword-only argument: 'c'

def kwo2(a,b=42,*,c):
    print(a,b,c)
kwo2(3,b=7,c=99)#prints 3 7 99
kwo2(3,c=13)    #prints 3 42 13
# kwo2(3,23)    #breaks, invalid syntax, with the following error
# TypeError: kwo2() missing 1 required keyword-only argument: 'c'
```

### 입력 파라미터 조합하기

다음의 규칙만 만족한다면 앞서 다룬 인자의 종류르 섞어서 사용할 수 있다.

- 함수를 정의할 때, 다음의 순서로 인자를 정의한다
  - `위치적 인자(name)`
  - `기본값(name=value)`
  - `가변 위치적(*name / *)`
  - `키워드-전용 인자(name,name=value)`
  - `가변 키워드 인자(**name)`
- 반면 함수를 호출할 때에는, 인자는 다음의 순서로 주어져야 한다.
  - `위치적 인자(value)`
  - `키워드 인자의 아무 조합(name=value)`
  - `가변 위치적 인자(*name)`
  - `가변 키워드 인자(**name)`

다음의 예제를 보자.

```python
# arguments.all.py
def func(a,b,c=7, *args, **kwargs):
    print(a,b,c)
    print(args)
    print(kwargs)
func(1,2,3,*(5,7,9),**{'A':'a','B':'b'})
func(1,2,3,5,7,9,A='a',B='b')
```

### 함정을 피하라! 가변 기본들

파이썬의 기본값들이 def 시간에서 생성되기 때문에 같은 함수의 후속 호출은 기본값의 가변성에 따라 다르게 동작할 수 있다. 다음의 예제를 보자.

```python
# arguments.defaults.mutable.py
def func(a=[], b={}):
    print(a)
    print(b)
    print('#' * 12)
    a.append(len(a))  # this will affect a's default value
    b[len(a)] = len(a)  # and this will affect b's one
func()
func()
func()
```

위의 결과는 다음과 같이 나온다.

```bash
$ python arguments.defaults.mutable.py
[]
{}
############
[0]
{1: 1}
############
[0, 1]
{1: 1, 2: 2}
############
```

이는 매우 신기하고 이상할 수 있으나, 메모이제이션과 같은 기술들을 다룰 때 편리하게 사용할 수 있다.

더 흥미로운 것은 다음의 예와 같이 호출들 사이에 기본값을 사용하지 않는 것이다.

```python
# arguments.defaults.mutable.intermediate.call.py
func()
func(a=[1,2,3],b={'B':1})
func()
```

위의 코드를 실행하면 다음의 결과를 볼 수 있다.

```bash
$ python arguments.defaults.mutable.intermediate.call.py
[]
{}
############
[1, 2, 3]
{'B': 1}
############
[0]
{1: 1}
############
```

위의 예제를 보면 기본값을 사용하지 않더라도 기본값은 계속 남아있다는 것이다. 어떻게 하면 매 호출마다 기본값을 얻을 수 있을까? 정답은 다음과 같다.

```python
# arguments.defaults.mutable.no.trap.py
def func(a=None):
    if a is None:
        a = []
    #이제 a는 마음껏 써도 된다
```

위의 코드를 통해 기본값 인자가 비어있는 경우, 항상 새 기본값을 넘겨줄 수 있다.

## 반환 값

함수의 반환값은 파이썬이 다른 언어들보다 몇 년은 앞서있는 것 중 하나이다. 함수는 보통 하나의 객체만을 반환할 수 있지만, 파이썬에서는 튜플을 통해 원하는 만큼 반환할 수 있다. 함수에서 값을 반환하기 위해 `return`키워드를 사용해야 하며, 함수의 몸체에는 여러 개의 `return`키워드가 사용될 수 있다. 반면, 함수의 몸체에 `return`이 없는 경우, 함수는 None을 반환한다. 이 동작은 무해하며, 파이썬이 일관된 언어이며, 흥미로운 패턴을 쓸 수 있게 한다. 이것이 무해하다는 것을 다음의 예제를 통해 확인해보자.

```python
# return.none.py
def func():
    pass
func()      # the return of this call won't be collected. It's lost.
a = func()  # the return of this one instead is collected into 'a'
print(a)    # prints None
```

함수의 몸체가 `pass`로만 구성된 것을 보라. 공식 문서에 따르면 `pass`는 null operation이다. 이는 placeholder로써 매우 유용하다.

### 다중 값 반환

다른 언어들과는 달리, 파이썬에서는 다중 객체를 반환하는 것이 매우 쉽다. 이는 튜플을 이용한다. 다음의 예제로 확인해보자.

```python
# return.multiple.py
def moddiv(a,b):
    return a//b, a%b
print(moddiv(20,7)) #prints (2,6)
```

## 꿀팁들

함수를 쓸 때 다음의 가이드를 따르면 좋다.

- `함수는 하나의 동작만 해야 한다`: 여러 동작을 하는 함수는 작음 함수로 쪼개질 수 있다. 작은 함수는 쓰기도 읽기도 이해하기도 쉽다.
- `함수는 작아야 한다`: 작은 함수는 테스트하기도 쓰기도 쉽다.
- `적은 인자가 더 좋다`: 인자를 많이 받는 함수는 관리하기 어려워진다.
- `함수는 반환값에 일관성이 있어야 한다`: False나 None이 False로 평가되더라도 일관성 있는 타입으로 쓰자
- `함수는 부작용이 없어야 한다`

## 재귀 함수

알지?

## 익명 함수

마지막으로 다룰 것은 익명 함수이다. 익명함수는 파이썬에서 람다라 불리며, 원하는 동작을 하는 한 줄짜리 코드이다.

예를 들어 N까지 5의 배수인 숫자들을 리스트 하고싶을 때, 함수와 iterable을 입력받는 `filter`함수를 이용해서 구한다고 하자. 익명함수를 쓰지 않은 예제는 다음과 같다.

```python
# filter.regular.py
def is_multiple_of_five(n):
    return not n%5
def get_multiples_of_five(n):
    return list(filter(is_multiple_of_five,range(n)))
print(get_multiples_of_five(50))
```

위의 코드를 람다를 이용해서 구해보자.

```python
# filter.lambda.py
def get_multiples_of_five(n):
    return list(filter(lambda k:not k%5,range(n)))
print(get_multiples_of_five(50))
```

람다를 정의하는 것은 다음과 같다. `func_name = lambda[parameter_list]:expression` 이는 함수 객체가 반환되며, 이는 다음과 같다. `def func_name([parameter_list]):return expression`

## 함수 속성

모든 함수는 온전한 객체이므로 많은 속성을 가지고 있다. 그 중 일부는 런타임에서 함수 객체를 검사하기 위해 사용될 수 있다.

```python
# func.attributes.py
def multiplication(a, b=1):
    """Return a multiplied by b."""
    return a * b
special_attributes = [
    "__doc__", "__name__", "__qualname__", "__module__",    "__defaults__", "__code__", "__globals__", "__dict__",    "__closure__", "__annotations__", "__kwdefaults__",
]

for attribute in special_attributes:
    print(attribute,'->',getattr(multiplication,attribute))
```

위의 실행 결과는 다음과 같다.

```bash
$ python func.attributes.py
__doc__ -> Return a multiplied by b.
__name__ -> multiplication
__qualname__ -> multiplication
__module__ -> __main__
__defaults__ -> (1,)
__code__ -> <code object multiplication at 0x7ff529e79300, file "ch4/func.attributes.py", line 1>
__globals__ -> {... omitted ...}
__dict__ -> {}
__closure__ -> None
__annotations__ -> {}
__kwdefaults__ -> None
```

## 내장 함수

파이썬에는 내장 함수가 더럽게 많다. `builtin`모듈을 `dir(__builtin__)`과 같이 찾아볼 수 있다. 파이썬에는 내장함수가 진짜 더럽게 많아서 여기에 다 쓰지 않겠다.

## 코드를 문서화하기

파이썬은 `docstrings`라는 문자열로 문서화되어 있다. 이는 한 줄 혹은 여러 줄로 쓰일 수 있다. 큰따옴표 3개를 통해 쓸 수 있으며 문장은 마침표로 끝나고, 앞이나 뒤에 빈 줄을 두지 않는다.

## 객체 가져오기

함수를 쓰는 요점은 재사용한다는것이다. 이는 파이썬에서 네임스페이스에 필요한 함수를 import한다는 것이다. 이를 하는 많은 방법들이 있지만, 주로 두 가지 방법이 사용된다.

- import module_name
- from module_name import function_name

import module_name은 module_name을 찾고 지역 네임스페이스의 import문이 실행된 곳에 이름을 정의한다.

from module_name import identifier은 조금 복잡하지만 기본적으로는 같은 동작을 한다.

두 가진 형태는 가져온 객체의 이름을 as 문을 통해 바꿀 수 있다.

```python
from my_module import myfunc as better_named_func
```

이는 상대경로도 됨 ^^