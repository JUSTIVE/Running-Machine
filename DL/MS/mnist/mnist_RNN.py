import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("./mnist/data/", one_hot=True)#버전높으면 안될걸..


# 옵션 설정

learning_rate = 0.001
total_epoch = 50
batch_size = 256

# RNN 은 순서가 있는 자료를 다루므로,
# 한 번에 입력받는 갯수와, 총 몇 단계로 이루어져있는 데이터를 받을지를 설정해야합니다.
# 이를 위해 가로 픽셀수를 n_input 으로, 세로 픽셀수를 입력 단계인 n_step 으로 설정하였습니다.
n_input = 28
n_step = 28
n_hidden = 128
n_class = 10


# 신경망 모델 구성

with tf.name_scope('input_layer'):
    X = tf.placeholder(tf.float32, [None, n_step, n_input])#28* 28
with tf.name_scope('output_layer'):
    Y = tf.placeholder(tf.float32, [None, n_class])#10

W = tf.Variable(tf.random_normal([n_hidden, n_class]))#128,10
b = tf.Variable(tf.random_normal([n_class]))

# RNN 에 학습에 사용할 셀을 생성
# 다음 함수들을 사용하면 다른 구조의 셀로 간단하게 변경
# BasicRNNCell,BasicLSTMCell,GRUCell

cell = tf.nn.rnn_cell.BasicRNNCell(n_hidden)#셀 생성.

# RNN 신경망을 생성합니다
# 원래는 다음과 같은 과정을 거쳐야 하지만
# states = tf.zeros(batch_size)
# for i in range(n_step):
#     outputs, states = cell(X[[:, i]], states)
# ...
# 다음처럼 tf.nn.dynamic_rnn 함수를 사용하면
# CNN 의 tf.nn.conv2d 함수처럼 간단하게 RNN 신경망을 만들어줍니다.->ㅁㄹ

outputs, states = tf.nn.dynamic_rnn(cell, X, dtype=tf.float32)
# tf.nn.dynamic_rnn(셀,플레이스홀더입력값(x),데이터타입)

# 결과를 Y의 다음 형식과 바꿔야 하기 때문에
# Y : [batch_size, n_class]
# outputs 의 형태를 이에 맞춰 변경해야합니다.
# outputs : [batch_size, n_step, n_hidden]
#        -> [n_step, batch_size, n_hidden]
#        -> [batch_size, n_hidden]

outputs = tf.transpose(outputs, [1, 0, 2])
outputs = outputs[-1]#reshape같은데..
model = tf.matmul(outputs, W) + b

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=model, labels=Y))
optimizer = tf.train.AdamOptimizer(learning_rate).minimize(cost)
#아담 옵티마이저
# http://dalpo0814.tistory.com/29#adam-optimization-%EB%85%BC%EB%AC%B8-%EC%9A%94%EC%95%BD%EC%A0%95%EB%A6%AC


# 신경망 모델

sess = tf.Session()
sess.run(tf.global_variables_initializer())

total_batch = int(mnist.train.num_examples/batch_size)

for epoch in range(total_epoch):
    total_cost = 0
    tf.summary.merge_all()
    writer = tf.summary.FileWriter("./logs")
    writer.add_graph(sess.graph)

    for i in range(total_batch):
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)
        # X 데이터를 RNN 입력 데이터에 맞게 [batch_size, n_step, n_input] 형태로 변환합니다.
        batch_xs = batch_xs.reshape((batch_size, n_step, n_input))

        _, cost_val = sess.run([optimizer, cost], feed_dict={X: batch_xs, Y: batch_ys})
        total_cost += cost_val

    print('Epoch:', '%04d' % (epoch + 1),'Avg. cost =', '{:.3f}'.format(total_cost / total_batch))
    tf.summary.scalar('loss',(total_cost / total_batch))

print('최적화 완료!')

#########
# 결과 확인
######

#정확도
is_correct = tf.equal(tf.argmax(model, 1), tf.argmax(Y, 1))
accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))

#테스트 배치 사이즈
test_batch_size = len(mnist.test.images)

#데이터 대입
test_xs = mnist.test.images.reshape(test_batch_size, n_step, n_input)
test_ys = mnist.test.labels
print('정확도:', sess.run(accuracy,feed_dict={X: test_xs, Y: test_ys}))

#confusion = tf.confusion_matrix(labels = tf.argmax(test_ys,1),predictions = tf.argmax(model,1))
confusion = tf.confusion_matrix(tf.argmax(test_ys, 1),tf.argmax(model, 1))

test_confusion = sess.run(confusion, feed_dict={X: test_xs, Y: test_ys})
print(test_confusion)




