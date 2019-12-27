# 1부터 n까지 숫자들의 합을 리턴하는 함수
# 1 + 2 + 3 + ... + n


def summate(number):
    # result = 0
    # for i in range(1, number + 1):
    #     result += i
    # return result
    return int(number * (number + 1) / 2)


print(summate(6))
print(summate(1))

# 1부터 n까지 숫자들의 제곱의 합을 리턴하는 함수
# 1**2 + 2**2 + 3**2 + ... + n**2


def sumsqure(number):
    # result = 0
    # for i in range(1, number + 1):
    #     result += i ** 2
    # return result
    return int(number * (number + 1) * (2 * number + 1) / 6)


print(sumsqure(5))
print(sumsqure(1))

# 숫자들의 리스트를 전달받아서 최댓값을 찾아 리턴하는 함수


def find_max(nums):
    result = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > result:
            result = nums[i]
    return result


print(find_max([1, 2, 3, 4, 5]))
print(find_max([5, 4, 3, 2, 1]))
print(find_max([5, 7, 10, 24, 2]))


def find_max2(values: list) -> float:
    # sorted(list): list를 정렬한 새로운 리스트 리턴
    # 원본 리스트는 순서가 그대로 유지됨
    # list.sort(): 원본 리스트를 정렬해서 순서를 바꿈 / returns None
    sorted_list = sorted(values)
    return sorted_list[-1]

# 숫자들의 리스트를 전달받아서 최댓값의 인덱스를 리턴하는 함수


def max_index(nums):
    result = 0
    compare = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > compare:
            result = i
            compare = nums[i]
    return result
    # max_id, max_val = 0, nums[0]
    # for i, v in enumerate(nums):
    #     if v > max_val:
    #         max_id, max_val = i, v
    # return max_id


print(max_index([5, 4, 3, 2, 1]))
print(max_index([4, 5, 1]))
print(max_index([1, 2, 3, 4, 5]))

# 숫자들의 리스트를 전달받아서 중앙값을 리턴하는 함수
# 일단 정렬부터


def sort(nums):
    for i in range(len(nums) - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j+1] = temp
    return nums


def median(nums):
    nums = sort(nums)
    mid = len(nums) // 2
    if len(nums) % 2:
        result = nums[mid]
    else:
        result = (nums[mid - 1] + nums[mid]) / 2
    return result


print(median([3, 5, 1, 4, 2]))
print(median([6, 4, 3, 5, 1, 2]))
