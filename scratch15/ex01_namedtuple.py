# 번호, 이름, 수학점수, 과학점수, 컴퓨터점수
from collections import namedtuple
from typing import NamedTuple

student_1 = (1, '홍길동', 10, 20, 30)
print('번호:', student_1[0])
print('과학점수:', student_1[3])

# 튜플(tuple) 타입의 단점:
#   - 해당 인덱스의 원소의 의미를 파악하기 어려움
#   - 특정 원소에 접근(read/write)하기 위해서는 정수 인덱스만 사용해야 함

stu_dict = {'no': 2,
            'name': '김길동',
            'math': 90,
            'science': 50,
            'computer': 100}


# 튜플의 단점을 해결하기 튜플과 딕셔너리(dict)의 특징을 모두 갖는 NamedTuple 클래스가 만들어짐

Student = namedtuple('Student', ('no', 'name', 'math', 'science', 'cs'))
student_2 = Student(3, '허균', 100, 100, 10)
print(student_2)
print(f'번호: {student_2[0]}, {student_2.no}')
print(f'수학 점수: {student_2[2]}, {student_2.math}')


# Python 3.6부터 NameTuple을 class처럼 선언하는 방밥이 만들어짐
class Student2(NamedTuple):  # Student2 클래슨느 NamedTuple Class 상속
    # field 선언 - 변수 타입 annotation을 반드시 추가해야 함
    no: int
    name: str
    math: int
    science: int
    cs: int


student_3 = Student2(4, 'abc', 90, 88, 79)
print(student_3)
