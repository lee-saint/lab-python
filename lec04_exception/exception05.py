def user_input():
    """
    사용자에게 1, 2, 3 중 하나의 숫자를 입력하도록 안내 -> 사용자가 입력한 숫자를 리턴.
    사용자가 숫자로 변환할 수 없는 문자를 입력하면, 안내문 출력 후 다시 입력받기
    사용자가 1, 2, 3 이외의 숫자를 입력하면, 안내문 출력 후 다시 입력받기
    :return: 1, 2, 3 중의 하나
    """
    while True:
        try:
            try:
                num = int(input("1, 2, 3 중 하나의 숫자를 입력하세요."))
            except ValueError:
                raise ValueError('숫자만 입력해주세요!')
            if num > 3 or num < 1:
                raise ValueError('1 ~ 3 중에서 입력하세요.')
            return num
        except ValueError as e:
            print(e.args)


num = user_input()
print(num)
