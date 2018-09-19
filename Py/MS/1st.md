# Introduction and First Steps-Take a Deep Breath

코딩은 컴퓨터에게 컴퓨터가 이해할 수 있는 언어로 무언가를 하도록 말하는 것.

컴퓨터는 매우 강력한 도구이나 스스로 생각할 수 없기에 모든것을 설명해야 한다.
우리는 코드를 다양한 스타일과 언어로 작성할 수 있다. 
이것은 어렵기도 하고, 쉽기도 하다. 언어와 마찬가지로, 누구나 쓰는 법을 배우는 건 쉽지만, 시를 쓰는 것처럼 혼자 배우기는 쉽지 않다.

좋은 코드란
- 짧다
- 빠르다
- 아름답다
- 읽고 이해하기 쉽다
- 간단하다
- 수정하고 확장하기 쉽다
- 리팩토링하기 쉽다
- 테스트하기 쉽다

## 적절한 소개

우리가 코드를 작성할 때, 우리는 컴퓨터에게 어떤 것들이 어떻게 되어야 할지 지시한다. 이러한 동작들은 여러 곳에서 일어난다.

- 메모리
- 하드 드라이브
- 네트워크 케이블
- CPU
- 등등

모든 물체는 `properties:속성` 과 `method:메소드`라는 두 가지 주요한 특징을 가지고 있다. 
- `properties:속성`은 객체의 특성을 가리키는 것이다.
- `method:메소드`는 객체가 할수 있는 것들을 의미한다.

여기서 알아야 할 것은, Python에 있는 모든 객체는 `ID`와 `type:타입`, 그리고 `value:값`을 가진다는 것이다.
- 한번 생성된 객체의 id는 변하지 않는다. 
- 타입도 절대 변하지 않는다.
- 값은 바뀔 수도 있고, 아닐 수도 있다. 바뀌는 경우에는 `mutable`이라 불리고, 바뀌지 않는 경우에는 `immutable`이라 불린다.

우리는 객체를 이용할 때, 각각의 객체의 이름을 통해 사용한다. 

## Python으로 들어가며

파이썬은 네덜란드 컴퓨터 과학자 귀도 반 로썸이 1989년 크리스마스에 세상에 내린 선물이다.

## Python에 대해

파이썬은 다음의 특징을 가진다.

### 이식성
파이썬은 리눅스, 맥, 윈도우에서 돌아간다. 단, 설정과 경로를 좀 수정해야 할 것.

### 일관성
파이썬은 극도로 논리적이고 일관적이다.

### 개발자 생산성
Mark Lutz에 의하면 파이썬은 Java나 C++ 코드에 비해 $\frac{1}{5}$ 내지 $\frac{1}{3}$정도의 크기를 가진다고 한다. 이것은 작업을 더 빨리 할 수 있다는 것이다. 적은 코드는 
- 시장에 더 빨리 반응할 수 있다
- 적은 코드만 써도 된다
- 적은 코드만 읽어야 한다
- 적은 코드만 유지하고, 디버그하고, 리팩토링해야한다.

파이썬의 다른 중요한 장점은 파이썬은 컴파일과 링킹 단계가 필요 없이 동작한다는 것이다.

### 광범위한 라이브러리
파이썬은 놀라울 정도로 광범위한 기본 라이브러리를 가지고 있다. 뿐만 아니라, 서드 파티 라이브러리를 `Python Package Index:PyPI`에서 받을 수 있다.

### 소프트웨어 품질
파이썬은 가독성, 일관성, 그리고 품질에 매우 집중되어있다. 파이썬의 중요한 특징 중 하나는 본질적으로 `다중 패러다임`이라는 것이다. 파이썬을 스크립트 언어로 사용할 수 도 있고, 명시적 객체지향으로 쓸 수도 있으며, 함수형으로도 쓸 수 있다.

### 소프트웨어 통합
파이썬은 다른 많은 언어와 확장되거나 통합되어질 수 있다. 

## 단점은 무엇인가?

아마, 파이썬에서 찾을 수 있는 유일한 단점은 실행 속도이다. 파이썬은 컴파일 된 언어보다 `느리다`. 파이썬에서 프로그램을 실행할 때 컴파일한 코드는 .pyc 확장자를 가지는 `바이트코드`라 불리며, `파이썬 인터프리터`에 의해 실행된다. 이러한 접근은 이식성을 높이나 기계어 레벨로 컴파일된 다른 언어들에 비해 느리다.

