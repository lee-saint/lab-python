import pandas as pd
import os

from sklearn.metrics import confusion_matrix

from scratch12.ex04 import summarize_by_class, calculate_class_probability


def train_test_split(df, test_size=0.2):
    """df=데이터프레임, test_size=테스트 세트의 비율
    학습 세트(X_train)와 검증 세트(X_test)를 리턴
    train/test set: 리스트 또는 np.ndarray
    [[x1, x2, ..., label1], [x1, x2, ..., label2], [], ...], [[], [], [], ...]
    """
    df_shuffled = df.sample(frac=1)
    cut = int(len(df) * (1 - test_size))
    X_train = df_shuffled[:cut].to_numpy()
    X_test = df_shuffled[cut:].to_numpy()
    X_test_without_label = X_test[:, :-1]
    y_test = X_test[:, -1]
    return X_train, X_test_without_label, y_test


def predict(summaries, X_test):
    """테스트 세트의 예측값들의 배열(리스트)을 리턴
    [0, 1, 1, 2, 0, 0, 2, ...]"""
    # X_test의 원소 개수만큼 반복하면서 각 원소의 클래스에 속할 확률을 계산
    # 각 클래스에 속할 확률 중 최댓값을 찾아 키값을 예측값 리스트에 추가
    prediction = []
    for row in X_test:
        probabilities = calculate_class_probability(summaries, row)
        probabilities_sort = sorted(probabilities.items(), key=lambda x: x[1], reverse=True)
        prediction.append(probabilities_sort[0][0])
    return prediction


if __name__ == '__main__':
    iris_file = os.path.join('..', 'scratch11', 'iris.csv')
    cancer_file = os.path.join('..', 'scratch11', 'wisc_bc_data.csv')

    iris_dataset = pd.read_csv(iris_file, header=None)
    print(iris_dataset.head())

    species = set(iris_dataset.iloc[:, -1])
    print(species)

    # iris 데이터 전처리: class 숫자화
    iris_dataset.loc[iris_dataset[4] == 'Iris-setosa', 4] = 0
    iris_dataset.loc[iris_dataset[4] == 'Iris-versicolor', 4] = 1
    iris_dataset.loc[iris_dataset[4] == 'Iris-virginica', 4] = 2
    print(iris_dataset.head())
    print(iris_dataset.tail())

    # data split
    iris_train, iris_x_test, iris_y_test = train_test_split(iris_dataset, test_size=0.2)
    # print(iris_test[:5])

    # 학습
    iris_summaries = summarize_by_class(iris_train)
    # print(iris_summaries)

    # 예측
    iris_y_pred = predict(iris_summaries, iris_x_test)
    print(iris_y_pred[:5])

    # 평가
    print(confusion_matrix(iris_y_test, iris_y_pred))

    # Cancer data
    cancer_dataset = pd.read_csv(cancer_file)
    print(cancer_dataset.head())

    # 전처리: id 제거, class 숫자화
    ret = cancer_dataset.drop('id', axis=1)
    # 원본 데이터프레임은 그대로 나아있고, 컬럼이 삭제된 새로운 데이터프레임을 리턴
    print(ret.head())

    # del cancer_dataset['id']  # 원본 데이터프레임에서 컬럼을 삭제

    # column_names = ret.columns.tolist()
    # column_names.remove('diagnosis')
    # column_names.append('diagnosis')
    # df = ret.reindex(columns=column_names)

    print(cancer_dataset.loc[:, ::-1].head())

    cancer_dataset.loc[cancer_dataset['diagnosis'] == 'B', 'Class'] = 0
    cancer_dataset.loc[cancer_dataset['diagnosis'] == 'M', 'Class'] = 1
    cancer_noid = cancer_dataset.iloc[:, 2:]
    print(cancer_noid.head(10))

    # data split
    cancer_train, cancer_x_test, cancer_y_test = train_test_split(cancer_noid, test_size=0.2)

    # 학습
    cancer_summaries = summarize_by_class(cancer_train)

    # 예측
    cancer_y_pred = predict(cancer_summaries, cancer_x_test)

    # 평가
    print(confusion_matrix(cancer_y_test, cancer_y_pred))
