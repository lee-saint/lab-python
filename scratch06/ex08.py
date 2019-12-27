"""
scipy 패키지의 stats 모듈에서 제공하는 확률밀도함수(PDF: Probability Density Function), 누적분포함수(CDF: Cumulative Distribution Function)
"""
from scipy import stats
import matplotlib.pyplot as plt

xs = [x / 10 for x in range(-30, 31)]  # 그래프를 그릴 x 구간
# 균등 분포(uniform distribution) 확률밀도함수
ys1 = [stats.uniform.pdf(x) for x in xs]
# 균등 분포 누적 분포 함수(CDF)
ys2 = [stats.uniform.cdf(x) for x in xs]

plt.plot(xs, ys1, color='b', label='PDF')
plt.plot(xs, ys2, color='r', label='CDF')
plt.legend()
plt.show()

# 정규분포(Normal Distribution) 확률 밀도 함수
ys1 = [stats.norm.pdf(x) for x in xs]
# 표준 정규분표 누적분포함수(CDF)
ys2 = [stats.norm.cdf(x) for x in xs]

plt.plot(xs, ys1, label='PDF')
plt.plot(xs, ys2, label='CDF')
plt.legend()
plt.title('Standard Normal Distribution PDF & CDF')
plt.show()

