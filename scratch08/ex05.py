"""
mpg.csv 파일을 읽고, 경사 하강법을 사용해서 선형 회귀식 찾기
cty = slope * displ + intersect
"""
import random
import matplotlib.pyplot as plt
from scratch04.ex01 import vector_mean
from scratch08.ex03 import gradient_step
from scratch08.ex04 import minibatches, linear_gradient

with open('mpg.csv', encoding='UTF-8') as f:
    # 파일 사용(read, write)이 모두 끝났을 때 close() 자동 호출
    f.readline()  # 첫번째 라인을 읽고 버림 - 컬럼 이름들
    # 한줄씩 읽어서
    # 그 줄의 앞뒤 공백들(줄바꿈, \n)을 제거하고
    # ','로 문자열을 분리해서 만든 리스트를 df에 저장
    df = [line.strip().split(',') for line in f]

print(df[0:5])
# 배기량(displ)과 시내 연비(cty)만 추출 - 데이터 타입: 숫자
displ = [float(row[2]) for row in df]
cty = [float(row[7]) for row in df]
displ_cty = [(d, c) for d, c in zip(displ,cty)]
print(displ_cty[:5])


def mini_batch_gd(dataset,
                  epochs=5000,
                  learning_rate=0.001,
                  batch_size=1,
                  shuffle=True):
    dataset = dataset.copy()  # 원본 데이터를 복사해서 사용
    # 찾으려고 하는 직선의 기울기와 절편의 초기값
    theta = [random.randint(-10, 10), random.randint(-10, 10)]
    print('theta 초기값:', theta)
    for epoch in range(epochs):  # epochs 횟수만큼 반복
        if shuffle:
            random.shuffle(dataset)
        mini_batch = minibatches(dataset, batch_size, shuffle)
        for batch in mini_batch:  # 미니 배치 크기만큼 반복
            # 미니 배치 안의 점들에 대해서 gradient들을 계산
            gradients = [linear_gradient(x, y, theta) for x, y in batch]
            # gradient들의 평균울 계산
            gradient = vector_mean(gradients)
            theta = gradient_step(theta, gradient, -learning_rate)
    return theta


print("=== stochastic gradient descent ===")
theta_stochastic = mini_batch_gd(displ_cty, epochs=200, shuffle=False)
print(theta_stochastic)

print("=== batch gradient descent ===")
theta_batch = mini_batch_gd(displ_cty, epochs=5000, batch_size=len(displ_cty), learning_rate=0.01, shuffle=True)
print(theta_batch)

# 미니 배치 경사 하강법
print("=== mini batch gradient descent ===")
theta_mini = mini_batch_gd(displ_cty, epochs=1000, learning_rate=0.01, batch_size=32, shuffle=True)
print(theta_mini)


def linear_regression(x, theta):
    slope, intersect = theta
    return slope * x + intersect  # y = ax + b


plt.scatter(displ, cty)

ys_stochastic = [linear_regression(x, theta_stochastic) for x in displ]
plt.plot(displ, ys_stochastic, color='red', label='Stochastic GD')

ys_batch = [linear_regression(x, theta_batch) for x in displ]
plt.plot(displ, ys_batch, color='green', label='Batch GD')

ys_mini = [linear_regression(x, theta_mini) for x in displ]
plt.plot(displ, ys_mini, color='yellow', label='Mini-Batch GD')

plt.xlabel('displacement(cc)')
plt.ylabel('efficiency(mpg)')
plt.title('Fuel Efficiency vs Displacement')
plt.legend()
plt.show()
