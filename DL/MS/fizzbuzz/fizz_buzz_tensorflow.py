import numpy as np
import tensorflow as tf
import unittest as ut
from os import system
import sys

def binaryEncode(i, num_digits):
    """입력된 수를 이진화하는 함수"""
    return np.array([i >> d & 1 for d in range(num_digits)])

def fizzBuzzEncode(i):
    """입력된 숫자를 one-hot encoding 된 fizzbuzz로 바꾸는 함수"""
    if   not i % 15 :   return np.array([0,0,0,1])
    elif not i % 5 :    return np.array([0,0,1,0])
    elif not i % 3 :    return np.array([0,1,0,0])
    else:               return np.array([1,0,0,0])

# 이진수의 자리를 10자리로 설정
NUM_DIGITS = 10

# 트레이닝셋 설정
trX = np.array([binaryEncode(i,NUM_DIGITS)  for i in range (101,2**NUM_DIGITS)])
trY = np.array([fizzBuzzEncode(i)           for i in range (101,2**NUM_DIGITS)])

#뉴런의 가중치를 무작위값으로 설정
def initWeights(shape):
    return tf.Variable(tf.random_normal(shape,stddev=0.01))

# 본 뉴럴 네트워크의 모델
def model(X,w_h,w_o):
    h = tf.nn.relu(tf.matmul(X,w_h))# 렐루 활성화 함수
    return tf.matmul(h,w_o)

# 입력 레이어 10차원을 설정
X = tf.placeholder("float",[None, NUM_DIGITS])
Y = tf.placeholder("float",[None,4])

NUM_HIDDEN = 100

w_h = initWeights([NUM_DIGITS,NUM_HIDDEN])#히든 레이어 설정
w_o = initWeights([NUM_HIDDEN, 4])# 출력 레이어 설정

py_x = model(X,w_h,w_o)# 모델 인스턴스 생성

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=py_x,logits=Y))
train_op = tf.train.GradientDescentOptimizer(0.05).minimize(cost)

predict_op = tf.argmax(py_x,1)

#출력 벡터로부터 fizz-buzz를 반환
def fizzBuzz(i,prediction):
    return [str(i), "fizz","buzz","fizzbuzz"][prediction]


class TestSetChecker(ut.TestCase):
    def fzbzEncoderTest(self):
        self.assertEqual(fizzBuzzEncode(105),np.array([0,0,0,1]))
        self.assertEqual(fizzBuzzEncode(110),np.array([0,0,1,0]))
        self.assertEqual(fizzBuzzEncode(108),np.array([0,1,0,0]))
        self.assertEqual(fizzBuzzEncode(106),np.array([1,0,0,0]))

# test-driven development 를 위해서 unittest를 수행하는 부분
# if __name__ =='__main__':
#     ut.main()

BATCH_SIZE=128
TEST_SIZE =10000

with tf.Session() as sess:
    tf.initialize_all_variables().run()

    for epoch in range(TEST_SIZE):
        p = np.random.permutation(range(len(trX)))
        trX,trY = trX[p],trY[p]

        for start in range(0,len(trX),BATCH_SIZE):
            end = start + BATCH_SIZE
            sess.run(train_op,feed_dict={X:trX[start:end],Y:trY[start:end]})

        #현재 epoch에서의 training 결과
        print(epoch/TEST_SIZE,'\t',"[","]",np.mean(np.argmax(trY,axis=1)==sess.run(predict_op,feed_dict={X:trX,Y:trY})))

    # 트레이닝셋 이후의 테스트셋
    numbers = np.arange(1,101)
    teX = np.transpose(binaryEncode(numbers,NUM_DIGITS))
    teY = sess.run(predict_op,feed_dict={X:teX})
    output = np.vectorize(fizzBuzz)(numbers, teY)

    print(output)




