import numpy as np

# numpy.c_ (column bind)와 numpy.r_(row bind)의 비교
a = np.array([1, 2, 3])
print(a, type(a), a.shape)
b = np.array([4, 5, 6])
print(b, type(b), b.shape)

c = np.c_[a, b]
print(c, type(c), c.shape)

d = np.r_[a, b]
print(d, type(d), d.shape)

e = np.array([[1, 2, 3],
              [4, 5, 6]])
f = np.array([[10, 20],
              [30, 40]])
print(np.c_[e, f])  # e와 f의 row 개수가 같아야 column 방향으로 붙일 수 있음
# print(np.r_[e, f])  # e와 f의 column 개수가 다르면 row 방향으로 붙일 수 없음!

g = np.array([[100, 200, 300]])
# print(np.c_[e, g])  # row의 개수가 달라 오른쪽으로 못 붙임
print(np.r_[e, g])  # column의 개수가 같아야 밑으로 붙일 수 있음

# (2, 3) shape의 모든 원소가 1인 array를 생성해서 출력: A
A = np.ones((2, 3), dtype='int')
print(A)
# (2, 3) shape의 모든 원소가 0인 array를 생성해서 출력: B
B = np.zeros((2, 3), 'int')
print(B)
# (3, 2) shape의 모든 원소는 1 ~ 6인 array를 생성해서 출력: C
C = np.arange(1, 7).reshape((3, 2))
print(C)
# (3, 2) shape의 난수들로 이루어진 array를 생성해서 출력: D
D = np.random.random((3, 2))
print(D)

