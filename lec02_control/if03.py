"""
가위/바위/보
"""
import numpy as np

print("가위 바위 보 게임")
print('[1] 가위')
print('[2] 바위')
print('[3] 보')
print('----------------')
print('선택>>')

user = int(input())

computer = np.random.randint(1, 4)  # 1 <= com < 4 난수

rcp = {1: '가위', 2: '바위', 3:'보'}

# user == computer -> 비김
# user - computer == 1 or -2 -> user 승리
if user == computer:
    print(f'당신: {rcp[user]}, 컴퓨터: {rcp[computer]} - 비겼습니다.')
elif user - computer in [1, -2]:
    print(f'당신: {rcp[user]}, 컴퓨터: {rcp[computer]} - 당신의 승리입니다.')
else:
    print(f'당신: {rcp[user]}, 컴퓨터: {rcp[computer]} - 컴퓨터의 승리입니다.')

