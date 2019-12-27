"""
scikit-learn 패키지에 포함된 위스콘신 대학 암 데이터를 로딩해서 Gaussian Naive Bayes 모델로 예측 결과를 분석
"""
from sklearn import datasets
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler

if __name__ == '__main__':
    # 데이터 불러오기
    X, y = datasets.load_breast_cancer(return_X_y=True)
    print(X, y)

    # train/test 세트 나누기
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # 정규화
    scaler = StandardScaler()
    scaler.fit(X_train, y_train)
    X_train_tf = scaler.transform(X_train)
    X_test_tf = scaler.transform(X_test)

    # 모델 학습, 예측
    gnb = GaussianNB()
    gnb.fit(X_train_tf, y_train)
    y_pred = gnb.predict(X_test_tf)

    # 성능 평가
    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))
