import numpy as np
from numpy import random as rd
from math import sqrt
rd.seed(666)

# 빈 리스트(scores)를 선언
scores = []

# 난수(0 <= x <= 100) 10개를 리스트에 저장
for _ in range(10):
    scores.append(rd.randint(0, 101))
print(scores)

# 리스트에 저장된 시험 점수 10개의 총점을 계산, 출력
sum_scores = 0
for score in scores:
    sum_scores += score
print(f'총점: {sum_scores}')
print(f'총점2: {sum(scores)}')

# 리스트에 저장된 시험 점수 10개의 평균을 계산, 출력
avg_scores = sum_scores / len(scores)
print(f'평균: {avg_scores}')
print(f'평균2: {np.mean(scores)}')

# 표준편차 계산: from math import sqrt
sum_sq = 0
for score in scores:
    sum_sq += (score - avg_scores) ** 2
std = sqrt(sum_sq / len(scores))
print(f'표준편차: {std}')
print(f'표준편차2: {np.std(scores)}')

# 리스트에 저장된 시험 점수 10개 중에서 최댓값, 최솟값을 찾아서 출력
max_score = 0
min_score = 100
for score in scores:
    if score > max_score: max_score = score
    if score < min_score: min_score = score
print(f'최대 점수: {max_score}, 최소 점수: {min_score}')

sorted_scores = sorted(scores)
print(sorted_scores)
print(scores)
