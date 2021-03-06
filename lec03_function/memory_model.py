"""
파이썬 메모리 모델 -
파이썬이 변수들의 메모리 공관을 관리하는 방법
"""

n1 = 1
print(f'주소 = {id(n1)} 저장된 값 = {n1}')

n2 = n1
print(f'주소 = {id(n2)}, 저장된 값 = {n2}')

n2 = 2
print(f'주소 = {id(n2)}, 저장된 값 = {n2}')

n3 = 1
print(f'주소 = {id(n3)}, 저장된 값 = {n3}')
# 정수 / 문자열의 경우 생성된 객체를 캐싱함(재활용)
n3 = 3 - 1  # n2의 주소를 재활용
print(f'주소 = {id(n3)}, 저장된 값 = {n3}')

# 정수, 문자열을 제외한 다른 객체들의 경우 값이 사용할 때마다 새로 생성됨
f1 = 1.2
print(f'주소 = {id(f1)}, 저장된 값 = {f1}')
f2 = 1.2
print(f'주소 = {id(f2)}, 저장된 값 = {f2}')

s1 = 'abc'
print(f'주소 = {id(s1)}, 저장된 값 = {s1}')
s2 = 'abc'
print(f'주소 = {id(s2)}, 저장된 값 = {s2}')

l1 = [1, 2, 3]
print(f'주소 = {id(l1)}, 저장된 값 = {l1}')
l2 = [1, 2, 3]
print(f'주소 = {id(l2)}, 저장된 값 = {l2}')
l2[0] = 100
print(l1)  # list1에는 영향 없음
print(l2)

l3 = l2
print(f'주소 = {id(l3)}, 저장된 값 = {l3}')
l3[1] = 200
print(l2, l3)


# == 연산자 VS is 연산자
a = [1, 2, 3]
b = [1, 2, 3]
print(f'==: {a == b}, is: {a is b}')
print(f'==: {s1 == s2}, is: {s1 is s2}')
