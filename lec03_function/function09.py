"""
재귀 함수(recursive function)
"""

# factorial
# 0! = 1
# n! = 1 x 2 x 3 x ... x (n-1) x n


def factorial1(n: int) -> int:
    result = 1
    for x in range(1, n+1):
        result *= x
    return result


def factorial2(n: int) -> int:
    if n == 0:
        return 1
    elif n > 0:
        return factorial2(n-1) * n


for x in range(6):
    print(f'{x}! = {factorial2(x)}')


"""
하노이의 탑: hanoi(n, from, to)
n = 1
hanoi(1, 1, 3)

n = 2
hanoi(2, 1, 3)
-> hanoi(1, 1, 2) / 2번 이동 / hanoi(1, 2, 3)
"""


def hanoi(n, _from, _to):
    if n == 1:
        print(f'1, {_from} -> {_to}')
    else:
        # 경유지 찾기: 스테이션 목록에서 출발지와 목적지를 제외한 나머지가 경유지임
        stops = [1, 2, 3]
        stops.remove(_from)
        stops.remove(_to)
        stop = stops[0]
        # n-1개의 원반을 출발지에서 경유지로
        hanoi(n-1, _from, stop)
        # 마지막 원반을 출발지에서 도착지로
        print(f'{n}, {_from} -> {_to}')
        # n-1개의 원반을 경유지에서 도착지로
        hanoi(n-1, stop, _to)


for i in range(1, 6):
    hanoi(i, 1, 3)
    print('-----------------')


def hanoi_tower(n, start, target, aux):
    """
    재귀 함수를 사용해서 하노이 탑 문제 해결 방법 출력
    :param n: 옮길 원반 개수(양의 정수)
    :param start: 원반들이 있는 시작 기둥 번호
    :param target: 원반들을 모두 옮겨 놓을 타겟 기둥 번호
    :param aux: 보조 기둥으로 사용할 기둥 번호
    :return: None
    """
    if n == 1:
        print(f'{start} -> {target}')
        return  # 함수 종료

    # (n-1)개의 원반을 target을 보조 기둥으로 사용해서 aux 기둥으로 모두 옮김
    hanoi_tower(n - 1, start, aux, target)
    # 시작 기둥에 남아 있는 한 개의 원반을 목표 기둥으로 옮김
    print(f'{start} -> {target}')
    # aux 기둥에 남아있는 (n-1)개의 원반을 start 기둥을 보조 기둥으로 사용해서 target으로 옮김
    hanoi_tower(n - 1, aux, target, start)


# 원반 한개짜리 하노이 탑
hanoi_tower(1, 1, 3, 2)
