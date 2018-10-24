# RNN(Recurrent Neural Network)

- RNN은 히든 노드가 방향을 가진 엣지로 연결돼 순환구조를 이루는(directed cycle) 인공신경망이다.
- 반복적인 데이터, 순차적인 데이터를 학습하는데 특화되어있다.
  - 음성인식
  - 단어 의미 판단, 대화 등..(자연어 처리)
  - 영상, 소리 분류

- RNN의 구조는 아래와 같다.

![RNN_구조](RNN_사진\RNN_구조.jpg)

- 여기에서 W는 상태에서 상태로 선형 변환을 정의한다.
- U는 입력에서 상태로의 선형 변환이다.
- 출력 O는 시퀀스의 다음 단어의 확률 벡터 (O1 ... Ot ...)의 시퀀스이다.

> $$ S_t= f(S_{t-1}, X_t) $$

- 현재의 아웃풋을 전달받아 갱신되는 구조이다.
- 스테이트의 활성함수는 비선형 함수인 `하이퍼볼릭탄젠트(tanh)`, ReLU, logit 함수로 활성함수로 사용할 수 있다.
- 따라서 RNN에서 각 상태는 되풀이되어 `이전의 모든 계산에 종속된다.`

![RNN_기본구조](RNN_사진\RNN_기본구조.png)

- RNN은 고정 크기의 입력을 처리하는 데에만 국한되지 않는다. 따라서 다양한 길이의 시퀀스나 다양한 크기의 이미지와 같이 신경망을 사용하여 계산 가능한 것을 처리할 수 있다.

- 아래는 만들 수 있는 모든 경우의 시퀀스의 조합에 대한 그림이다.

![RNN_상태매칭](RNN_사진\RNN_상태.png)

- `일대일` : 피드 포워드 신경망 및 길쌈 네트워와 같이 비순차적 처리
- `일대다` : 단일 입력을 기반으로 시퀀스 생성(예 : 이미지의 캡션 생성)
- `다대일` : 시퀸스를 기반으로 한 단일 결과가 출력(예 : 텍스트의 감정 분류)
- `다대다(간접)` : 시퀸스는 하나의 상태 백터로 인코딩 된고 그 후 상태 백터가 새 시퀀스로 디코딩 된다.  (예 : 다른 언어로번역)
- `다대다(직접)` : 각 입력의 단계에 대한 결과가 출력된다. (예 : 음성 인식의 프레임 음소 레이블링)

## RNN의 수행 및 훈련 과정

한 시퀸스에 얼만큼의 1이 있는지 계산하는 예제를 보자. 이 문제에서는 1의 수를 세는 방법과 시퀸스가 끝날 때 결과를 출력하는 법을 알려준다. 아래와 같은 입력이면 결과가 3이 나와야 할 것이다.

``` text
In: (0, 0, 0, 0, 1, 0, 1, 0, 1, 0)
Out: 3
```

네트워크는 아래와 같이 구성된다.

![예제 네트워크](RNN_사진\RNN_예제.png)

이 네트워크에는 `입력 가중치 U` 와 `반복 가중치 W` 의 두 가지 매개 변수만 있다.
> $$ S_t= S_{t-1}*W+X_t*U $$

위는 비선형 함수를 적용하지 않기 때문에 선형 모델이다. 따라서 아래와 같이 코드를 만들 수 있다.

```python
def step(s, x, U, W):
    return x * U + s * W
```

- U=1로 설정하면 입력이 수신 될 때마다 전값을 그대로 얻는다.
- W=1로 설정하면 누적 될 값은 감소하지 않는다.

## 시간 경과에 따른 역전파

- 순전파 : 입력층을 시작으로 출력층까지 결과 값이 출력되는 과정
- `역전파` : 결과 값을 통해 다시 역으로 input 방항으로 오차를 다시 보내며 가중치를 재업데이트 하는 것

![순전파 역전파](RNN_사진\순전파_역전파.png)

- 초록: 순전파, 빨강: 역전파

순전파는 시퀸스를 따라 RNN의 래핑을 해제하고 각 단계에 대한 일련의 활동을 구축한다. 일련의 입력 시퀸스 X가 있는 진행 단계는 다음과 같이 구현 가능하다.

