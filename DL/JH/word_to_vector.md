# Word To Vector

## 언어 모델링

언어 모델링의 목표는 대개 단어 확률을 계산하는 것이다.
특히 음성 인식, 광학 문자 인식, 기계 번역 및 맞춤법 교정같은 프로그램에서 매우 중요하다.

따라서 좋은 언어 모델은 대화 어떤 구문이 가장 올바른지 구별할 수 있다.

## Word 기반 모델

### `N-grams`

N-gram은 문자열에서 `N개의 연속된 요소를 추출`하는 방법이다.  
N-gram은 문자 혹은 단어 단위를 선택하여 추출할 수 있다.  
각 시퀀스의 확률에 대한 추론(w1, ... wm)은 일반적으로 실행 못한다.
  > 시퀀스: 수열, 연속, 순서, 여기에서는 특정 단어의 열

P(w1, ..., wm)의 결합 확률을 계산하려면 다음과 같은 `체인 규칙`을 적용하면된다.

$$P(w_1 ... , w_m) = P(w_1)*P(w_2|w_1)*P(w_3|w_2,w_1)* ... *P(w_m|w_1, ... , w_{m-1})$$

특정 초기 단어가 부여된 이후 단어의 확률은 데이터로부터 추정하기가 어렵다. n-gram은 순차적 단어가 같을 확률만 모델링한다.
n-gram은 길이가 n인 다른 문자를 나타내기 위해 사용될 수 있다.

이 공동 분포에 대한 추론은 여러 개별 부품에서 합동 분포를 분할하는 N-gram 모델을 통해 근사적으로 추정할 수 있다.

예를 들어 "The quick brown fox"라는 단어에서  
아래는 단어 단위 n-gram 이다.

- 1-gram: "The," "quick," "brown," and "fox" (also known as unigram)
- 2-grams: "The quick," "quick brown," and "brown fox" (also known as bigram)
- 3-grams: "The quick brown" and "quick brown fox" (also known as trigram)
- 4-grams: "The quick brown fox"

방대한 양의 텍스트가 있는 경우, 특정 n개(일반적으로 2~4)까지  
모든 n개 그래프를 찾아 해당 문자열에서 각 n 그램의 발생을 카운트할 수 있다.  
이전 n-1 단어에서 각 n-그램의 마지막 단어의 확률을 추정할 수 있다.

- ![n-gram](word_to_vector_pic\n-gram.png)

i번째 단어가 이전 n-1 단어에만 의존한다는 독립성 가정은 공동 분포의 근사치에 사용할 수 있다.
예르 들어, 유니그램의 경우 다음과 같은 방법으로 결합 분포를 추정할 수 있다.

$$P(w_1 ... , w_m) = P(w_1)*P(w_2)*P(w_3)* ... *P(w_m)$$

3-gram의 경우

$$P(w_1 ... , w_m) = P(w_1)*P(w_2|w_1)*P(w_3|w_2,w_1)* ... *P(w_m|w_{m-2},w_{m-1})$$

따라서, 어휘 크기에 기반해 n-gram의 수가 n과 함께 기하 급수적으로 증가 함을 알 수 있다.  (이를 이를 `차원의 저주`이라고 한다.)

예를 들어 100 단어가 포함된 경우 5-gram의 수는 $100^5 = 10,000,000,000$이다.  
따라서 모든 확률을 저장하기 위해서는 매우 큰 저장 장치가 필요하며 n의 큰 값에 대한 n-그램 확률 추정치를 만들기 위하여 매우 큰 텍스트 덩어리가 필요하다.

조합당 최소 하나의 예(n-graph modeling의 경우)가 필요할 때 발생한다.
n이 클수록 원래 분포에 대한 근사치 및 n-gram 확률에 대한 더 많은 데이터가 필요하다.

## Nerual language models

n-gram의 차원의 저주를 극복하는 방법은 단어의 더 낮은 차원의 분산 표현을 학습하는 것이다.

