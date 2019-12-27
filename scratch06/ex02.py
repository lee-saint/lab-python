"""
사건의 종속성 vs 독립성
사건 A의 발생 여부가 사건 B의 발생 여부에 대한 정보를 제공한다면,
사건 A와 사건 B는 종속사건(dependent event)이다.
사건 A의 발생 여부가 사건 B의 발생 여부와 상관이 없다면,
사건 A와 B는 독립사건(independent event)이다.

동전 2개를 던지는 경우,
A: 첫번째 동전이 앞면
B: 두번째 동전이 뒷면
C: 두 동전 모두 뒷면(앞면)
A와 B는 독립사건, A와 C는 종속사건

P(A): 사건 A가 발생할 확률
P(B): 사건 B가 일어날 확률
P(A, B): 사건 A와 사건 B의 교집합이 일어날 확률

P(A, B) = P(A) * P(B)가 성립하면 두 사건은 독립사건
"""

# 자녀가 2명인 경우,
# A: 첫째가 딸인 경우
# B: 둘째가 아들인 경우
# C: 둘 다 딸인 경우
# A와 B가 독립사건, A와 C는 종속사건임을 증명
# P(A), P(B), P(C), P(A, B), P(A, C)
from collections import Counter
from scratch06.ex01 import experiment

child = ['M', 'F']
trials = 10000
children = experiment(child, 2, trials)
cdr_counter = Counter(children)
print(cdr_counter)

case_a = 0
case_b = 0
case_c = 0
case_ab = 0
case_ac = 0
for c, v in cdr_counter.items():
    if c[0] == 'F':
        case_a += v
        if c[1] == 'M':
            case_ab += v
        if c[1] == 'F':
            case_ac += v
    if c[1] == 'M':
        case_b += v
    if c[0] == 'F' and c[1] == 'F':
        case_c += v
print('P(A) =', case_a / trials)
print('P(B) =', case_b / trials)
print('P(C) =', case_c / trials)
print('P(A, B) =', case_ab / trials)
print('P(A) x P(B) =', case_a / trials * case_b / trials)
print('P(A, C) =', case_ac / trials)
print('P(A) x P(C) =', case_a / trials * case_c / trials)


