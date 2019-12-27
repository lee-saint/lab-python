"""
1) R의 ggplot2 패키지에 포함된 mpg 데이터 프레임을 csv 파일 형식으로 저장
2) 저장된 csv 파일을 파이썬 프로젝트의 scratch08 폴더에 복사
3) 저장된 csv 파일을 읽어서 배기량(displ)과 시내 연비(cty) 데이터를 추출
4) 선형 회귀식
    cty = slope * displ + intersect
의 기울기(slope)와 절편(intersect)을 경사 하강법의 3가지 방법(stochastic, batch, mini-batch)으로 결정하고 값을 비교
5) 배기량과 시내 연비 산점도 그래프(scatter plot)과 선형 회귀 직선을 하나의 plot으로 출력해서 결과 확인
"""
import random
import matplotlib.pyplot as plt
from lec07_file.file07 import my_csv_reader
from scratch04.ex01 import vector_mean
from scratch04.ex03 import get_column
from scratch08.ex03 import gradient_step
from scratch08.ex04 import linear_gradient, minibatches

mpg = my_csv_reader('mpg.csv')
displ = list(map(float, get_column(mpg, 3)))
cty = list(map(float, get_column(mpg, 8)))
displ_cty = [(x, y) for x, y in zip(displ, cty)]

plt.scatter(displ, cty)

xs = [i / 10 for i in range(0, 81)]  # x값 초기화

# stochastic gradient descent
print('===확률적 경사 하강법===')
theta = [-1, 1]  # 초기값
step = 0.005
for epoch in range(200):
    random.shuffle(displ_cty)
    for dis, cty in displ_cty:
        gradient = linear_gradient(dis, cty, theta)
        theta = gradient_step(theta, gradient, -step)
    if (epoch + 1) % 10 == 0:
        print(f'{epoch}: {theta}')

sgd_ys = [theta[0] * x + theta[1] for x in xs]
plt.plot(xs, sgd_ys, label='Stochastic GD')

# batch gradient descent
print('\n=== 배치 경사 하강법 ===')
theta = [-1, 1]  # 초기값
step = 0.005
for epoch in range(10000):
    gradients = [linear_gradient(x, y, theta) for x, y in displ_cty]
    gradient = vector_mean(gradients)
    theta = gradient_step(theta, gradient, -step)
    if (epoch + 1) % 500 == 0:
        print(f'{epoch}: {theta}')

bgd_ys = [theta[0] * x + theta[1] for x in xs]
plt.plot(xs, bgd_ys, label='Batch GD')

# mini-batch gradient descent
print('\n=== 미니 배치 경사 하강법 ===')
theta = [-1, 1]  # 초기값
step = 0.005
for epoch in range(1000):
    mini_batches = minibatches(displ_cty, 20)
    for batch in mini_batches:
        gradients = [linear_gradient(x, y, theta) for x, y in displ_cty]
        gradient = vector_mean(gradients)
        theta = gradient_step(theta, gradient, -step)
    if (epoch + 1) % 100 == 0:
        print(f'{epoch}: {theta}')

mbgd_ys = [theta[0] * x + theta[1] for x in xs]
plt.plot(xs, mbgd_ys, label='Mini-Batch GD')

plt.legend()
plt.xlim(1, 7)
plt.title('displ vs cty')
plt.xlabel('displ')
plt.ylabel('cty')

plt.show()
