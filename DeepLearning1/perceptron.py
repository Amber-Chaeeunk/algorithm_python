# def AND(x1, x2):
#     w1, w2, theta = 0.5, 0.5, 0.8
#     cal = w1*x1 + w2*x2
#     if cal <= theta:
#         return 0
#     elif cal > theta:
#         return 1
#
# print(AND(0, 0), AND(1, 0), AND(0, 1), AND(1, 1), sep='\n')

#
# import numpy as np
# x = np.array([0,1])
# w = np.array([0.5, 0.5])
# b = -0.9
#
# print(w*x)
# print(np.sum(w*x))
# print(np.sum(w*x)+b)
#d

# import numpy as np
# def AND(x1, x2):
#     x = np.array([x1, x2])
#     w = np.array([0.5, 0.5])
#     b = -0.9
#     cal = np.sum(w*x)+b
#     if cal <= 0:
#         return 0
#     else:
#         return 1
#
# print(AND(0, 0), AND(1, 0), AND(0, 1), AND(1, 1), sep='\n')


# def XOR(x1, x2):
#     s1 = NAND(x1, x2)
#     s2 = OR(x1, x2)
#     y = AND(s1, s2)
#     return y
#
# print(XOR(0, 0))


# def step_function(x):
#     if x > 0:
#         return 1
#     if x <= 0:
#         return 0
#
#
# import numpy as np
# def step_function1(x):
#     y = x > 0
#     return y.astype(np.int)

#
# import numpy as np
# x = np.array([-1.0, 1.0, 2.0])
# print(x)
# y = x > 0
# y = y.astype(np.int)
# print(y)
#
# import numpy as np
# def sigmoid(x):
#     return 1 / (1 + np.exp(-x))
#
# x = np.array([-1.0, 1.0, 2.0])
# print(sigmoid(x))
#
# x = np.arange(-5.0, 5.0, 0.1)
# y = sigmoid(x)
# plt.plot(x, y)
# plt.ylim(-1.0, 1.1)
# plt.show()
#
#
# import numpy as np
#
# #1차원 배열
# A = np.array([1,2,3,4])
# print(A)
# print(np.ndim(A))  #배열의 차원 수
# print(A.shape)  #배열의 형상을 튜플로 나타냄
#
# #2차원 배열
# B = np.array([[1,2], [3,4],[5,6]])
# print(B)
# print(np.ndim(B))
# print(B.shape)
#
# import numpy as np
# A = np.array([[1,2], [3,4]])
# print(A.shape)
# B = np.array([[5,6], [7,8]])
# print(B.shape)
# print(np.dot(A,B))  #행렬의 곱


# import numpy as np
# X = np.array([1,2])
# print(X.shape)
# W = np.array([[1,3,5,], [2,4,6]])
# print(W)
# print(W.shape)
# Y = np.dot(X,W)
# print(Y)
#
# import numpy as np
#
# #0층에서 1층
# X = np.array([1.0, 0.5])
# W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
# B1 = np.array([0.1, 0.2, 0.3])
# A1 = np.dot(X, W1) + B1
# print(A1)
# def sigmoid(x):
#      return 1 / (1 + np.exp(-x))
# Z1 = sigmoid(A1)
# print(Z1)
#
#
# #1층에서 2층
# W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
# B2 = np.array([0.1, 0.2])
# A2 = np.dot(Z1, W2) + B2
# print(A2)
# Z2 = sigmoid(A2)
# print(Z2)
#
#
# #2층에서 3층
# def identity_function(x):  #항등함수
#     return x
# W3 = np.array([[0.1, 0.3],[0.2, 0.4]])
# B3 = np.array([0.1, 0.2])
# A3 = np.dot(Z2, W3) + B3
# Y = identity_function(A3) #생략해도 무관함 Y = A3
# print(Y)
#
# import numpy as np
# def init_network():
#     network = {}
#     network['W1'] = np.array([[0.1, 0.3, 0.5],[0.2, 0.4, 0.6]])
#     network['b1'] = np.array([0.1, 0.2, 0.3])
#     network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
#     network['b2'] = np.array([0.1, 0.2])
#     network['W3'] = np.array([[0.1, 0.3],[0.2, 0.4]])
#     network['b3'] = np.array([0.1, 0.2])
#     return network
#
# def forward(network, x):
#     W1, W2, W3 = network['W1'], network['W2'], network['W3']
#     b1, b2, b3 = network['b1'], network['b2'], network['b3']
#     def sigmoid(x):
#          return 1 / (1 + np.exp(-x))
#     def identity_function(x):
#         return x
#     a1 = np.dot(x, W1) + b1
#     z1 = sigmoid(a1)
#     a2 = np.dot(z1, W2) + b2
#     z2 = sigmoid(a2)
#     a3 = np.dot(z2, W3) + b3
#     y = identity_function(a3)
#     return y
#
# network = init_network()
# x = np.array([1.0, 0.5])
# y = forward(network, x)
# print(y)
#

