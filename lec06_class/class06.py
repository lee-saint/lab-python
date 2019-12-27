from math import pi


class Circle:
    # field: 반지름(radius)
    # method:
    #   __init__: 초기화(객체 생성) 함수
    #   area(): 원의 넓이를 리턴
    #   perimeter(): 원의 둘레 길이를 리턴
    #   __str__(): Circle(r=123) 형식
    #   __eq__(): 반지름 같은면 equal(Tru)
    def __init__(self, radius):
        self.radius = radius
        if self.radius < 0:
            raise ValueError('반지름은 0 또는 양수')

    def area(self):
        return pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * pi * self.radius

    def __str__(self):
        return f'Circle(r={self.radius})'

    # representation
    def __repr__(self):
        return f'원({self.radius})'

    def __eq__(self, other):  # equal
        print('__eq__ 호출')
        return self.radius == other.radius

    def __ne__(self, other):  # not equal
        # != 연산자를 사용하면 자동으로 호출되는 메소드
        print('__ne__ 호출')
        return self.radius != other.radius

    def __gt__(self, other):
        # greater than: > 연산자를 사용하면 자동으로 호출
        print('__gt__ 호출')
        return self.radius > other.radius

    def __ge__(self, other):
        # greater than or equal to
        # >= 연산자를 사용하면 자동으로 호출되는 메소드
        return self.__gt__(other) or self.__eq__(other)

    # __lt__: less than(<)
    # __le__: less than or equal to


if __name__ == '__main__':
    cc1 = Circle(5)
    print(cc1)
    print('cc1 id:', id(cc1))
    print('cc1 area:', cc1.area())
    print('cc1 perimeter', cc1.perimeter())

    cc2 = Circle(3)
    print(cc1 == cc2)

    cc3 = Circle(5)
    print('cc3 id:', id(cc3))
    print(cc1 == cc3)  # c1.__eq__(c2)
    print(cc1 != cc3)
    # __eq__ 메소드만 작성한 경우, != 연산자는 __eq__ 메소드를 호출한 후 그 결과값의 반대(not)를 사용
    # __ne__ 메소드가 있는 경우, != 연산자는 __ne__ 메소드의 리턴값을 사용

    print(cc1 > cc3)
    print(cc1 >= cc3)
    print(cc1 < cc3)
    print(cc1 <= cc3)

    circles = [
        Circle(10),
        Circle(7),
        Circle(100),
        Circle(50),
        Circle(0)
    ]
    print(circles)
    print(sorted(circles))



