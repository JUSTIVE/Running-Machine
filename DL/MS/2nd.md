# Machine Learning - an Introduction

## Brief desciption of popular techniques/algorithms

### 딥 러닝

이전 문단에서는 1개 `피드-포워드:feed forward` 레이어의 매우 간단한 뉴럴 넷의 예제를 소개했다. 그들이 `피드-포워드`라 불리는 이유는 정보가 입력에서 출력을 향하고, 절대 순환하지 않으며, 1개 레이어인 이유는 입력 레이어를 제외하고는 1개의 출력 레이어만 가지기 때문이다. 우리는 이미 1개의 `피드-포워드` 네트워크가 선형적인 분류에서만 가능하며, 논리적인 XOR 연산에 접근하지 못하는 한계들에 논의했다. 하지만, 네트워크는 입력 레이어와 출력 레이어 사이에 추가적인 레이어를 가질 수 있다. 이 레이어들은 `히든 레이어:hidden layer`라고 불린다. 히든 레이어를 가진 피드 포워드 네트워크는 정보를 입력 레이어에서 히든레이어를 통해 출력 레이어로 보낼 것이고, 이것은 입력을 받고 출력을 정의하는 함수가 될 것이다. 이것에 관한 `보편적 근사 정리:Universal Approximation Theorem, 시벤코 정리:Cybenko's Theorem`가 있다. 
>`Cybenko's Theorem`  
>1989년 시벤코가 발표한 정리
>$\varphi$를 *sigmoid* 함수라 할 때, $[0,1]^n$ 또는 $R^n$의 부분 집합에서 실수의 연속 함수 f 와 $\epsilon>0$이 주어지면  
>> sigmoid란 이렇게 생긴 함수를 말함  
$S(x)=\frac{1}{1+e^{-x}}=\frac{e^x}{e^x+1}$  
이 함수는 미분값으로 $\frac{dy}{dx}=\frac{e^x}{(1+e^x)^2}$인데 계산하기 쉬워서 사용
>>
>다음을 만족하는 벡터 $w=(w_1,w_2,...w_n)$,$\alpha$,$\theta$ 와 매개 함수 $G(\cdot,w,\alpha,\theta):[0,1]^n\rightarrow R$이 존재한다.  
>$|G(x,w,\alpha,\theta) -f(x)|<|\epsilon|\forall x\in[0,1]^n$  
이 때,  
$G(x,w,\alpha,\theta)=\displaystyle\sum_{i=1}^{n}\alpha_j\varphi(w_j^Tx+\theta_j)$이고,  
$w_j\in{R^n},\alpha_j,\theta_j\in{R},w=(w_1,w_2,...w_n),\alpha=(\alpha_1,\alpha2,...,\alpha_n),\theta=(\theta_1,\theta_2,...,\theta_n)$이다.
>> 드럽게 어려운것 같지만 하나의 히든 레이어를 가지더라도 뉴런의 수만 많으면 비선형적인 문제도 충분히 풀 수 있다는 얘기다.

이 정리는 적어도 하나의 히든 레이어가 있는 신경망으로 모든 함수를 근사할 수 있다고 말한다. 다음장에서 이것이 왜 참인지 영감을 줄 것이다.

오랜 기간동안, 이 정리와 복잡한 네트워크 동작의 어려움에 의해 사람들은 하나의 히든 레이어만 가지는 얕은 네트워크로 일하곤 했다. 반면, 최근 사람들은 