"""
2차원 리스트(list)를 이용한 행렬
"""


def shape(matrix):
    """
    행렬의 행과 열의 개수를 tuple 형태로 리턴
    :param matrix: nxm 행렬(행의 개수가 n개, 열의 개수가 m개인 2차원 리스트)
    :return: tuple(n, m)
    """
    return len(matrix), len(matrix[0])


def get_row(matrix, index):
    """
    주어진 행렬(matrix)에서 index에 해당하는 row를 리턴
    :param matrix: nxm 행렬
    :param index: 행 번호
    :return: 벡터(원소가 m개인 1차원 리스트)
    """
    return matrix[index]


def get_column(matrix, index):
    """
    주어진 행렬에서 index에 해당하는 column을 리턴
    :param matrix: nxm 행렬
    :param index: 행 번호
    :return: 벡터(원소가 m개인 1차원 리스트)
    """
    # r = []
    # for v in matrix:
    #     r.append(v[index])
    # return r
    return [x[index] for x in matrix]


def make_matrix(nrows, ncols, fn):
    """
    함수 fn의 리턴값들로 이루어진 nrows x ncols 행렬을 생성
    :param nrows: 행의 개수
    :param ncols: 열의 개수
    :param fn: 함수(fn(nrows, ncols) = 숫자)
    :return: nrows x ncols 행렬
    """
    # result = []
    # for i in range(nrows):
    #     col = []
    #     for j in range(ncols):
    #         col.append(fn(i, j))
    #     result.append(col)
    # return result
    return [[fn(i, j) for j in range(ncols)] for i in range(nrows)]


def transpose(matrix):
    """
    주어진 행렬에서 행과 열을 뒤바꾼 행렬(전치행렬)을 리턴
    :param matrix: n x m 행렬
    :return: m x n 행렬
    """
    # result = []
    # for i in range(len(matrix[0])):
    #     result.append(get_column(matrix, i))
    # return result

    # return [get_column(matrix, i) for i in range(len(matrix[0]))]
    # return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]

    nrows, ncols = shape(matrix)
    return make_matrix(ncols, nrows, lambda i, j: matrix[j][i])


def transpose(matrix):
    print('unpacking 연산자 *를 사용한 transpose')
    # t = []
    # for col in zip(*matrix):
    #     t.append(col)
    # return t
    return [list(x) for x in zip(*matrix)]


if __name__ == '__main__':
    # 2x3 행렬(row=2, column=3)
    A = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    # 3x2 행렬(row=3, column=2)
    B = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]

    print(A)
    print('Shape of A =', shape(A))
    print(B)
    print('Shape of B =', shape(B))
    print(get_column(A, 0))
    print(get_column(B, 0))
    print(get_row(A, 0))
    print(get_row(B, 0))

    test = make_matrix(2, 3, lambda x, y: x+y)
    print(test)

    m = make_matrix(2, 2, lambda i, j: i * j)
    print(m)

    def identity(x, y):
        # if x == y:
        #     return 1
        # else:
        #     return 0

        # result = 1 if x == y else 0  # 3항 연산자
        # return result
        return 1 if x == y else 0

    identity_matrix = make_matrix(3, 3, lambda x, y: 1 if x == y else 0)
    print(identity_matrix)

    m1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(transpose(m1))

    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [7, 8, 9]
    for x, y, z in zip(a, b, c):
        print(x, y, z)

    # unpacking 연산자: *
    print('A =', A)
    print('*A =', *A)
    print('B =', B)
    print('*B =', *B)

