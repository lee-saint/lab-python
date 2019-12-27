"""
file open 모드(mode)
    r: read, 읽기 모드
        읽기 모드는 파일이 없으면 FileNotFound
    w: write, 쓰기 모드
        쓰기 모드는 파일이 없으면 새 파일 생성
        파일이 있으면 기존 파일을 열어 줌. 단, 기존 파일 내용이 삭제됨(덮어쓰기/overwrite)
    a: append, 추가 모드
        추가 모드는 파일이 없으면 새로운 파일을 생성
        파일이 있으면 기존 파일의 가장 마지막에 file pointer가 위치
        새로운 내용은 파일 끝에 추가(append)
"""

try:
    with open('NoFile.txt', 'r') as f:
        pass
except FileNotFoundError:
    pass

with open('NewFile.txt', 'w', encoding='utf-8') as f:
    pass

with open('Append.txt', 'a', encoding='utf-8') as f:
    f.write('test\n')

with open('Append.txt', 'a', encoding='utf-8') as f:
    f.write('추가...\n')


