"""
모듈(module): 파이썬 파일(.py)
    변수, 함수, 클래스들이 정의된 스크립트 파일
패키지(package): 파이썬 모듈들을 관련된 기능들끼리 모아서 저장한 폴더

기본 패키지/모듈 이외의 기능들을 사용할 때 import 구문을 사용함
import 모듈이름
from 모듈이름 import 기능(변수, 함수, 클래스 이름)
from 패키지이름 import 모듈이름
"""

# 파이썬은 여러가지 수학 함수들과 상수들을 정의한 math 모듈이 있음
import math
# math.py 파일 안에 정의된 함수들과 상수들을 사용할 수 있음
print(math.pi)  # 모듈에 정의된 상수(변수) 사용
print(math.sqrt(2))  # 모듈에 정의된 함수 사용

import numpy