하지만, 최근에는 차선의 특성들에 의해 파이썬의 속도 문제는 보기 드물다. 실제로, 하드웨어의 비용은 더 이상의 문제가 아니며, 대부분은 병렬화를 통해 속도를 얻기 쉽다.  
숫자 계산에 대해서는 고급 컴파일 기술로 평균 7배의 성능을 내는 `PyPy`와 같은 컴파일러를 이용할 수 있다.  
데이터 과학의 경우에는 `Pandas`나 `Numpy`와 같은 네이티브로 구현된 라이브러리를 찾게 될 것이다.

## 누가 파이썬을 쓰는가?

뭐 유명한 우리가 아는 대부분의 기업이 쓴다.
파이썬은 다양한 곳에서 쓰인다.
- 시스템 프로그래밍
- 웹 프로그래밍
- GUI 어플리케이션
- 게임
- 로보틱스
- 빠른 프로토타이핑
- 시스템 통합
- 데이터 과학
- 데이터베이스 어플리케이션
- 등등

## 파이썬 프로그램을 실행하는 법

### 파이썬 스크립트를 실행하기
파이썬은 스크립트 언어로 실행되어질 수 있다. 스크립트는 태스크처럼 주로 보통 실행하는 작은 파일이다.

### 파이썬 대화 쉘을 실행하기
파이썬을 실행하는 다른 방법은 대화형 쉘을 이용하는 것이다. 콘솔을 열고 가상환경을 활성화 한 후에, python을 친다. 

다른 방법으로는, `IDLE:Integrated Development Environment`를 사용하는 것이 있다. 

### 파이썬을 서비스로 실행하기
스크립트나 쉘에서 파이썬을 실행하는 것 말고, 파이썬은 적절한 소프트웨어로 쓰여지고 동작할 수 있다. 뒤에 나온다

### 파이썬을 GUI 프로그램으로 실행하기
파이썬은 GUI로 실행될 수 있다. 이와 관련된 몇몇 프레임워크가 있으나, 몇몇은 플랫폼 종속적이고, 몇몇은 크로스 플랫폼이다. 이 책에서는 Tkinter를 이용한다.

## 어떻게 파이썬 코드가 구성되는가

파이썬 코드는 모듈이라 불리는, .py 확장자를 가진 파일로 구성된다. 그러나 몇 백 라인이 채 되지 않는 스크립트가 아니고서는 여러 모듈을 이용해야 한다. 그래서 파이썬은 `package`라는 모듈을 묶을 수 있는 구조를 제공한다. `package`는 `__init__.py`라는 코드가 필요 없는 파일을 포함한 폴더이다(Python 3.3부터는 `__init__.py`는 더 이상 필수 조건이 아니다).

### 모듈과 패키지를 어떻게 써야 하는가?
개발자가 어플리케이션을 만들 때, 다른 구역에 같은 조각들을 끼워맞추는 것과 유사할것이다.
코드를 복붙하는 것은 매우 안좋은 습관이다. 이것은 `DRY:Don't Repeat Yourself` 원칙을 위배한다. 코드를 복붙하는 것이 나쁜 이유는 다음과 같다.
- 로직에 버그가 있을 경우, 그 로직이 적용된 모든 곳을 고쳐야 한다.
- 유효성 검사를 마친 후, 코드를 수정할 때 적용된 모든 곳을 바꿔야 한다.
- 코드가 쓰인 곳을 찾다 한두개를 빼먹을 수도 있다.
- 코드가 좋지 않은 이유로 더 이상 쓰이지 않을 수도 있다.

파이썬에서 `함수:function`를 이용하면 같은 코드를 반복할 수 있다.
라이브러리란 언어의 능력을 향상시켜주는 기능들을 제공하는 함수들과 객체들의 집합이다.

## 파이썬 실행 모델

### Name 과 namespaces
구획이 나뉘어지지 않은 채 원하는 라이브러리/모듈을 찾는 것은 매우 힘들것이다. 파이썬 `Name`은 다른 언어에서 변수라 불리는 것에 가장 가까운 추상화다. 이름은 주로 객체를 참조하며 이름 바인딩 연산자로 소개된다.
```python
>>> n=3 # integer number
>>> address = "221b Baker Street, NW1 6XE, London" # S.Holmes
>>> employee = {
    'age':45,
    'role':'CTO',
    'SSN':'AB1234567'
}
>>> #let's print them
>>> n
3
>>> address
'221b Baker Street, NW1 6XE, London'
>>> emplolyee
{'role':'CTO','SSN':'AB1234567','age':45}
```
위의 예제에서의 *n*,*address*,*employee* 와 같은 것들을 `name`이라 부른다. 이것들은 어딘가에 보관되어져야 하며, 이러한 객체를 가져와야 할 경우 이름을 통해 가져올 수 있다. 이 때, 이름들을 붙잡을 공간을 `namespace`라 한다.

