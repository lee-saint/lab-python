"""
numpy를 사용하지 않고 add(x, y), subtract(), multiply(), divide(), dot() 함수를 구현
"""
import numpy as np
from numpy.linalg import inv


def add(x, y):
    rownum = x.shape[0]
    colnum = x.shape[1]
    result = np.empty((rownum, colnum))
    for i in range(rownum):
        for j in range(colnum):
            result[i][j] = x[i][j] + y[i][j]
    return result


def subtract(x, y):
    rownum = x.shape[0]
    colnum = x.shape[1]
    result = np.empty((rownum, colnum))
    for i in range(rownum):
        for j in range(colnum):
            result[i][j] = x[i][j] - y[i][j]
    return result


def multiply(x, y):
    rownum = x.shape[0]
    colnum = x.shape[1]
    result = np.empty((rownum, colnum))
    for i in range(rownum):
        for j in range(colnum):
            result[i][j] = x[i][j] * y[i][j]
    return result


def divide(x, y):
    rownum = x.shape[0]
    colnum = x.shape[1]
    result = np.empty((rownum, colnum))
    for i in range(rownum):
        for j in range(colnum):
            result[i][j] = x[i][j] / y[i][j]
    return result


def dot(x, y):
    if x.shape[1] != y.shape[0]:
        raise ValueError('dot 연산을 할 수 없는 형식입니다!')
    rownum = x.shape[0]
    medium = x.shape[1]
    colnum = y.shape[1]
    result = np.zeros((rownum, colnum))
    for i in range(rownum):
        for j in range(colnum):
            for n in range(medium):
                result[i][j] += x[i][n] * y[n][j]
    return result


if __name__ == '__main__':
    x = np.array([[1, 2],
                  [3, 4]])
    y = np.array([[5, 6],
                  [7, 8]])
    print(add(x, y))
    print(subtract(x, y))
    print(multiply(x, y))
    print(divide(x, y))
    print(dot(x, y))
    print(x @ y)  # A.dot(B)
    print(dot(y, x))
    print(y @ x)  # B.dot(A)

    a = np.array([[1, 2, 3],
                  [4, 5, 6]])
    b = np.array([[1, 2, 3, 4],
                  [1, 2, 3, 4],
                  [1, 2, 3, 4]])
    print(dot(a, b))

"""
항등 행렬(Indentity matrix): 대각선의 원소는 1이고, 나머지 원소는 0인 정사각행렬
    A @ I = I @ A = A를 만족
역행렬(Inverse matrix): A @ A- = A- @ A = I를 만족하는 행렬
전치 행렬(Transpose matrix): 행렬의 row와 column을 서로 바꾼 행렬
"""
identity = np.identity(2)
print(identity)
print(x.dot(identity))
print(identity.dot(x))

x_inv = inv(x)
print(x_inv)
print(x.dot(x_inv))
print(x_inv.dot(x))

x_tp = np.transpose(x)
print(x_tp)
