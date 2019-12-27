"""
통계

중심 경향성: 평균, 중앙값, 분위수(4분위, 100분위=퍼센트), 최빈값
산포도: 분산(variance), 표준편차(standard deviation), 범위(range)
상관관계: 공분산(covariance), 상관 계수(correlation)
"""
from scratch04.ex01 import sum_of_squares, dot


def mean(x):
    """

    :param x: 원소 n개인 (1차원) 리스트
    :return: 평균
    """
    # sum_ = 0
    # for n in x:
    #     sum_ += n
    return sum(x) / len(x)


def median(x):
    """
    리스트 x를 정렬했을 때 중앙에 있는 값을 찾아서 리턴
    n이 홀수이면 중앙값 / n이 짝수이면 중앙에 있는 두 개 값의 평균을 리턴
    :param x: 원소 n개인 (1차원) 리스트
    :return: 중앙값
    """
    sx = sorted(x)
    return sx[len(x) // 2] if len(x) % 2 else (sx[len(x) // 2] + sx[len(x) // 2 - 1]) / 2


def quantile(x, p):
    """
    리스트 x의 p분위에 속하는 값을 찾아서 리턴
    :param x: 원소 n개인 (1차원) 리스트
    :param p: 퍼센트(0 ~ 1.0 사이의 값)
    :return: 해당 분위수(퍼센트)의 값
    """
    sx = sorted(x)
    idx = int(len(x) * p)
    return sx[idx]


def mode(x):
    """
    리스트에서 가장 자주 나타나는 값을 리턴
    최빈값이 여러개인 경우 최빈값들의 리스트를 리턴
    from collections import Counter
    :param x: 원소가 n개인 (1차원) 리스트
    :return: 최빈값들의 리스트
    """
    from collections import Counter

    c = Counter(x)
    mc = c.most_common()
    # result = []
    # for tup in mc:
    #     if tup[1] == mc[0][1]:
    #         result.append(tup[0])
    # return result
    # return [tup[0] for tup in mc if tup[1] == mc[0][1]]
    max_c = max(c.values())
    return [val for val, cnt in c.items() if cnt == max_c]


def data_range(x):
    """

    :param x: 원소가 n개인 (1차원) 리스트
    :return: 리스트의 최댓값 - 최솟값
    """
    return max(x) - min(x)


def de_mean(x):
    """
    편차(데이터 - 평균)들의 리스트
    :param x: 원소 n개 리스트
    :return: 편차(deviation)의 리스트
    """
    mu = mean(x)
    return [n - mu for n in x]


def variance(x):
    """
    ((x1 - mean) ** 2 + (x2 - mean) ** 2 + ... + (xn - mean) ** 2) / n - 1
    :param x: 원소 n개의 리스트
    :return: 분산
    """
    # return sum([(n - mean(x)) ** 2 for n in x]) / len(x) - 1
    deviations = de_mean(x)
    # return sum([d ** 2 for d in deviations]) / len(x) - 1
    return sum_of_squares(deviations) / len(x) - 1


def standard_deviation(x):
    """
    sqrt(variance)
    :param x: 원소 n개인 (1차원) 리스트
    :return: 표준편차
    """
    from math import sqrt
    return sqrt(variance(x))


def covariance(x, y):
    """
    공분산(Covariance)
    Cov = sum((xi - x_bar)(yi - y_bar)) / (n - 1)
    :param x: 원소가 n개인 리스트
    :param y: 원소가 n개인 리스트
    :return: 공분산
    """
    x_dev = de_mean(x)
    y_dev = de_mean(y)
    cov = dot(x_dev, y_dev) / len(x) - 1
    return cov


def correlation(x, y):
    """
    상관 계수(correlation)
    cor = cov(x, y) / (SD(x) * SD(y))
    :param x: 원소 n개인 리스트
    :param y: 원소 n개인 리스트
    :return: 상관계수
    """
    sdx = standard_deviation(x)
    sdy = standard_deviation(y)
    return covariance(x, y) / (sdx * sdy) if sdx != 0 and sdy != 0 else 0


if __name__ == '__main__':
    x = [1, 2, 3, 4, 5]
    y = [1, 2, 3, 4, 5, 6]
    print('mean(x) =', mean(x))
    print('mean(y) =', mean(y))
    print('median(x) =', median(x))
    print('median(y) =', median(y))
    print('quantile(y, 0.25) =', quantile(y, 0.25))

    test = [2, 2, 3, 3, 4, 4, 4, 6, 6, 6, 100]
    print(mode(test))
    print(mean(test))
    print(data_range(test))
    print(variance(test))
    print(standard_deviation(test))

    t1 = [1, 2, 3, 4, 5]
    t2 = [2, 4, 4, 5, 8]
    print(covariance(t1, t2))
    print(correlation(t1, t2))
