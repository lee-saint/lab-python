def test():
    print('test')


def test(param=0):
    print('test param =', param)


test()

# overloading: 함수(메소드)의 파라미터가 다른 경우 같은 이름으로 여러 개의 함수(메소드)를 정의하는 것
# 파이썬은 overloading을 제공하지 않음!!
