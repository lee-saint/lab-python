"""
for-in 구문 연습
"""
from math import sqrt

# 피보나치 수열(fibonacci sequence)
# f[0] = 0, f[1] = 1
# f[n] = f[n-1] + f[n-2], n >= 2
# 피보나치 수열 원소 20개짜리 리스트를 생성

fib = [0, 1]
for i in range(18):
    fib.append(fib[i] + fib[i + 1])
print(fib)


def fibo(x):
    if x == 0: return 0
    elif x == 1: return 1
    else: return fibo(x-1) + fibo(x-2)


f = []
for i in range(20):
    f.append(fibo(i))
print(f)


# 소수(prime number): 1과 자기자신만으로 나누어지는 정수
# 2부터 10까지의 정수 중에서 소수를 찾아서 출력

pnum = []
for i in range(2, 100):
    p = True
    for j in range(2, int(sqrt(i)) + 1):
        if i % j == 0:
            p = False
            break
    if p: pnum.append(i)
print(pnum)

# for/while 반복문과 else가 함께 사용되는 경우,
# 반복문이 break를 만나지 않고 범위 전체를 반복했을 때 else 블록이 실행
# 반복문 중간에 break를 만나게 되면 else는 실행되지 않음

for i in range(5):
    if i == 3: continue
    print(i, end=' ')
else:
    print('모든 반복을 끝냄')
print()

# for-else 구문을 사용한 소수 찾기
for n in range(2, 11):
    for divider in range(2, int(sqrt(n)) + 1):
        if n % divider == 0: break              # 약수가 존재: 소수가 아님
    else: print(f'{n}은 소수!')                 # break를 만나지 않았을 때: 약수가 없음 -> 소수
