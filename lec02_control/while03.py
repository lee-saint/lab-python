"""
반복문 연습
"""

# 1 + 2 + 3 + ... + 100 = ?
num = [i for i in range(1, 101)]
print(sum(num))

n = 100
print(n * (n + 1) / 2)

# Shift+F6: refactor/rename
# 1 + 2 + 3 + ... + x (<= 100)
total = 0
n = 1
while 1:
    if total + n > 100: break
    total += n
    n += 1
print(total, n - 1)

# 문자 T로 채워진 직각삼각형
for i in range(1, 8):
    for j in range(1, i + 1):
        print('T', end='')
    print()

# 문자 T로 채워진 (빗변이 왼쪽에 있는) 직각삼각형
for i in range(1, 8):
    for j in range(1, 8):
        if j <= 7 - i:
            print(' ', end='')
        else:
            print('T', end='')
    print()


# 위의 것들을 while 루프로
# 문자 T로 채워진 직각삼각형
x = 1
while x < 8:
    y = 1
    while y <= x:
        print('T', end='')
        y += 1
    print()
    x += 1

# 문자 T로 채워진 (빗변이 왼쪽에 있는) 직각삼각형
x = 1
while x < 8:
    y = 1
    while y < 8:
        if y <= 7 - x: print(' ', end='')
        else: print('T', end='')
        y += 1
    print()
    x += 1
