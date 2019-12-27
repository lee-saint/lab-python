from scratch11.ex03 import train_test_split, MyScaler, MyKnnClassifier

import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt


if __name__ == '__main__':
    col_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'Class']
    iris = pd.read_csv('iris.csv', header=None, names=col_names)
    print(iris.head())

    # 데이터프레임을 이용해서 각 특성(변수)들과 Class(레이블)과의 관계 그래프프
    iris_by_class = iris.groupby('Class')
    for name, group in iris_by_class:
        # print(name, len(group))
        plt.scatter(group['petal_width'], group['petal_length'], label=name)
    plt.legend()
    plt.xlabel('petal_width')
    plt.ylabel('petal_length')
    plt.show()

    # 데이터세트를 points와 labels로 구분
    X = iris.iloc[:, :-1].to_numpy()  # points
    y = iris.iloc[:, -1].to_numpy()  # labels

    # 학습/검증(train/test) 세트로 분리
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Scaling
    scaler = MyScaler()  # 생성자 호출
    scaler.fit(X_train)  # 스케일링을 위한 평균과 표준편차 계산
    X_train = scaler.transform(X_train)  # 데이터 변환
    X_test = scaler.transform(X_test)

    # k-NN 알고리즘 적용
    knn = MyKnnClassifier(n_neighbors=5)  # 분류기 객체 생성
    knn.fit(X_train, y_train)  # 학습
    y_pred = knn.predict(X_test)  # 예측
    print(np.mean(y_pred == y_test))  # 예측 결과 확인

    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))

    #####################################################
    # 유방암 데이터 세트
    bc = pd.read_csv('wisc_bc_data.csv')
    print(bc.head())

    # 데이터세트를 points와 labels로 구분
    X = bc.iloc[:, 2:].to_numpy()  # points
    y = bc.iloc[:, 1].to_numpy()  # labels

    # 학습/검증(train/test) 세트로 분리
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Scaling
    scaler = MyScaler()  # 생성자 호출
    scaler.fit(X_train)  # 스케일링을 위한 평균과 표준편차 계산
    X_train = scaler.transform(X_train)  # 데이터 변환
    X_test = scaler.transform(X_test)

    # k-NN 알고리즘 적용
    knn = MyKnnClassifier(n_neighbors=5)  # 분류기 객체 생성
    knn.fit(X_train, y_train)  # 학습
    y_pred = knn.predict(X_test)  # 예측
    print(np.mean(y_pred == y_test))  # 예측 결과 확인

    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))
