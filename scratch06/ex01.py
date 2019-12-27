"""
scratch06/ex01_namedtuple.py
확률

사건 공간(universe of events)
사건(event)
확률(probability)
"""
import random
from collections import Counter

coin = ['H', 'T']
dice = [1, 2, 3, 4, 5, 6]
print(random.choice(dice))

# 동전 1개를 10,000번 던지는 실험
# 앞면(H)이 나올 확률과 뒷면(T)이 나올 확률이 1/2에 수렴함을 보여라

head = 0
tail = 0
for _ in range(10000):
    r = random.choice(coin)
    if r == 'H':
        head += 1
    else:
        tail += 1
print('event of H: ', head)
print('event of T: ', tail)

# 동전 2개를 10,000번 던지는 실험
# 1) 앞면의 개수가 1개일 확률 1/2
# 2) 첫번째 동전이 앞면일 확률 1/2
# 3) 적어도 한개의 동전이 앞면일 확률 3/4
# = 1 - 두개 동전 모두 뒷면일 확률

one_head = 0
first_head = 0
head_not_zero = 0
trials = 10000

for _ in range(trials):
    r = [random.choice(coin), random.choice(coin)]
    if r.count('H') == 1:
        one_head += 1
    if r[0] == 'H':
        first_head += 1
    if 'H' in r:
        head_not_zero += 1

p_oh = one_head / trials
p_fh = first_head / trials
p_hnz = head_not_zero / trials

print('P(H1) =', p_oh)
print('P(H*) =', p_fh)
print('P(eH) =', p_hnz)


# 동전 3개를 던지는 실험(10,000번)
# 앞면의 개수가 1개일 확률 3/8
one_head = 0

for _ in range(trials):
    r = [random.choice(coin), random.choice(coin), random.choice(coin)]
    if r.count('H') == 1:
        one_head += 1

p_oh = one_head / trials
print('P(H1) =', p_oh)


def experiment(type, n, t):
    """

    :param type: 실험 타입(동전 던지기 or 주사위 던지기, ...)
    :param n: 동전의 개수
    :param t: 실험 회수
    :return: 리스트
    """
    cases = []  # 동전 던지기 실험 결과를 저장
    for _ in range(t):
        case = []  # 각 실험의 결과를 저장
        for _ in range(n):
            rand = random.choice(type)  # 'H' or 'T'
            case.append(rand)  # 1회 실험 결과에 저장
        # 1회 실험이 끝날 때마다 각 결과를 tuple로 변환 후 저장
        # Counter 클래스는 튜플은 셀 수 있지만 리스트는 셀 수 없음!!
        cases.append(tuple(case))
    return cases


coin_exp = experiment(coin, 2, 10000)
print(coin_exp[0:10])

coin_event_counts = Counter(coin_exp)
print(coin_event_counts)


def how_many_head(x):
    counters = Counter(x)
    return counters['H']


num_of_cases = 0
for ev, cnt in coin_event_counts.items():
    if how_many_head(ev) == 1:
        num_of_cases += cnt
p_h1 = num_of_cases / trials
print('P(앞면이 1개일 확률) =', p_h1)

num_of_cases = 0
for ev, cnt in coin_event_counts.items():
    if ev[0] == 'H':
        num_of_cases += cnt
p_first_h = num_of_cases / trials
print('P(첫번째 동전이 앞면) =', p_first_h)

num_of_cases = 0
for ev, cnt in coin_event_counts.items():
    if how_many_head(ev) >= 1:
        num_of_cases += cnt
p_h = num_of_cases / trials
print('P(앞면이 한번은 나올 확률) =', p_h)

# 여사건 이용
num_of_cases = 0
for ev, cnt in coin_event_counts.items():
    if how_many_head(ev) == 0:
        num_of_cases += cnt
p = num_of_cases / trials
print('P(앞면이 한번은 나올 확률) =', 1 - p)

# H = 1, T = 0 약속
coin2 = [1, 0]
cases = []
for _ in range(trials):
    num_of_heads = 0
    for _ in range(2):
        num_of_heads += random.choice(coin2)
    cases.append(num_of_heads)
print(cases[0:10])
coin_event_counts = Counter(cases)
print('P(H=0) =', coin_event_counts[0] / trials)
print('P(H=1) =', coin_event_counts[1] / trials)
print('P(H=2) =', coin_event_counts[2] / trials)

# 주사위 2개를 던졌을 때, 두 눈의 합이 8일 확률 5/36
# 주사위 2개를 던졌을 때, 적어도 하나가 짝수가 나올 확률 27/36 = 3/4
dice_exp = experiment(dice, 2, trials)
print(dice_exp[:5])
sum_8 = 0
all_odd = 0
for exp in dice_exp:
    if sum(exp) == 8:
        sum_8 += 1
    if exp[0] % 2 and exp[1] % 2:
        all_odd += 1
print('P(sum = 8) =', sum_8 / trials)
print(5/36)
print('P(적어도 하나는 짝수) =', 1 - all_odd / trials)

