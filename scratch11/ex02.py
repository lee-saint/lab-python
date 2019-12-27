"""
R을 활용한 머신러닝 - 암 데이터 파일(csv)
scikit-learn 패키지 활용, kNN 결과
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

if __name__ == '__main__':
    # 데이터 불러오기
    bc = pd.read_csv('wisc_bc_data.csv')
    print(bc.info())
    print(bc.describe())
    print(bc.head())

    # 데이터 전처리: train/test 셋 구분
    X = bc.iloc[:, 2:].to_numpy()
    y = bc.iloc[:, 1].to_numpy()

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    print(len(X_train), len(X_test), len(y_train), len(y_test))

    # 표준화
    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)

    # 학습/예측
    classifier = KNeighborsClassifier(n_neighbors=5)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)

    # 모델 평가
    conf_matrix = confusion_matrix(y_test, y_pred)
    print(conf_matrix)
    report = classification_report(y_test, y_pred)
    print(report)

    errors = []
    for i in range(1, 41):
        knn = KNeighborsClassifier(n_neighbors=i)
        knn.fit(X_train, y_train)
        pred_i = knn.predict(X_test)
        errors.append(np.mean(pred_i != y_test))

    plt.plot(range(1, 41), errors, marker='o')
    plt.show()
