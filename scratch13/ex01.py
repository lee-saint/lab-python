from sklearn import linear_model
from sklearn.datasets import load_diabetes
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    # X, y = load_diabetes(return_X_y=True)
    # print(X[:5])
    # print(X.shape)

    datasets = load_diabetes()
    X = datasets.data
    y = datasets.target
    print(X.shape, y.shape)
    features = datasets.feature_names
    print(features)
    print(X[0])
    # 모든 특성(컬럼)들이 평균=0, 표준편차=1로 전처리되어 있는 데이터세트
    print(y[0])

    # 선형 회귀(linear regression)
    # y = b + a * x

    # 1개 figure에 10개의 subplot을 그림

    fig, axes = plt.subplots(2, 5)
    ax_flat = axes.flatten()
    for i in range(10):
        ax = ax_flat[i]
        ax.scatter(X[:, i], y)
        ax.set_xlabel(datasets.feature_names[i])

    plt.show()

    # y = b + a * bmi: y와 bmi 간의 선형 관계식
    bmi = X[:, np.newaxis, 2]  # data에서 'bmi' 컬럼만 선택
    # scikit-learn의 LinearRegression은 훈련 데이터 세트가 반드시 2차원 배열이어야 함
    print('bmi.shape:', bmi.shape)
    print('bmi[5] =', bmi[:5])

    # bmi를 학습(training)/검증(test) 세트로 분리
    bmi_train = bmi[:-40]
    bmi_test = bmi[-40:]
    y_train = y[:-40]
    y_test = y[-40:]

    # 선형 회귀 모델(linear regression model) 객체 생성
    regr = linear_model.LinearRegression()

    # training set를 학습(fit)
    # y = b + a * bmi 선형 관계식에서 y절편 b와 기울기 a를 결정
    regr.fit(bmi_train, y_train)
    print('coefficients:', regr.coef_)

    # 검증 세트로 테스트
    y_pred = regr.predict(bmi_test)

    plt.scatter(bmi_test, y_test)  # 실제값
    plt.plot(bmi_test, y_pred, 'ro-')  # 예측값
    plt.show()

    # y ~ s5 선형 관계식 찾고 그래프 그리기
    s5 = X[:, np.newaxis, -2]
    print('s5.shape:', s5.shape)
    print('s5[:5] =', s5[:5])

    s5_train = s5[:-40]
    s5_test = s5[-40:]

    regr.fit(s5_train, y_train)
    print('coefficients:', regr.coef_)

    y_pred = regr.predict(s5_test)

    plt.scatter(s5_test, y_test)
    plt.plot(s5_test, y_pred, 'ro-')
    plt.show()
