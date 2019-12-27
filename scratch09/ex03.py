"""
1) csv 파일(stock_price.csv) write
6/20/2019,AAPL,90.91
6/20/2019,MSFT,41.68
6/21/2019,AAPL,90.86
6/21/2019,MSFT,41.51

2) csv 파일의 내용을 csv.reader를 사용해서 리스트로 변환
각 종목의 주식 가격 평균을 계산해서 출력

3) csv 파일의 내용을 csv.DictReader를 사용해서 리스트로 변환
각 주식 종목의 주식 가격 평균을 계산해서 출력
"""
import csv

from lec07_file.file07 import get_sum_mean

row1 = ['6/20/2019', 'AAPL', 90.91]
row2 = ['6/20/2019', 'MSFT', 41.68]
row3 = ['6/21/2019', 'AAPL', 90.86]
row4 = ['6/21/2019', 'MSFT', 41.51]
stock = [row1, row2, row3, row4]

with open('stock_price.csv', mode='w', encoding='UTF-8', newline='') as f:
    writer = csv.writer(f, delimiter=',')
    for row in stock:
        writer.writerow(row)


with open('stock_price.csv', mode='r', encoding='UTF-8') as f:
    reader = csv.reader(f)
    df = [row for row in reader]
apple = [row for row in df if row[1] == 'AAPL']
ms = [row for row in df if row[1] == 'MSFT']
apple_mean = get_sum_mean(apple, 2)[1]
ms_mean = get_sum_mean(ms, 2)[1]
print('Mean of APPLE:', apple_mean)
print('Mean of Microsoft:', ms_mean)


with open('stock_price.csv', mode='r', encoding='UTF-8') as f:
    # csv 파일에 컬럼 이름이 없는 경우 생성자의 fieldnames 파라미터에 컬럼 이름 값들을 전달하면 됨
    col_names = ['date', 'stock', 'price']
    dict_reader = csv.DictReader(f, fieldnames=col_names)
    dict_stock = [row for row in dict_reader]
apple_stock = [float(row['price']) for row in dict_stock if row['stock'] == 'AAPL']
ms_stock = [float(row['price']) for row in dict_stock if row['stock'] == 'MSFT']

ap_mean = sum(apple_stock) / len(apple_stock)
msft_mean = sum(ms_stock) / len(ms_stock)

print('Mean of APPLE:', ap_mean)
print('Mean of Microsoft:', msft_mean)




