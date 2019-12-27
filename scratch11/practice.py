from collections import Counter

import numpy as np
import pandas as pd


def my_train_test_split(X, y, test_size=0.2):
    indices = np.array([i for i in range(len(X))])
    np.random.shuffle(indices)
    cut = int(len(X) * (1 - test_size))
    X_train = X[indices[:cut]]
    X_test = X[indices[cut:]]
    y_train = y[indices[:cut]]
    y_test = y[indices[cut:]]
    return X_train, X_test, y_train, y_test


class MyStandardScaler:
    def fit(self, X):  # 컬럼별 평균, 표준편차 저장
        self.mean = np.mean(X, axis=0)
        self.std = np.std(X, axis=0)

    def transform(self, X):
        X_transformed = np.array([[(X[i][j] - self.mean[j]) / self.std[j] for j in range(len(X[0]))] for i in range(len(X))])
        return X_transformed


class MySecondKnnClassifier:
    def __init__(self, k_neighbors=5):
        self.k = k_neighbors

    def fit(self, X_train, y_train):
        self.points = X_train
        self.labels = y_train

    def predict(self, X_test):
        pdtion = []
        for point in X_test:
            distances = [(self.distance(p, point), label) for p, label in zip(self.points, self.labels)]
            distances.sort(key=lambda x: x[0])
            print(distances)
            closest = [x[1] for x in distances[:self.k]]
            print(closest)
            most_vote = Counter(closest).most_common(1)
            print(most_vote)
            pdtion.append(most_vote[0][0])
        return pdtion

    def distance(self, p1, p2):
        return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


if __name__ == '__main__':
    X = np.random.randint(10, size=(5, 2))
    print(X)
    y = np.array(['a', 'b', 'a', 'b', 'a'])

    X_train, X_test, y_train, y_test = my_train_test_split(X, y, test_size=0.2)

    scaler = MyStandardScaler()
    scaler.fit(X_train)
    X_train_tf = scaler.transform(X_train)
    X_test_tf = scaler.transform(X_test)
    print(X_train_tf)
    print(X_test_tf)

    knn = MySecondKnnClassifier(k_neighbors=3)
    knn.fit(X_train_tf, y_train)
    y_pred = knn.predict(X_test_tf)
    print(y_pred)


    # print(np.mean(X_train_tf, axis=0))
    # print(np.std(X_train_tf, axis=0))

    # iris = pd.read_csv('iris.csv', header=None)
    # print(iris.head())
    #
    # X = iris.iloc[:, :-1].to_numpy()
    # y = iris.iloc[:, -1].to_numpy()
    #
    # X_train, X_test, y_train, y_test = my_train_test_split(X, y, test_size=0.2)
    # print(len(X_train), len(X_test), len(y_train), len(y_test))
    #
    # scaler = MyStandardScaler()
    # scaler.fit(X_train)
    # X_train_tf = scaler.transform(X_train)
    # X_test_tf = scaler.transform(X_test)


