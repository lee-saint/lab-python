import matplotlib.pyplot as plt
import pandas as pd

if __name__ == '__main__':
    column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'Class']
    iris = pd.read_csv('iris.csv', header=None, names=column_names)
    iris_by_class = iris.groupby('Class')

    xy = []  # x축 / y축에 사용할 변수 이름
    for i in range(3):
        for j in range(i+1, 4):
            xy.append((column_names[i], column_names[j]))
    print(xy)

    fig, ax = plt.subplots(2, 3)
    xy_idx = 0
    for row in range(2):
        for col in range(3):
            axis = ax[row, col]  # axis = ax[row][col]
            x = xy[xy_idx][0]  # x축 데이터 이름
            y = xy[xy_idx][1]  # y축 데이터 이름
            xy_idx += 1  # 다음 이름 세트로 이동
            axis.set_title(f'{x} vs {y}')  # subplot의 제목
            axis.set_xlabel(x)  # subplot의 x라벨
            axis.set_ylabel(y)  # subplot의 y라벨
            for name, group in iris_by_class:
                ax[row][col].scatter(group[x], group[y], label=name)
    plt.legend()
    plt.show()
