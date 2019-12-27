"""
numpy의 행렬 관련 함수
"""


import numpy as np

# numpy.darray 타입의 객체를 생성
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
B = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

print(A)
print(B)
print(A.shape)
print(B.shape)

# list[r]w][col], ndarray[row, col]
print(A[1, 2])
print(A[0, 0:2])
print(A[0:2, 0:2])
print(A[:, 0:2])
print(A[:, 0])  # 인덱스 0번 컬럼의 원소들로 이루어진 array
print(A[0, :])  # 인덱스 0번 row의 원소로 이루어진 array

# 항등 행렬(Identity Matrix)
identity_matrix = np.identity(3, dtype=int)
print(identity_matrix)

# 전치 행렬(Transpose Matrix)
print(A.transpose())
print(B.transpose())

# 행렬 곱셈
print(A.dot(B))
print(B                                                                          .dot(A))
