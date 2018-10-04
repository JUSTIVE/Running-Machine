# -*- coding: utf-8 -*-
# >>>original
import numpy as np
import tensorflow as tf
# >>>additional modules what i've added
import unittest as ut # for unit-test(for the concept of Test-Driven Development)
# from os import system # both modules are legacy of attempting carriage-return
# import sys
import matplotlib.pyplot as plt
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] ='2'

# 이진수의 자리를 10자리로 설정
NUM_DIGITS = 10

def binaryEncode(i, num_digits):
    """입력된 수를 이진화하는 함수"""
    return np.array([i >> d & 1 for d in range(num_digits)])

def fizzBuzzEncode(i):
    """입력된 숫자를 one-hot encoding 된 fizzbuzz로 바꾸는 함수"""
    if   i % 15 == 0 :  return np.array([0,0,0,1])
    elif i % 5  == 0 :  return np.array([0,0,1,0])
    elif i % 3  == 0 :  return np.array([0,1,0,0])
    else:               return np.array([1,0,0,0])

# 트레이닝셋 설정
trX = np.array([binaryEncode(i,NUM_DIGITS)  for i in range (101,2**(NUM_DIGITS))]) # [[1,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,,0,0],[]]
trY = np.array([fizzBuzzEncode(i)           for i in range (101,2**(NUM_DIGITS))])

#뉴런의 가중치를 무작위값으로 설정
def initWeights(shape):
    return tf.Variable(tf.random_normal(shape,stddev=0.01))

# 본 뉴럴 네트워크의 모델
def model(X,b_h,
    w_h,w_h2,w_h3,
    w_o,):
    h = tf.nn.relu(tf.matmul(X,w_h))# 렐루 활성화 함수 (1*3) * (3*3)= (1*3)
    h2 = tf.nn.relu(tf.matmul(h,w_h2))
    # h3 = tf.nn.relu(tf.matmul(h2,w_h3))
    return tf.matmul(h2,w_o)

# 입력 레이어 10차원을 설정
X = tf.placeholder("float",[None, NUM_DIGITS])
Y = tf.placeholder("float",[None,4])

NUM_HIDDEN = 1000
b_h=initWeights([NUM_HIDDEN])
w_h = initWeights([NUM_DIGITS,NUM_HIDDEN])#히든 레이어 설정 
w_h2 = initWeights([NUM_HIDDEN,NUM_HIDDEN])#히든 레이어 설정 
w_h3 = initWeights([NUM_HIDDEN,NUM_HIDDEN])#히든 레이어 설정 
w_o = initWeights([NUM_HIDDEN, 4])# 출력 레이어 설정

py_x = model(X,b_h,
    w_h,w_h2,w_h3,
    w_o)# 모델 인스턴스 생성

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=Y,logits=py_x))
train_op = tf.train.GradientDescentOptimizer(0.05).minimize(cost)

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

BATCH_SIZE=250
TRAIN_SIZE = 10000
epoch_data=[]
acc_data=[]

with tf.Session() as sess:
    tf.global_variables_initializer().run()

    for epoch in range(TRAIN_SIZE):
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
        epoch_data.append(epoch)
        acc_data.append(np.mean(np.argmax(trY, axis=1) == sess.run(predict_op, feed_dict={X: trX, Y: trY})))
        print(epoch,'\t', acc_data[-1])

    # 트레이닝셋 이후의 테스트셋
    numbers = np.arange(1,101)
    teX = np.transpose(binaryEncode(numbers,NUM_DIGITS))
    teY = sess.run(predict_op,feed_dict={X:teX})
    output = np.vectorize(fizzBuzz)(numbers, teY)

    print(output)

actual = ['1','2','fizz','4','buzz','fizz','7','8','fizz','buzz','11','fizz','13','14','fizzbuzz','16','17','fizz','19','buzz','fizz','22','23','fizz','buzz','26','fizz','28','29','fizzbuzz','31','32','fizz','34','buzz','fizz','37','38','fizz','buzz','41','fizz','43','44','fizzbuzz','46','47','fizz','49','buzz','fizz','52','53','fizz','buzz','56','fizz','58','59','fizzbuzz','61','62','fizz','64','buzz','fizz','67','68','fizz','buzz','71','fizz','73','74','fizzbuzz','76','77','fizz','79','buzz','fizz','82','83','fizz','buzz','86','fizz','88','89','fizzbuzz','91','92','fizz','94','buzz','fizz','97','98','fizz','buzz']
correct = [(x == y) for x, y in zip(actual, output)]
print('correct',sum(correct))

plt.plot(epoch_data,acc_data,'ro')
plt.axis([0, TRAIN_SIZE, 0, 1])
plt.show()