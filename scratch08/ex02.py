"""
gradient descent 연습
"""
import matplotlib.pyplot as plt
from scratch08.ex01 import difference_quotient, tangent, move


def g(x):
    """y = (1/3)x**3 - x"""
    return x ** 3 / 3 - x


if __name__ == '__main__':
    # ex01에서 작성한 함수를 이용, 함수 g(x)의 그래프를 그림
    # 극값(local 최소/최대)를 경사 하강법으로 찾음
    xs = [x / 10 for x in range(-30, 31)]
    ys = [g(x) for x in xs]

    plt.plot(xs, ys)
    plt.axhline(y=0, color='0.3')
    plt.axvline(x=0, color='0.3')
    plt.axvline(x=-1, color='0.75')
    plt.axvline(x=1, color='0.75')
    plt.ylim(bottom=-2, top=2)

    x_init = 1.9
    tolerance = 0.00001
    count = 0
    while True:
        count += 1
        gradient = difference_quotient(g, x_init, 0.0001)
        x_next = move(x_init, gradient, -0.1)
        print(f'{count} x: {x_next}')
        # ys_next = [tangent(x, gradient, x_next, g(x_next)) for x in xs]
        # plt.plot(xs, ys_next)
        if abs(x_init - x_next) < tolerance:
            break
        else:
            x_init = x_next

    x_init = -1.9
    count = 0
    while True:
        count += 1
        gradient = difference_quotient(g, x_init, 0.0001)
        x_next = move(x_init, gradient, 0.1)
        print(f'{count} x: {x_next}')
        # ys_next = [tangent(x, gradient, x_next, g(x_next)) for x in xs]
        # plt.plot(xs, ys_next)
        if abs(x_init - x_next) < tolerance:
            break
        else:
            x_init = x_next

    plt.show()
