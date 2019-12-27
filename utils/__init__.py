"""
utils.__init__
패키지에 대한 설명과 설정을 담당하는 파일
다른 모듈에서 패키지 이름을 import 했을 때 공개할 모듈 이름들을 설정할 수 있음
"""

# from 패키지 import * 구문에서 공개할 모듈 이름 리스트
__all__ = ['mymath1']

from . import mymath2
