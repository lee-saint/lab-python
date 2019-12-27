"""
선형 대수(Linear Algebra)
"""
from math import sqrt


def add(v, w):
    """

    :param v: n차원 벡터(성분이 n개인 벡터)
    :param w: n차원 벡터(성분이 n개인 벡터)
    :return: 각 성분별로 더하기 결과를 갖는 벡터
    """
    if len(v) != len(w):
        raise ValueError('v and w must have same length.')
    return [x + y for x, y in zip(v, w)]


def subtract(v, w):
    """
    주어진 두 개의 n차원 벡터에서 성분별로 뺄셈을 수행
    :param v: n차원 벡터
    :param w: n차원 벡터
    :return: n차원 벡터
    """
    if len(v) != len(w):
        raise ValueError('v and w must have same length.')
    return [x - y for x, y in zip(v, w)]


def vector_sum(vectors):
    """
    모든 벡터들에서 각 성분별 더하기를 수행
    vector_sum([[1, 2], [3, 4], [5, 6]]) = [9, 12]

    :param vectors: n차원 벡터들의 리스트
    :return: n차원 벡터
    """
    len_of_vectors = len(vectors[0])
    for v in vectors[1:]:
        if len_of_vectors != len(v):
            raise ValueError('All vectors must have the same length.')

    v_sum = vectors[0]
    for v in vectors[1:]:
        v_sum = add(v_sum, v)
    return v_sum


def scalar_multiply(c, vector):
    """
    c * [x1, x2, x3, ...] = [c*x1, c*x2, c*x3, ...]
    :param c: 숫자(스칼라, scalar)
    :param vector: n차원 벡터
    :return: n차원 벡터
    """
    return [c * i for i in vector]


def dot(v, w):
    """
    [v1, v2, v3, ...] · [w1, w2, w3, ...] = v1*w1 + v2*w2 + v3*w3 + ...
    :param v: n차원 벡터
    :param w: n차원 벡터
    :return: 숫자(스칼라)
    """
    if len(v) != len(w):
        raise ValueError('v and w must have the same length.')
    sum_ = 0
    for i in range(len(v)):
        sum_ += v[i] * w[i]
    return sum_


def vector_mean(vectors):
    """
    주어진 벡터들의 리스트에서 각 항목별 평균으로 이루어진 벡터
    :param vectors: n차원 벡터들의 리스트
    :return: n차원 벡터
    """
    return scalar_multiply(1 / len(vectors), vector_sum(vectors))
    # len_vec = len(vectors[0])
    # for v in vectors[1:]:
    #     if len_vec != len(v):
    #         raise ValueError('All vectors must have the same length.')
    # sum_ = [0] * len_vec
    # for i in len_vec:
    #     for v in vectors:
    #         sum_[i] += v[i]
    # return


def sum_of_squares(vector):
    """
    v = [x1, x2, ..., xn]일 때,
    x1 ** 2 + x2 ** 2 + ... + xn ** 2을 리턴
    :param vector: n차원 벡터
    :return: 숫자
    """
    # sum_ = 0
    # for i in vector:
    #     sum_ += i ** 2
    # return sum_
    return dot(vector, vector)


def magnitude(vector):
    """
    벡터의 크기를 리턴 - math.sqrt(sum_of_squares)
    :param vector:
    :return:
    """
    return sqrt(sum_of_squares(vector))


def squared_distance(v, w):
    """
    v = [v1, v2, ..., vn], w = [w1, w2, ..., wn]
    (v1-w1)**2 + (v2-w2)**2 + ... + (vn-wn)**2 리턴

    :param v: n차원 벡터
    :param w: n차원 벡터
    :return: 숫자
    """
    return sum_of_squares(subtract(v, w))


def distance(v, w):
    """
    두 벡터 v와 w 사이의 거리를 리턴 - sqrt(squared_distance)
    :param v: n차원 벡터
    :param w: n차원 벡터
    :return: 숫자
    """
    return sqrt(squared_distance(v, w))


if __name__ == "__main__":
    a = [1, 2, 3]
    b = [4, 5, 6]
    print('add =', add(a, b))
    print('sub =', subtract(a, b))
    print(scalar_multiply(3, a))
    print(dot(a, b))

    a = [1, 2]
    b = [3, 4]
    print('add =', add(a, b))
    print('sub =', subtract(a, b))

    a = [1, 2]
    b = [3, 4]
    c = [5, 6]
    print(vector_sum([a, b, c]))

    v = [2, 3]
    unit_x = [1, 0]  # x축 단위벡터
    unit_y = [0, 1]  # y축 단위벡터
    dot1 = dot(v, unit_x)
    print('dot1 =', dot1)
    dot2 = dot(v, unit_y)
    print('dot2 =', dot2)

    vectors = [
        [1, 2, 3],
        [3, 4, 5],
        [5, 6, 7],
        [7, 8, 9]
    ]
    vm = vector_mean(vectors)
    print(vm)

    v = [3, 4]
    print(sum_of_squares(v))
    print(magnitude(v))

    v = [1, 2]
    w = [4, 6]
    print(squared_distance(v, w))
    print(distance(v, w))

