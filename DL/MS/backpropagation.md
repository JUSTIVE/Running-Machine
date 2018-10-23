# 역전파 알고리즘

우리는 어떻게 뉴럴 네트워크가 입력값을 고정된 가중치에 의해 결정적인 출력값에 사상하는지를 보았다. 뉴럴 네트워크의 구조(피드-포워드, 히든레이어의 수, 레이어당 뉴런의 수)가 정의되고, 각 뉴런의 활성화 함수가 선택된 이상, 우리는 이러한 네트워크 상의 각각의 뉴런의 상태를 결정할 가중치들을 설정할 필요가 있다. 우리는 1 레이어- 네트워크에서 어떻게 동작하는 지 보고, 이를 깊은 전방향 네트워크에 어떻게 확장할 지를 확인할 것이다. 딥 뉴럴 네트워크에서 가중치를 설정하는 알고리즘의 이름은 역전파 알고리즘이라 불리며, 우리는 이것에 대해 논하고, 이 알고리즘에 대해 설명할 것이다. 우선, 단일 레이어 - 네트워크에서 확인해보자.

우리가 이해해야할 일반적인 개념은 다음과 같다: 모든 뉴럴 네트워크는 어떤 함수에의 근사이며, 이에 각 뉴럴네트워크는 요구하는 함수와 같지 않은 대신, 몇몇 값들이 다를 것이다. 이러한 값들은 오차 **error** 라 불리며, 우리의 목표는 이 오차값을 줄이는 것이다. 오차가 뉴럴 네트워크의 가중치의 함수이기 때문에, 우리는 가중치를 이용하여 오차를 줄일 것이다. 오차 함수는 많은 가중치들의 함수이다. 이는 많은 변수를 포함한 함수이다. 수학적으로, 이 함수가 0을 가지는 값의 집합은 초평면을 정의하며, 이 평면상의 최소점들을 찾고 곡선을 따라 최소지점으로 가야 합니다.

## 선형 회귀

우리는 이미 첫 장에서 선형 회귀에 대해 소개했으나, 우리는 이제 많은 변수를 다루고 있기 때문에, 행렬 표기를 통해 간단하게 나타낼 것이다. `x`를 입력이라 하자. 우리는 `x`를 하나의 벡터라 생각할 수 있다. 선형 회귀의 경우, 우리는 단일 출력 뉴런 `y`를 고려할 것이다. 가중치의 집합 `w`는 `x` 와 같은 크기의 벡터 차원을 가지는 벡터일 것이다. 활성 값은 내부 산물인 `<x,w>`로 정의된다.

우리가 각각의 입력 `x`에 대해 우리는 목표값 `t`를 가지길 원한다. 각각의 입력 `x`에 대해서 뉴럴 네트워크는 정의된 활성 함수에 의해 `y`의 출력값을 가질 것이나, 이 경우 (y-t)의 절댓값은 입력값 `x`에 대해서 우리의 예측 값과 실제 값의 차이를 나타낸다. 만약 m개의 입력값 ${x_i}$들에 대해, 각가의 입력값은 목표값 $t_i$를 가질 것이다. 이 경우에, 우리는 오차를 평균제곱오차 $\sum_i(y^i-t^i)^2$를 통해 구할 것이다. 이때의 $y^2$는 `w`의 함수 값이다. 이 `w`에 대한 함수의 오류는 보통 `J(w)`로 나타내어진다. 우리가 앞에서 언급했듯이, 이는 `w`와 같은 차원의 초공간을 나타내고, 각각의 $w_j$에 대해 우리는 평면상의 최저점을 향하는 곡선을 찾아야 한다. 이 곡선이 방향은 다음과 같이구할 수 있다.

