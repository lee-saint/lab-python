"""
Boston house price dataset
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures

# 보스턴 집값 데이터 세트 로딩

boston = load_boston()  # Bunch: 파이썬의 dict와 비슷한 타입
print(type(boston))
print(boston.keys())
print(boston['DESCR'])

X = boston.data  # boston['data']
y = boston.target  # boston['target']
print(X.shape)  # (506, 13)
print(y.shape)  # (506, )

features = boston['feature_names']

# 데이터 탐색 - 그래프
fig, ax = plt.subplots(3, 5)
ax_flat = ax.flatten()
for i in range(len(features)):
    ax_flat[i].scatter(X[:, i], y)
    ax_flat[i].set_title(features[i])
plt.show()

# 선형 회귀 - 단순 선형회귀, 다중 선형회귀
# 단순 선형회귀: lstat(마지막 열)
lin_reg = LinearRegression()
lin_reg.fit(X[:, np.newaxis, -1], y)
print(f'coefficients = {lin_reg.coef_}, intercept = {lin_reg.intercept_}')


# 다중 선형회귀
lin_reg2 = LinearRegression()
lin_reg2.fit(X, y)
print(f'coefficients = {lin_reg2.coef_}, intercept = {lin_reg2.intercept_}')


# 검증 세트를 사용해서 예측 -> 그래프
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
print(X_train.shape, X_test.shape)
lin_reg.fit(X_train[:, np.newaxis, -1], y_train)
y_lstat_pred = lin_reg.predict(X_test[:, np.newaxis, -1])
plt.scatter(X_test[:, -1], y_test)
plt.plot(X_test[:, -1], y_lstat_pred, 'ro-')
plt.show()

# Price ~ LSTAT + LASTAT^2 선형회귀
# price = b0 + b1 * lstat + b2 * lstat^2
poly_features = PolynomialFeatures(degree=2, include_bias=False)
# 데이터에 다항식 항들을 컬럼으로 추가해주는 클래스 객체
# 학습 세트에 다항식 항을 추가
X_train_lstat_poly = poly_features.fit_transform(X_train[:, np.newaxis, -1])
X_test_lstat_poly = poly_features.fit_transform(X_test[:, np.newaxis, -1])

lin_reg_poly = LinearRegression()
lin_reg_poly.fit(X_train_lstat_poly, y_train)
print(f'intercept: {lin_reg_poly.intercept_}, coefficients: {lin_reg_poly.coef_}')
y_lstat_poly_pred = lin_reg_poly.predict(X_test_lstat_poly)

plt.scatter(X_test[:, -1], y_test)
xs = np.linspace(X_test[:, -1].min(), X_test[:, -1].max(), 100).reshape((100, 1))
xs_poly = poly_features.fit_transform(xs)
ys = lin_reg_poly.predict(xs_poly)
plt.plot(xs, ys, 'r')

plt.title('Price ~ lstat + lstat^2')
plt.show()

# Price ~ RM + LSTAT 선형회귀: price = b0 + b1 * rm + b2 * lstat
X_train_rm_lstat = X_train[:, [5, 12]]
X_test_rm_lstat = X_test[:, [5, 12]]

lin_reg.fit(X_train_rm_lstat, y_train)
print(f'intercept: {lin_reg.intercept_}, coefficients: {lin_reg.coef_}')

y_pred_rm_lstat = lin_reg.predict(X_test_rm_lstat)
print(y_test[:5], y_pred_rm_lstat[:5])

# Price ~ RM + LSTAT + RM^2 + RM*LSTAT + LSTAT^2
# Price = b0 + b1*rm + b2*lstat + b3*rm^2 + b4*rm*lstat + b5*lstat^2
X_train_rm_lstat_poly = poly_features.fit_transform(X_train_rm_lstat)
X_test_rm_lstat_poly = poly_features.fit_transform(X_test_rm_lstat)

lin_reg.fit(X_train_rm_lstat_poly, y_train)
print(f'intercept: {lin_reg.intercept_}, coefficients: {lin_reg.coef_}')

y_pred_rm_lstat_poly = lin_reg.predict(X_test_rm_lstat_poly)
print(y_test[:5], y_pred_rm_lstat_poly[:5])

# Price ~ RM + LSTAT + LSTAT^2
# Price = b0 + b1*RM + b2*lstat + b3*lstat^2
X_train_lstat_poly_rm = np.c_[X_train[:, -1], X_train_lstat_poly]
X_test_lstat_poly_rm = np.c_[X_test[:, -1], X_test_lstat_poly]

lin_reg.fit(X_train_lstat_poly_rm, y_train)
print(f'intercept: {lin_reg.intercept_}, coefficients: {lin_reg.coef_}')

y_pred_lstat_poly_rm = lin_reg.predict(X_test_lstat_poly_rm)
print(y_test[:5], y_pred_lstat_poly_rm[:5])


# all
lin_reg2.fit(X_train, y_train)
y_pred = lin_reg2.predict(X_test)

# 제곱 선형회귀?!
X_poly_train = poly_features.fit_transform(X_train)
print(X_poly_train.shape)
X_poly_test = poly_features.fit_transform(X_test)
print(X_poly_test.shape)
lin_reg3 = LinearRegression()
lin_reg3.fit(X_poly_train, y_train)
y_poly_pred = lin_reg3.predict(X_poly_test)

# Mean Square Error 계산
print('MSE(lstat) =', np.sqrt(mean_squared_error(y_test, y_lstat_pred)))
print('MSE(lstat^2) =', np.sqrt(mean_squared_error(y_test, y_lstat_poly_pred)))
print('MSE(lstat+rm) =', np.sqrt(mean_squared_error(y_test, y_pred_rm_lstat)))
print('MSE(lstat^2+rm^2) =', np.sqrt(mean_squared_error(y_test, y_pred_rm_lstat_poly)))
print('MSE(lstat^2+rm) =', np.sqrt(mean_squared_error(y_test, y_pred_lstat_poly_rm)))
print('MSE(all) =', np.sqrt(mean_squared_error(y_test, y_pred)))
print('MSE(poly) =', np.sqrt(mean_squared_error(y_test, y_poly_pred)))

# R2-score 계산
print('R2(lstat) =', r2_score(y_test, y_lstat_pred))
print('R2(lstat^2) =', r2_score(y_test, y_lstat_poly_pred))
print('R2(lstat+rm) =', r2_score(y_test, y_pred_rm_lstat))
print('R2(lstat^2+rm^2) =', r2_score(y_test, y_pred_rm_lstat_poly))
print('R2(lstat^2+rm) =', r2_score(y_test, y_pred_lstat_poly_rm))
print('R2(all) =', r2_score(y_test, y_pred))
print('R2(poly) =', r2_score(y_test, y_poly_pred))

