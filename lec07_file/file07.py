"""
file.readline() 사용해서 csv 파일 읽기
"""


def my_csv_reader(fn: str, header=True) -> list:
    """

    :param fn: 읽을 파일 이름(ex. data\\exam.csv)
    :param header: csv 파일의 헤더 존재 여부
    :return: csv 파일에서 헤더를 제외한 데이터들로 이루어진 2차원 리스트
    """
    data = []
    with open(fn, 'r', encoding='utf-8') as f:
        if header:
            f.readline()
        for line in f:
            data.append(line.strip().split(','))
    return data


def print_data(data: list) -> None:
    """
    2차원 리스트의 내용을 출력
    ex.
    1 10 20 30 40
    2 11 21 31 41
    ...

    :param data: 2차원 행렬 형태의 리스트
    :return: None
    """
    for row in data:
        for col in row:
            print(col.rjust(3), end=' ')
        print()


def get_sum_mean(data: list, col: int) -> tuple:
    """
    주어진 2차원 리스트(data)에서 해당 컬럼(col)의 데이터의 총합(sum)과 평균(avg)을 계산해서 리턴

    :param data: 2차원 행렬 형태의 리스트
    :param col: 컬럼 인덱스(0, 1, 2, ...)
    :return: 컬럼 데이터의 합과 평균
    """
    col_sum = 0
    for row in data:
        col_sum += float(row[col])
    col_mean = col_sum / len(data)
    return col_sum, col_mean
    # col_data = []
    # for row in data:
    #     col_data.append(int(row[col]))
    # t = (sum(col_data), sum(col_data) / len(col_data))
    # return t


if __name__ == '__main__':
    # 작성한 함수를 테스트
    import os
    test = my_csv_reader(os.path.join('data', 'exam.csv'), True)
    print_data(test)
    print(get_sum_mean(test, 1))