# import numpy as np
#
# a = np.array([0.3, 2.9, 4.0])
# exp_a = np.exp(a)
# print(exp_a)
# sum_exp_a = np.sum(exp_a)
# print(sum_exp_a)
# y = exp_a / sum_exp_a
# print(y)
#
# import numpy as np
# def softmax(a):
#     exp_a = np.exp(a)
#     sum_exp_a = np.sum(exp_a)
#     y = exp_a / sum_exp_a
#
#     return y
#
#
#
# import numpy as np
# a = np.array([1010, 1000, 990])
# print(np.exp(a) / np.sum(np.exp(a)))  #에러남
#
# C = np.max(a)
# print(a-C)
# print(np.exp(a-C) / np.sum(np.exp(a-C))) #개선함

# import numpy as np
# def softmax(a):
#     C = np.max(a)
#     exp_a = np.exp(a-C)
#     sum_exp_a = np.sum(exp_a)
#     y = exp_a / sum_exp_a
#
#     return y

#


# try:
#     import urllib.request
# except ImportError:
#     raise ImportError('You should use Python 3.x')
# import os.path
# import gzip
# import pickle
# import os
# import numpy as np
#
# url_base = 'http://yann.lecun.com/exdb/mnist/'
# key_file = {
#     'train_img': 'train-images-idx3-ubyte.gz',
#     'train_label': 'train-labels-idx1-ubyte.gz',
#     'test_img': 't10k-images-idx3-ubyte.gz',
#     'test_label': 't10k-labels-idx1-ubyte.gz'
# }
#
# dataset_dir = os.path.dirname(os.path.abspath(__file__))
# save_file = dataset_dir + "/mnist.pkl"
#
# train_num = 60000
# test_num = 10000
# img_dim = (1, 28, 28)
# img_size = 784


# def _download(file_name):
#     file_path = dataset_dir + "/" + file_name
#
#     if os.path.exists(file_path):
#         return
#
#     print("Downloading " + file_name + " ... ")
#     urllib.request.urlretrieve(url_base + file_name, file_path)
#     print("Done")
#
#
# def download_mnist():
#     for v in key_file.values():
#         _download(v)
#
#
# def _load_label(file_name):
#     file_path = dataset_dir + "/" + file_name
#
#     print("Converting " + file_name + " to NumPy Array ...")
#     with gzip.open(file_path, 'rb') as f:
#         labels = np.frombuffer(f.read(), np.uint8, offset=8)
#     print("Done")
#
#     return labels
#
#
# def _load_img(file_name):
#     file_path = dataset_dir + "/" + file_name
#
#     print("Converting " + file_name + " to NumPy Array ...")
#     with gzip.open(file_path, 'rb') as f:
#         data = np.frombuffer(f.read(), np.uint8, offset=16)
#     data = data.reshape(-1, img_size)
#     print("Done")
#
#     return data
#
#
# def _convert_numpy():
#     dataset = {}
#     dataset['train_img'] = _load_img(key_file['train_img'])
#     dataset['train_label'] = _load_label(key_file['train_label'])
#     dataset['test_img'] = _load_img(key_file['test_img'])
#     dataset['test_label'] = _load_label(key_file['test_label'])
#
#     return dataset
#
#
# def init_mnist():
#     download_mnist()
#     dataset = _convert_numpy()
#     print("Creating pickle file ...")
#     with open(save_file, 'wb') as f:
#         pickle.dump(dataset, f, -1)
#     print("Done!")
#
#
# def _change_one_hot_label(X):
#     T = np.zeros((X.size, 10))
#     for idx, row in enumerate(T):
#         row[X[idx]] = 1
#
#     return T
#
#
# def load_mnist(normalize=True, flatten=True, one_hot_label=False):
#     """MNIST 데이터셋 읽기
#
#     Parameters
#     ----------
#     normalize : 이미지의 픽셀 값을 0.0~1.0 사이의 값으로 정규화할지 정한다.
#     one_hot_label :
#         one_hot_label이 True면、레이블을 원-핫(one-hot) 배열로 돌려준다.
#         one-hot 배열은 예를 들어 [0,0,1,0,0,0,0,0,0,0]처럼 한 원소만 1인 배열이다.
#     flatten : 입력 이미지를 1차원 배열로 만들지를 정한다.
#
#     Returns
#     -------
#     (훈련 이미지, 훈련 레이블), (시험 이미지, 시험 레이블)
#     """
#     if not os.path.exists(save_file):
#         init_mnist()
#
#     with open(save_file, 'rb') as f:
#         dataset = pickle.load(f)
#
#     if normalize:
#         for key in ('train_img', 'test_img'):
#             dataset[key] = dataset[key].astype(np.float32)
#             dataset[key] /= 255.0
#
#     if one_hot_label:
#         dataset['train_label'] = _change_one_hot_label(dataset['train_label'])
#         dataset['test_label'] = _change_one_hot_label(dataset['test_label'])
#
#     if not flatten:
#         for key in ('train_img', 'test_img'):
#             dataset[key] = dataset[key].reshape(-1, 1, 28, 28)
#
#     return (dataset['train_img'], dataset['train_label']), (dataset['test_img'], dataset['test_label'])
#
#
# if __name__ == '__main__':
#     init_mnist()

#

# import sys, os
# sys.path.append(os.pardir)
# from dataset.mnist import load_mnist
#
# (x_train, t_train), (x_test, t_test) = \
#     load_mnist(flatten=True, normalize=False)
