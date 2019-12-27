# open
f = open('test.txt', mode='r', encoding='utf-8')
# read: read(), readline()
# content = f.read()  # 텍스트 문서 전체를 읽음
content = f.read(3)  # read(n): n개의 문자만 읽음
print(content)
content = f.read(3)  # read(n): n개의 문자만 읽음
print(content)
# close
f.close()

f = open('test2.txt', 'r', encoding='utf-8')
# readline(): 파일에서 한줄씩 읽음
# 줄바꿈 문자('\n')까지 읽음!
line = f.readline().strip()
print(f'line: {line}, length: {len(line)}')
line = f.readline().strip()
print(f'line: {line}, length: {len(line)}')
line = f.readline().strip()
print(f'line: {line}, length: {len(line)}')
f.close()

# 무한루프와 readline()을 사용해서 문서 끝까지 읽기
f = open('test2.txt', 'r', encoding='utf-8')
while True:  # 무한루프
    line = f.readline()
    if line == '':  # 파일 끝(EOF: End Of File)에 도달
        break  # 무한루프 종료
    print(line.strip())
f.close()

f = open('test.txt', 'r', encoding='utf-8')
line = f.readline()
while line:
    print(line.strip())
    line = f.readline()

f.close()

with open('test2.txt', mode='r', encoding='utf-8') as f:
    line = f.readline()
    while line:
        print(line.strip())
        line = f.readline()