![낮은 차원 분산](word_to_vector_pic\under_dimension.png)
> 어휘에서 V-단어는 V크기의 핫 인코딩 벡터로 변환된다.(각 단어는 유니크하게 인코딩된다.)  
그런 다음 임베딩 함수는 V 차원 공간을 크기 D(위에서는 D=4)의 분산 표현으로 변환합니다.

이 방법 핵심은 `학습된 임베딩 함수가 단어에 대한 의미 정보를 학습`하는 것이다.  
이는 어휘의 각 단어를 연속적인 가치를 지닌 벡터 표현인 단어 임베딩과 연결시킨다.

각 단어는 단어의 문법적 또는 의미론적 속성에 다른 차원이 해당되는 이 단어의 포함 영역에 해당된다.  
`목표는 이 임베딩 영역에서 서로 가깝게 단어가 유사한 의미를 갖도록 하는 것`이다.  이 방법으로 일부 단어가 의미론적으로 유사한 정보가 언어 모델에 의해 악용될 수 있다.  

예를 들어 "여우", "고양이"가 의미 상으로 관련되어 있고 "재빠른 갈색 여우"와 "재빠른 갈색 고양이"가 유효한 구문이라는 것을 알 수 있다.
이후 일련의 단어를  단어의 특성을 포착하는 일련의 벡터로 변환할 수 있다.

신경망을 통해 언어 모델을 모델링하고 묵시적으로 내장 함수를 학습하는 것이 가능하다. 만약 n-1 단어들의 순서를 주어진 신경 네트워크를 배우는 것이다. 이때 $w_{t-n+1}, ..., w_{t-1}$ 는 다음 단어의 확률 분포, 즉 wt를 출력하고 한다.

임베딩 계층은 단어 $w_i$를 한 번 열렬하게 표현한 다음 임베딩 행렬 C와 곱하여 그 임베딩으로 변환한다. 이 계산은 테이블 조회로 효율적으로 구현할 수 있다.

`임베딩 행렬 C는 모든 단어에 걸쳐 공유`되므로 모든 단어는 동일한 임베딩 함수를 사용한다. C는 `V*D 행렬`로 표현된다. 여기서 V는 어휘의 크기, D는 임베딩 크기이다. `임베딩의 결과는 히든 레이어로 연결`된다. 그 후 바이어스 b와 tanh와 같은 비선형 함수가 적용될 수 있다. 히든 레이어의 출력은 $z=tanh(concat(w_{t-n+1}, ..., w_{t-1}))$ 함수로 표현된다.

히든 레이어에서 `히든 레이어와 U`를 곱하여 다음 단어 $w_t$의 확률 분포를 출력할 수 있다. 이렇게 하면 히든 레이어에 단어 공간에 매핑하고 바이어스 b를 추가하고 softmax 함수를 적용하여 확률 분포를 얻는다. 최종 계층은 `softmax(z*U + b)`를 계산한다.