`namespace`란, 이름에서 객체로 사상하는 것이다. 예로는, 파이썬에 내장 이름들이 있고, 모듈 내의 전역 이름이 있고, 함수 내의 지역 이름이 있다. 객체의 속성들의 묶음도 `namespace`로 간주되어질 수 있다. 

`namespace`의 아름다움은 이름들을 겹치거나 간섭 없이 깔끔하게 정리하는 데에 있다. 예를 들어, 도서관에서 import할 책을 가져온다고 했을 때 다음과 같이 쓸 수 있다.
```python
from library.second_floor.section_x.row_trhee import book
```
우리는 *library*`namespace`에서 출발하여, `.`연산자를 통해 `namespace`공간들로 들어갔다.

### 스코프
파이썬의 문서에 따르면, *스코프는 네임 스페이스에 `직접 액세스` 할 수 있는 파이썬 프로그램의 텍스트 영역* 이라 되어있다. 직접 액세스 가능하다는 것은, 이름에 대한 부적절한 레퍼런스를 찾고 있을 때, 파이썬은 네임 스페이스에서 그 이름을 찾는다는 것이다.

스코프는 정적으로 결정되나, 실행 중에는 동적으로 사용되어진다.
파이썬에서 접근할 수 있는 4개의 다른 스코프가 있다.
- `지역`스코프: 가장 안쪽에 있고, 지역 이름을 포함한다.
- `인클로징`스코프: 비 지역 이름과 비 전역 이름을 포함한다.
- `전역`스코프: 전역 이름을 포함한다.
- `내장`스코프: 내장 이름을 포함한다.

파이썬이 이름을 찾는 순서는 `LEGB:local,enclosing,global,built-in`이다.
이에 대한 예시는 다음과 같다.
```python
scopes1.py
# local vs global
# we define a function, called local
def local():
    m = 7
    print(m)
m = 5
print(m)

# we call, or `execute` the function local
local()
```
결과는 각각 *5*와 *7*이 나왔을 것이다. 만약 *local*함수의 `m=7`라인이 없었다면 어떻게 되었을까? 파이썬은 local scope에서 못 찾은 후에, enclosing, 및 global scope를 확인할 것이다. 이에 대한 예제는 다음과 같다.
```python
scopes2.py
# Local versus Global
def local():
    # m doesn't belong to the scope defined by the local function
    # so Python will keep looking into the next enclosing scope.
    # m is finally found in the global scope
    print(m, 'printing from the local scope')

m = 5
print(m, 'printing from the global scope')
local()
```
위의 결과는 다음과 같을 것이다.
```cmd
5 printing from the global scope
5 printing from the local scope
```
다음은 enclosing scope에 대한 예제이다.
```python
scopes3.py
# local, enclosing and global
def enclosing_func():
    m=13
    def local():
        # m doesn't belong to the scope defined by the local function
        # so Python will keep looking into the next enclosing scope.
        # m is finally found in the global scope
        print(m, 'printing from the local scope')
    # calling the function local
    local()
m=5
print(m, 'printing from the global scope')

enclosing_func()
```
위의 결과는 다음과 같을 것이다.
```cmd
5 printing from the global scope
13 printing from the local scope
```

### 객체와 클래스
`객체`는, `클래스`의 인스턴스이다. 파이썬의 아름다움은 클래스가 객체라는 것인데, 이것은 `metaclass`라는 심화적인 개념으로 이어진다.
다음은 객체와 클래스의 예제이다.
```python
bike.py
# let's define the class Bike
class Bike:
    def __init__(self, colour, frame_material):
        self.colour = colour
        self.frame_material = frame_material

    def brake(self):
        print("Braking!")
# let's create a couple of instances
red_bike = Bike('Red', 'Carbon fiber')
blue_bike = Bike('Blue', 'Steel')

# let's inspect the objects we have, instances of the Bike class.
print(red_bike.colour) # prints: Red
print(red_bike.frame_material) # prints: Carbon fiber
print(blue_bike.colour) # prints: Blue
print(blue_bike.frame_material) # prints: Steel
# let's brake!
red_bike.brake() # prints: Braking!
```
여기에서 첫 메소드인 `__init__`은 생성자이다.

## 좋은 코드를 쓰는 가이드라인

`PEP8:Python Enhancement Proposal`을 보라. 
