"""
선택정렬 알고리즘
"""
import numpy as np


def find_min(numbers):
    """
    w두러이
    :param numbers:
    :return:
    """
    min_id, min_value = 0, numbers[0]
    for i, v in enumerate(numbers):
        if v < min_value:
            min_id, min_value = i, v
    return min_id, min_value


def find_max(numbers):
    """

    :param numbers:
    :return:
    """
    max_id, max_value = 0, numbers[0]
    for i, v in enumerate(numbers):
        if v > max_value:
            max_id, max_value = i, v
    return max_id, max_value


def sel_sort(numbers: list, reverse: bool = False):
    """
    주어진 리스트의 원소들이 정렬된 새로운 리스트를 생성해서 리턴
    주어진 리스트(파라미터에 전달된 리스트)의 순서는 변하지 않음
    :param numbers:
    :param reverse: False인 경우는 오름차순, True인 경우는 내림차순
    기본값은 False(오름차순 정렬이 기본값)
    :return:
    """
    numbers_copy = numbers.copy()
    result = []  # 빈 리스트 생성
    while numbers_copy:  # numbers의 원소가 있는 동안에
        # print('numbers =', numbers)
        # print('results =', result)
        if reverse:
            _, value = find_max(numbers_copy)
        else:
            _, value = find_min(numbers_copy)  # 최솟값 찾기
        result.append(value)  # 결과 리스트에 추가
        numbers_copy.remove(value)  # 원본에서 최솟값 찾기
    return result


numbers = [np.random.randint(0, 100) for _ in range(10)]
print('numbers =', numbers)
sorted_numbers_desc = sel_sort(numbers, reverse=True)
print('sorted_numbers(descending) =', sorted_numbers_desc)
sorted_numbers_asc = sel_sort(numbers)
print('sorted_numbers(ascending) =', sorted_numbers_asc)


def sel_sort2(numbers: list, reverse: bool = False) -> None:
    """
    주어진 리스트를 정렬하는 함수
    새로운 리스트를 생성하지 않고 원본 리스트의 순서를 바꿈
    :param numbers:
    :param reverse: False이면 오름차순, True이면 내림차순 정렬
    기본값은 False
    :return:
    """
    length = len(numbers)
    for i in range(0, length - 1):
        for j in range(i + 1, length):
            if reverse:
                if numbers[i] < numbers[j]:
                    numbers[i], numbers[j] = numbers[j], numbers[i]
            else:
                if numbers[i] > numbers[j]:
                    numbers[i], numbers[j] = numbers[j], numbers[i]
                    # print(numbers)


numbers = [np.random.randint(0, 100) for _ in range(10)]
print(numbers)
sel_sort2(numbers)
print(numbers)
sel_sort2(numbers, reverse=True)
print(numbers)
