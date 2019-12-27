"""
csv 모듈을 사용한 mpg.csv 파일 열기
"""
import csv
import os

file_path = os.path.join('..', 'scratch08', 'mpg.csv')
with open(file_path, mode='r', encoding='UTF-8') as f:
    reader = csv.reader(f)
    reader.__next__()  # 한 줄 읽고 건너뜀(첫번째 줄은 컬럼 이름이니까)
    df = [line for line in reader]

print(df[0:5])  # 리스트 df에서 인덱스 0 ~ 4까지 행을 출력
# 리스트 df에서 0번째 행의 0, 1, 2번째 컬럼 아이템만 출력
print(df[0][0], df[0][1], df[0][2])

displ = [row[2] for row in df]
print(displ)

with open(file_path, mode='r', encoding='UTF-8') as f:
    # 사전(dict) 타입으로 데이터를 읽어주는 reader 객체
    reader = csv.DictReader(f)
    df = [row for row in reader]

print(df[0:5])
print(df[0])
# 각 행의 특정 원소를 찾아갈 때, 인덱스가 아닌 컬럼 이름으로 찾을 수 있다.
print(df[0]['manufacturer'])
print(df[0]['model'])
print(df[0]['displ'])
displ = [float(row['displ']) for row in df]
print(displ)
