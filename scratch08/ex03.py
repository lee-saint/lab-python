"""
편미분(Partial Differentiation)을 이용한 경사 하강법
"""
import random
from scratch04.ex01 import scalar_multiply, add, distance


def partial_difference_quotient(f, v, i, h=0.001):
    """
    (f([x1, ..., xi + h, ..., xn]) - f([x1, ..., xi, ..., xn])) / h

    :param f: f(vector) = float인 함수
    :param v: 기울기(gradient)를 계산할 점의 위치
    :param i: 기울기를 계산할 성분의 인덱스
    :param h: i번째 성분의 변화량
    :return: 편미분 결과 -> i번째 성분 방향의 gradient
    """
    w = [v_j + (h if j == i else 0) for j, v_j in enumerate(v)]
    return (f(w) - f(v)) / h


def estimate_gradient(f, v, h=0.001):
    """
    [df/dx1, df/dx2, ..., df/dxi, ..., df/dxn]

    :param f: f(vector) = float 함수
    :param v: 기울기(gradient)를 구하려는 점의 좌표 [x1, ..., xn]
    :param h: 증분(increment)
    :return: 모든 성분의 gradient들로 이루어진 벡터(리스트)
    """
    return [partial_difference_quotient(f, v, i, h) for i, _ in enumerate(v)]


def gradient_step(v, gradient, step):
    """
    [xi + step * df/dxi]
    :param v: 이동 전 점의 위치
    :param gradient: 점 v에서의 기울기
    :param step: 이동시키는 가중치(학습률)
    :return: 기울기의 방향으로 이동한 점의 위치
    """
    increment = scalar_multiply(step, gradient)
    return add(v, increment)


def f(v):
    return v[0] ** 2 + v[1] ** 2


def g(v):
    return (v[0] - 1) ** 2 + (v[1] + 1) ** 2


if __name__ == '__main__':
    # f([x1, x2]) = x1 ** 2 + x2 ** 2: (0, 0)
    # g([x1, x2]) = (x1 - 1) ** 2 + (x2 + 1) ** 2 의 최솟값: (1, -1)
    init_x1 = random.randint(-10, 11)  # x축 시작값
    init_x2 = random.randint(-10, 11)  # y축 시작값
    v = [init_x1, init_x2]
    print(f'initial v = {v}')
    tolerance = 0.0001
    count = 0

    # f(v)의 최솟값 구하기
    while True:
        count += 1
        gradient = estimate_gradient(f, v)
        v_next = gradient_step(v, gradient, -0.1)
        print(f'{count} [x, y] = {v_next}')
        if distance(v, v_next) < tolerance:
            break
        else:
            v = v_next

    # g(v)의 최솟값 구하기
    count = 0
    while True:
        count += 1
        gradient = estimate_gradient(g, v)
        v_next = gradient_step(v, gradient, -0.1)
        print(f'{count} [x, y] = {v_next}')
        if distance(v, v_next) < tolerance:
            break
        else:
            v = v_next