> !["$\overrightarrow{d}\frac{\partial\sum_i(y^i-t^i)^2}{\partial w_j}$"](https://latex.codecogs.com/svg.latex?\overrightarrow{d}&space;=&space;\frac{\partial&space;\sum_i(y^i-t^i)^2}{\partial&space;w_j})

최소값을 향하기 위해서는 우리는 각각의 $w_j$에 대해 $\overrightarrow{d}$ 방향으로 움직여야 한다. 다음을 계산해보자.

>!["$\overrightarrow{d}=\frac{\partial\sum_i(y^i-t^i)^2}{\partial w_j}=\sum_i=\frac{\partial(y^i-t^i)^2}{\partial w_j}=2*\sum_i=\frac{\partial y^i}{\partial w_j}(y^i-t^i)$"](https://latex.codecogs.com/png.latex?\overrightarrow{d}=\frac{\partial\sum_i(y^i-t^i)^2}{\partial&space;w_j}=\sum_i=\frac{\partial(y^i-t^i)^2}{\partial&space;w_j}=2*\sum_i=\frac{\partial&space;y^i}{\partial&space;w_j}(y^i-t^i))

만약 $y^i=<x^i,w>$ 이고 $\frac{\partial y^i}{\partial w_j}=x^i_j$ 이면
$\overrightarrow{d}=\frac{\partial\sum_i(y^i-t^i)^2}{\partial w_j}=2*\sum_i x^i_j(y^i-t^i)$
>!["$\overrightarrow{d}=\frac{\partial\sum_i(y^i-t^i)^2}{\partial w_j}=2*\sum_i x^i_j(y^i-t^i)$"](https://latex.codecogs.com/png.latex?\overrightarrow{d}=\frac{\partial\sum_i(y^i-t^i)^2}{\partial&space;w_j}=2*\sum_i&space;x^i_j(y^i-t^i))

이다.

최소값으로 이동하기 위해서는 우리는 각각의 가중치들의 방향을 그들의 미분값의 방향으로 학습률 `l`만큼 움직여야 한다. 일반적으로 이 학습률은 1보다 작은 값을 가진다. 일반적으로 우리는 이 업데이트 규칙을 다음의 행렬 형태로 나타낼 수 있다.
>!["$w\rightarrow w\lambda\nabla(\sum_i(y^i-t^i)^2)=w-\lambda\nabla(J(w))$"](https://latex.codecogs.com/png.latex?w\rightarrow&space;w\lambda\nabla(\sum_i(y^i-t^i)^2)=w-\lambda\nabla(J(w)))

여기서 $\nabla$는 `nabla`라 불리며 편미분들의 벡터를 의미한다. 이 과정은 `경사하강`(`gradient descent`)라 불린다.

> $\nabla=(\frac{\partial}{\partial w_1},...,\frac{\partial}{\partial w_n})$

## 로지스틱 회귀

로지스틱 회귀에서 출력값은 연속적이지 않다. 대신 이는 클래스들의 집합으로 정의된다. 이 경우, 활성 함수는 이전과 다르게 판별하는 함수가 되지 않을 것이고, 대신 우리는 `시그모이드`(`sigmoid`)함수가 될 것이다. 로지스틱 시그모이드 함수는 우리가 전에 보듯이 (0,1)에서의 실수값을 출력하며, 따라서 이는 확률함수로 표현될 수 있다. 그리고 이것은 2-클래스 분류 문제에서 정확하게 작동할 수 있는 이유이다. 이 경우, 대상은 두 클래스 중 하나가 될 수 있으며, 결과물은 두 클래스가 될 확률을 의미한다.
> 여기서의 t 는 타겟이며, 이 경우에는, 두 개의 값을 가진다. 이 두 값은 class0과 class1으로 정의될 수 있다. 이 0과 1의 값을 로지스틱 시그보이드 함수의 값과 혼동하지 마라.

만약 $a$ 가 앞에서 정의된 뉴런 활성값이라면, $s(a)$를 로지스틱 시그모이드 함수라 정의하자. 따라서, 모든 예제 $x$에 대해 주어진 가중치 $w$에 의한 class로의 확률 $y$은 다음과 같다.

> !["$P(t|x,w) = \begin{cases}   \sigma(sigma) &\text{if }t=1 \\    1-\sigma(a) &\text{if} t=0 \end{cases}$"](https://latex.codecogs.com/png.latex?P(t|x,w)&space;=&space;\begin{cases}&space;\sigma(sigma)&space;&\text{if&space;}t=1&space;\\&space;1-\sigma(a)&space;&\text{if}&space;t=0&space;\end{cases})

위의 식을 다음과 같이 더 간결하게 작성할 수 있다.

> $P(t|x,w)=\sigma(a)^t(l-\sigma(a))^{l-t}$