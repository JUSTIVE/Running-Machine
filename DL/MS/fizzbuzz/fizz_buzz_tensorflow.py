# -*- coding: utf-8 -*-
# >>>original
import numpy as np
import tensorflow as tf
# >>>additional modules what i've added
import unittest as ut # for unit-test(for the concept of Test-Driven Development)
# from os import system # both modules are legacy of attempting carriage-return
# import sys
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] ='2'

# 이진수의 자리를 10자리로 설정
NUM_DIGITS = 10

def binaryEncode(i, num_digits):
    """입력된 수를 이진화하는 함수"""
    return np.array([i >> d & 1 for d in range(num_digits)])

def fizzBuzzEncode(i):
    """입력된 숫자를 one-hot encoding 된 fizzbuzz로 바꾸는 함수"""
    if   not i % 15 :   return np.array([0,0,0,1])
    elif not i % 5 :    return np.array([0,0,1,0])
    elif not i % 3 :    return np.array([0,1,0,0])
    else:               return np.array([1,0,0,0])

# 트레이닝셋 설정
trX = np.array([binaryEncode(i,NUM_DIGITS)  for i in range (101,2**(NUM_DIGITS))]) # [[1,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,,0,0],[]]
trY = np.array([fizzBuzzEncode(i)           for i in range (101,2**(NUM_DIGITS))])

#뉴런의 가중치를 무작위값으로 설정
def initWeights(shape):
    return tf.Variable(tf.random_normal(shape,stddev=0.01))

# 본 뉴럴 네트워크의 모델
def model(X,
    w_h,b_h,
    w_h2,b_h2,
    w_h3,b_h3,
    w_h4,b_h4,
    w_o,b_o):
    h = tf.nn.relu(tf.matmul(X,w_h)+b_h)# 렐루 활성화 함수 (1*3) * (3*3)= (1*3)
    h2 = tf.nn.relu(tf.matmul(h,w_h2)+b_h2)
    h3 = tf.nn.relu(tf.matmul(h2,w_h3)+b_h3)
    h4 = tf.nn.relu(tf.matmul(h3,w_h4)+b_h4)
    return tf.matmul(h4,w_o)+b_o


# 입력 레이어 10차원을 설정
X = tf.placeholder("float",[None, NUM_DIGITS])
Y = tf.placeholder("float",[None,4])

NUM_HIDDEN = 500
w_h = initWeights([NUM_DIGITS,NUM_HIDDEN])#히든 레이어 설정 
b_h = initWeights([NUM_HIDDEN])# 히든레이어 바이어스

w_h2 = initWeights([NUM_HIDDEN,NUM_HIDDEN])
b_h2 = initWeights([NUM_HIDDEN])

w_h3 = initWeights([NUM_HIDDEN,NUM_HIDDEN])
b_h3 = initWeights([NUM_HIDDEN])

w_h4 = initWeights([NUM_HIDDEN,NUM_HIDDEN])
b_h4 = initWeights([NUM_HIDDEN])

w_o = initWeights([NUM_HIDDEN, 4])# 출력 레이어 설정
b_o = initWeights([4])# 히든-히든레이어 설정

py_x = model(X,
    w_h,b_h,
    w_h2,b_h2,
    w_h3,b_h3,
    w_h4,b_h4,
    w_o,b_o)# 모델 인스턴스 생성

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=py_x,logits=Y))
train_op = tf.train.GradientDescentOptimizer(0.000001).minimize(cost)

predict_op = tf.argmax(py_x,1)

#출력 벡터로부터 fizz-buzz를 반환
def fizzBuzz(i,prediction):
    return [str(i), "fizz","buzz","fizzbuzz"][prediction]

# class TestSetChecker(ut.TestCase):
#     def test_fzbzEncoderTest(self):
#         self.assertEqual(fizzBuzz(2,0),"2")
#         self.assertEqual(fizzBuzz(3,1),"fizz")
#         self.assertEqual(fizzBuzz(5,2),"buzz")
#         self.assertEqual(fizzBuzz(15,3),"fizzbuzz")

class TestBinaryEncode(ut.TestCase):
    def test_binaryencode(self):
        self.assertListEqual(list(binaryEncode(1,NUM_DIGITS)),list([1,0,0,0,0,0,0,0,0,0]))
        self.assertListEqual(list(binaryEncode(101,NUM_DIGITS)),list([1,0,1,0,0,1,1,0,0,0]))

# #test-driven development 를 위해서 unittest를 수행하는 부분
# if __name__ =='__main__':
#     ut.main()

BATCH_SIZE=128

with tf.Session() as sess:
    tf.global_variables_initializer().run()

    for epoch in range(10000):
        #트레이닝 데이터셋에서 임의의 인덱스를 뽑음
        p = np.random.permutation(range(len(trX)))
        #해당 인덱스 번째의 데이터셋
        trX,trY = trX[p],trY[p]
        
        # 0 부터 전체 데이터셋까지 BatchSize만큼 간격으로
        for start in range(0,len(trX),BATCH_SIZE):
            end = start + BATCH_SIZE
            # start부터 batchSize만큼의 데이터를 학습
            sess.run(train_op,feed_dict={X:trX[start:end],Y:trY[start:end]})
            
        #현재 epoch에서의 training 결과
        print(epoch,'\t',"[","]",np.mean(np.argmax(trY,axis=1)==sess.run(predict_op,feed_dict={X:trX,Y:trY})))

    # 트레이닝셋 이후의 테스트셋
    numbers = np.arange(1,101)
    teX = np.transpose(binaryEncode(numbers,NUM_DIGITS))
    teY = sess.run(predict_op,feed_dict={X:teX})
    output = np.vectorize(fizzBuzz)(numbers, teY)

    print(output)