```python
def forward(X, U, W):
# Initialize the state activation for each sample along the sequence
    S = np.zeros((number_of_samples, sequence_length+1))
    # Update the states over the sequence
    for t in range(0, sequence_length):
    S[:,t+1] = step(S[:,t], X[:,t], U, W) # step function
    return S
```

> [:, n] 이 뭘까?  
이는 만약 arr[3][3]의 배열이 있는 경우 arr[:,1] = 3 이면  
> ```text
> [[0, 0, 0],         [[0, 0, 0],  
> [0, 0, 0],  에서     [3, 3, 3],  
> [0, 0, 0]]           [0, 0, 0]]  
> ```  
> 즉 `arr[행, 열] = 값` 으로 해당 행, 열 의 원소를 값으로 치환

위 python 코드의 결과로 배치의 각 단계 및 각 샘플에 대해 S로 표시되는 결과 활성화가 나타난다. S는 계속 커지기 때문에 다음과 같이 평균 제곱 오차 비용 함수를 사용하여 목표 및 출력 y에 대한 출력 비용을 정의한다.

```python
cost = np.sum((targets – y)**2)
```

![예제 네트워크](RNN_사진\RNN_예제.png)

앞의 단계와 코스트 함수를 통하여 함수의 기울기가 어떻게 전달되는지 정의할 수 있다.  
먼저 비용함수(∂ξ / ∂y)에 대한 출력 즉, y의 기울기를 구해야한다.


![y기울기](RNN_사진\y_기울기.png)

매개 변수의 기울기는 다음과 같이 누적된다.

![기울기_누적](RNN_사진\매개변수_기울기_누적.png)

U 및 W의 기울기는 gU, gW에 대한 축적되는 것을 아래의 코드로 표현할 수 있다.

```python
def backward(X, S, targets, W):
    # 결과의 기울기 계산
    y = S[:,-1] # Output `y` is last activation of sequence
    # Gradient w.r.t. cost function at final state
    gS = 2.0 * (y - targets)
    # gradients backwards를 축적
    gU, gW = 0, 0 # gradient accumulations 0으로 초기화
    for k in range(sequence_len, 0, -1):
    # Compute the parameter gradients and accumulate the
    results.
    gU += np.sum(gS * X[:,k-1])
    gW += np.sum(gS * S[:,k-1])
    # Compute the gradient at the output of the previous layer
    gS = gS * W
    return gU, gW
```

그라디언트 디센트를 사용하여 Network 최적화

```python
learning_rate = 0.0005
# Set initial parameters
parameters = (-2, 0) # (U, W)
# Perform iterative gradient descent
for i in range(number_iterations):
    # Perform forward and backward pass to get the gradients
    S = forward(X, parameters(0), parameters(1))
    gradients = backward(X, S, targets, parameters(1))
    # Update each parameter `p` by p = p - (gradient * learning_rate).
    # `gp` is the gradient of parameter `p`
    parameters = ((p - gp * learning_rate)
        for p, gp in zip(parameters, gradients))
```

그러나 이 코드를 실행하려고 하면 최종 매개 변수 U, W가 숫자가 아닌 NaN으로 끝나는 경향이 있다. 이것을 그래디언트 값이 폭발한다고 한다.

![순전파 역전파](RNN_사진\코스트_경사도.png)

## 그래디언트 값의 폭발 또는 사라짐

RNN은 반복적 특성으로 인해 모든 상태 업데이트를 계산하는데 어려움이 발생한다.
그래디언트 값이 폭발하는 것 외에도 사라지는 경우가 있다. 이 둘이 발생하는 이유는 그라디언트를 역방향으로 전파하는 반복 관계가 기하학적 순서를 형성하기 때문이다.

![그래디언트_폭발](RNN_사진\그래디언트_폭발.png)

단순 선형 RNN에서 |W|>1 이면 그래디언트가 폭발한다. 따라서 `|W|<1` 로 만들어야한다.
이외에도 그래디언트의 폭발을 관여하는 것은 W의 최대 고유치 `ρ(스펙트럼 반경)` 와도 관련이 있다.