> softmax: 벡터 요소의 값을 다 합쳤을 때 1이 되도록 벡터 요소를 변환하는 것  
예) Ve{ctor3 (1,2,3) 에 softmax는  
$(\frac {1^2} {1^2+2^2+3^2}, \frac {2^2} {1^2+2^2+3^2}, \frac {3^2} {1^2+2^2+3^2})$

이 네트워크는 아래 그림과 같다.

![임베딩 네트워크](word_to_vector_pic\embedding_net.png)

이 모델은 어휘의 `모든 단어의 임베딩과 단어의 연속에 대한 확률 함수의 모델을 동시에 습득`한다.  
이러한 분산 표현 덕분에 훈련 중 보이지 않는 일련의 단어로 이 확률 함수를 일반화할 수 있다.  
테스트 세트의 특정 단어 조합은 트레이닝 세트에는 보이지 않을 수 있으나 유사한 내장 기능을 가진 시퀀스는 트레이닝 중에 더 많이 표시될 수 있다.

아래는 일부 단어 포함에 대한 2D 투영을 보여준다.  

![2D 투영](word_to_vector_pic\2D_word_relation.png)  

여기에서 의미적으로 가까운 단어가 임베딩 공간에서 서로 가까운 것을 볼 수 있다.

단어 임베딩은 대규모 텍스트 데이터에 대해 비감독식 훈련이 될 수 있다.
이 방법으로 단어 사이에 일반적인 의미 정보를 포착할 수 있다.
그 결과로 `임베딩은 아직 분류가 안된 데이터들의 다른 작업의 성능을 향상` 시킬 수 있다.  
예를 들어 뉴스 기사에 내용을 분류하는 분류자는 one-hot 인코딩 벡터 대신에 이전에 습득한 단어 삽입을 사용하여 훈련될 수 있다.  

이러한 장점 덕분에 많은 연구가 단어의 연속에 대한 확률 함수를 학습하는 것에 초점을 두지 않고 더 나은 단어 임베딩을 만드는 것이 탄생하였다.

놀랍게도 단어 임베딩은 단어들 간 유추를 차이로 포착 할 수 있다.
예를 들어 "여성"과 "남성"의 임베딩 차이가 성을 인코딩하고 이 차이는 "여왕", "왕"과 같은 다른 성 관련 단어에서 동일하게 분류할 수 있다.

![단어 임베딩](word_to_vector_pic\word_embedding.png)

단어 임베딩 모델은 큰 어휘 입력을 모델링할 때 생기는 차원의 저주를 극복할 수 있으나 여전히 고정 길이의
단어 시퀀스만 모델링 하는 것으로 제한된다.

이 문제를 해결하기 위해 RNN을 사용하여 `고정 길이 단어 시퀀스에 국한되지 않는`  `RNN 언어 모델`을 작성할 수 있다.

RNN 기반 모델은 입력 임베딩에서 유사한 단어를 클러스터링 할 수 있을뿐만 아니라 반복적인 상태 벡터에서 유사한 히스토리를 클러스터링 할 수 있다.

각 단어의 출력 확률 $P(w_i | context)$를  계산하는 것이다. 모든 단어 활성화에 대해 softmax를 사용하여 이러한 출력 확률을 얻는다.

5만 단어의 작은 어휘 V의 경우, $|S| * |V|$ 가 필요하다.
  > $|V|$ 는 어휘 크기이다.  
$|S|$ 는 상태 백터이다.  

이 행렬은 거대하고 어휘의 크기가 증기할 수록 더 폭발적으로 증가한다.
softmax는 다른 모든 활성화를 조합하여 단일 단어의 활성화를 정상화하므로 각 단일 단어의 확률을 위해 각 활성화를 계산해야한다.

`RNN, 임베딩 네트워크 둘 모두 큰 어휘에서 softmax를 계산을 것이 어렵다.` 왜냐하면 softmax 이전에 선형 변환을 모델링하기 위해 많은 매개 변수가 필요하고 이에 softmax 자체는 계산이 많이 필요하기 때문이다.

이러한 문제를 해결하기 위해 `soft 함수`를 `이진 트리`로 모델링하여 $log(|V|)$ 계산만을 하여 단일 단어의 최종 출력 확률을 계산할 수 있다.

## 문자 기반 모델

대부분의 경우, 언어 모델링은 단어 레벨에서 수행되며, 여기에서 분포는 고정된 |V| 단어의 어휘이다.
음성 인식에 사용되는 언어 모델과 같은 현실세계의 task의 어휘는 종종 10만 단어를 초과한다.
위와 같은 거대한 차원의 행렬의 출력 분포를 모델링하는 것은 매우 어렵다. 또한 이러한 단어 수준의 모델은 훈련 데이터의 일부가 아니거나 단어가 아닌 문자열을 포함하는 것에 상당히 제한적이다.

이러한 문제를 극복할 수 있는 모델은 `문자 수준 언어 모델`이라고 부른다.
이 모델은 단어 대신 `문자의 시퀀스(열)에 대한 분포를 모델링`하므로 훨씬 작은 어휘에 대한 확률을 계산할 수 있다.(여기서 어휘는 텍스트 코퍼스의 가능한 모든 문자들)
그러나 이 모델의 단점으로 단어가 아닌 문자 시퀀스를 모델링하려면 시간이 지남에 따라 동일한 정보를 캡처하기 위해 더 긴 쉬퀀스를 모델링해야한다. 따라서 이런 `장기 의존성`을 찾기 위해 LSTM RNN 언어 모델을 사용한다.

Tensorflow에서 문자 수준의 LSTM은 $P(c_t | c+{t-1} ... c_{t-n})$ 을 통해 다음 문자의 확률을 모델링한다.

전체 텍스트가 너무 길어 `BPTT (back-propagation through time)`가있는 네트워크를 학습 할 수 없으므로 `잘린 BPTT`라는 일괄 처리 변형을 사용한다.

이 방법에서는 트레이닝 데이터를 고정된 시퀀스 배치(묶음)의 길이로 나누고 배치별로 네트워크에서 일괄 적으로 트레이닝한다.
시퀸스 배치 뒤에는 다른 배치가 이어져 있으므로 배치의 마지막 상태는 다음 배치의 초기 상태로 사용할 수 있다. 이렇게 하면 전체 입력 텍스트를 통해 `역전파를 수행하지 않고도 상태에 저장된 정보를 이용`할 수 있다.

### 프리프로세싱(전처리)과 데이터 읽기

이제 레오 톨스토이의 "전쟁과 평화"라는 책을 텍스트 데이터로 예제로 설명을 할 것이다.

1. 사전 처리의 일환으로 라이센스, 서적 정보 및 목차를 제거하자.
2. 다음 문장의 중간에 줄 바꿈을 제거하고 최대 연속 줄 수를 2줄로 줄이자.
3. 데이터를 네트워크에 공급하려면 숫자 형식으로 변환해야한다.  
4. 각 문자는 정수와 연결된다. 아래의 예제에서는 텍스트 덩어리에서 총 98개의 다른 문자를 추출한다.  
5. 다음으로 입력과 목표를 추출한다. `각 입력 문자에 대해 다음 문자를 예측`한다.  
6. `생략된 BPTT`로 훈련하기 때문에 시퀀스의 연속성을 이용하기 위해 모든 배치를 서로 추적하게 할 것이다.

텍스트를 색인 목록으로 변환하고 입력과 표적의 배치로 분할하는 프로세스는 아래의 그림과 같다.

![톨스토이 예제](word_to_vector_pic\tolstoy.png)

### LSTM 네트워크

교육할 네트워크는 각 레이어에 512개의 셀이 있는 2계층 LSTM 네트워크이다.
잘린된 BPTT로 이 네트워크를 교육할 것이므로 `배치간에 상태를 저장`해야 한다.
먼저, 입력 및 대상에 대한 자리 표시자를 정의해야한다.
입력과 목표의 `첫번째 차원은 병렬로 처리되는 배치 사이즈`이다.
두번째 차원은 텍스트 시퀸스를 따르는 치수이다.
첫번째, 두번째 차원의 자리표시자는 문자가 인덱스로 표시되는 시퀀스의 배치를 묶는다.

```python
import tensorflow as tf

inputs = tf.placeholder(tf.int32, (batch_size, sequence_length))
targets = tf.placeholder(tf.int32, (batch_size, sequence_length))
```

문자를 네트워크에 공급하려면 문자를 벡터로 변환해야한다.
따라서 one-hot 인코딩으로 변환할 것이다. 따라서 각 문자는 데이터 세트의 다른 문자 수와 `동일한 길이의 벡터로 변형`된다. 이 벡터는 인덱스에 해당하는 셀을 제외하고 모두 0이다.

```python
one_hot_inputs = tf.one_hot(inputs, depth=number_of_characters)
```

다음으로, 다층 LSTM 아키텍처를 정의할 것이다. 먼저 각 레이어에 대해 LSTM 셀을 정의해야 한다.

```python
# lstm_sizes은 각 레이어 사이즈의 리스트
cell_list = (tf.nn.rnn_cell.LSTMCell(lstm_size) for lstm_size in lstm_sizes)
```

그런 다음 단일 다층 RNN 셀에 래핑을 한다.

```python
multi_cell_lstm = tf.nn.rnn_cell.MultiRNNCell(cell_list)
```

배치간의 상태를 저장하기 위해 `네트워크의 초기 상태를 가져와서 저장할 변수에 래핑`해야 한다.
계산상의 이유로 텐서플로는 LSTM 상태를 `두개의 탠서로 분리된 한 튜플을 저장`한다.
> `텐서`란 LSTM 세션으로 부터의 c와 h이다.  
> ![LSTM 구조](word_to_vector_pic\LSTM_structure.png)

이 중첩된 데이터 구조를 flatten 메소드로 전개하고, 각 텐서를 변수에 랩핑한 다음 pack_sequence_as 메소드로 원래 구조로 다시 패키징할 수 있다.

```python
initial_state = self.multi_cell_lstm.zero_state(batch_size, tf.float32)

# Convert to variables so that the state can be stored between batches
state_variables = tf.python.util.nest.pack_sequence_as(
  self.initial_state,
  (tf.Variable(var, trainable=False)
  for var in tf.python.util.nest.flatten(initial_state)) )
```

초기 상태를 변수로 정의했으므로 시간 경과에 따라 네트워크를 unrolling(풀기)을 할 수 있다.
텐서플로우는 입력의 시퀀스 길이에 따라 풀기를 동적으로 수행하는 `dynamic_rnn 메서드`를 제공한다.
이 메소드는 LSTM 출력을 나타내는 `텐서와 최종 상태로 구성된 튜플을 반환`한다.

```python
lstm_output, final_state = tf.nn.dynamic_rnn(
  cell=multi_cell_lstm, inputs=one_hot_inputs,
  initial_state=state_variable)
```

다음, `최종 상태를 다음 배치의 초기 상태로 저장`한다.
변수 assign 메소드를 사용하여 각각의 최종 상태를 올바른 초기 상태 변수에 저장한다.
control_dependencies 메서드는 LSTM 출력을 반환하기 전에 상태 업데이트가 실행되도록 강제하는 데 사용된다.

```python
store_states = (
  state_variable.assign(new_state)
  for (state_variable, new_state) in zip(
  tf.python.util.nest.flatten(self.state_variables),
  tf.python.util.nest.flatten(final_state)) )

# LSTM 출력 반환 전 상테 업데이트 강제
with tf.control_dependencies(store_states):
  lstm_output = tf.identity(lstm_output)
```

최종 LSTM 출력에서 logit 출력을 얻으려면 `(배치 사이즈) * (시퀀스 길이) * (심볼 수)` 를 행렬로 가질 수 있도록 선형 변환을 출력에 적용해야한다.
이 선형 변환을 적용하기 전 출력으로 나오는 행렬의 사이즈 숫자인 `(ouput) * (outputs 특징의 수)`형태로 평평하게 변환해야 한다.

```python
output_flat = tf.reshape(lstm_output, (-1, lstm_sizes(-1)))
```

그런 logits를 구하기 위해 다음 가중치 행렬 W과 바이어스 b를 이용하여 선형 변환을 수행후 softmax 함수를 적용하여 탠서의 사이즈인 `(배치 사이즈) * (시퀀스 길이) * (문자들의 개수 수)`로 변환할 수 있다.

```python
# 출력 레이어 정의
logit_weights = tf.Variable(
  tf.truncated_normal((lstm_sizes(-1), number_of_characters), stddev=0.01))
logit_bias = tf.Variable(tf.zeros((number_of_characters)))

# 마지막 레이어 변환 적용
logits_flat = tf.matmul(output_flat, self.logit_weights) + self.logit_bias
probabilities_flat = tf.nn.softmax(logits_flat)

# 원래 배치, 시퀸스의 길이로 변환
probabilities = tf.reshape( probabilities_flat, (batch_size, -1, number_of_characters))
```

> `tf.random.truncated_normal()` 함수:  
이 함수는 잘린 정규 분포에서 임의의 값을 출력한다.  
즉, 랜덤한 잘린 정상 값으로 채워진 특정 모양의 한 텐서를 반환한다.  
> [텐서플로 자료](https://www.tensorflow.org/api_docs/python/tf/random/truncated_normal)  

아래와 같은 LSTM 문자 언어 모델이 나오게된다.  

![LSTM 문자 언어](word_to_vector_pic\LSTM_character.png)

### 트레이닝

교육의 첫 번째 단계는 손실을 최소화하는 함수를 정의하는 것이다.
이 손실 함수는 입력과 대상을 고려하여 잘못된 일련의 문자를 출력하는 비용을 출력한다.
우리는 다음 문자를 전의 문자를 통해 예측하기 때문에 잘못된 일련의 문자를 출력할 수 있다. 이를 `분류 문제`라 하며 이에 cross-entropy 손실을 사용한다.

본문에서는 `sparse_softmax_cross_ entropy_with_logits()` 라는 TensorFlow 함수를 사용하여 작업을 수행할 것이다.
>

```python
sparse_softmax_cross_ entropy_with_logits(  
  _sentinel=None,  
  labels=None,  
  logits=None,  
  name=None
)
```

`네크워크의 logit 출력`을 입력(softmax 이전)으로 타겟을 `클래스의 라벨`로
그리고 각 출력에 대한 타켓의 cross-entropy 손실을 계산한다.

먼저 타겟(목표)를 1차원 벡터로 전개하여 네트워크를 평평한 logits 출력과 호환되도록 만든다.

```python
# 타겟을 평평한 logits와 호환되도록 목표를 평평하게 만든다.
targets_flat = tf.reshape(targets, (-1, ))

# 모든 출력에서 손실을 얻는다.
loss = tf.nn.sparse_softmax_cross_entropy_with_logits(
  logits_flat, targets_flat)

# 모든 출력에서 단일 값으로 손실을 감소시킨다.
loss = tf.reduce_mean(loss)
```

손실 함수가 정의되었으므로 입력 및 대상 배치 네트워크를 최적화할 텐서플로 트레이닝 작업을 정의할 수 있다.  
최적화를 실행하기 위해 `Adam-optimaizer` 프로그램을 사용한다. 이는 그래디언트 업데이트를 안전화하는데 도움을 준다.
> Adam-optimaizer:  
이것은 최적화 알고리즘이며 효과적인 그래디언트 감소를 더 컨트롤하는 특수한 방법이다.

폭발하는 그래디언트를 막기위해 클리핑을한다.

```python
# 최적화를 위해 필요한 값 얻기
trainable_variables = tf.trainable_variables()

# Compute and clip the gradients
gradients = tf.gradients(loss, trainable_variables)
gradients, _ = tf.clip_by_global_norm(gradients, 5)

# 아담 옵티마이저 사용
algorithm.optimizer = tf.train.AdamOptimizer(learning_rate=2e-3)
train_op = optimizer.apply_gradients( zip(gradients, trainable_variables) )
```

교욱에 필요한 모든 텐서플로 작업을 정의 후 이제 `미니 배치로 최적화 작업`을 할 수 있다.  
만약 data_feeder가 입력 및 대상의 연속적인 배치를 반환하는 생성기인 경우, 입력 및 대상 배치를 반복적으로 공급하여 이러한 `배치를 훈련`할 수 있다.  
네트워크가 시퀀스 시작 시 초기 상태를 처리하는 방법을 학습할 수 있도록 우리는 초기 상태를 100 미니 배치마다 재설정한다.  
모델을 `텐서흐름 보호기`로 저장하여 나중에 샘플링하기 위해 다시 로드할 수 있다.

```python
with tf.Session() as session:
  session.run(tf.initialize_all_variables())
  for i in range(minibatch_iterations):
    input_batch, target_batch = next(data_feeder)
    loss, _ = sess.run(
      (loss, train_op),
      feed_dict={ inputs: input_batch,targets: target_batch}
      )
    # Reset initial state every 100 minibatches
    if i % 100 == 0 and i != 0:
      for state in tf.python.util.nest.flatten(state_variables):
        session.run(state.initializer)
```