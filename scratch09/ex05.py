"""
gapminder.tsv 파일을 pandas 패키지의 read_csv() 함수를 사용해서 DataFrame으로 변환
DataFrame의 행과 열의 개수 확인
DataFrame의 앞쪽 데이터 5개를 출력
DataFrame의 뒷쪽 데이터 5개를 출력
DataFrame의 컬럼 이름들을 출력
DataFrame의 각 컬럼의 데이터타입들을 출력
DataFrame에서 'country', 'lifeExp', 'gdpPercap' 컬럼들만 출력
DataFrame에서 행 인덱스가 0, 99, 999인 행들을 출력
DataFrame에서 행 레이블이 840~851인 행들의 나라이름, 기대수명, 1인당 GDP를 출력
DataFrame에서 연도(year)별 기대수명의 평균을 출력
DataFrame에서 연도(year)별, 대륙(continent)별 기대수명의 평균
"""
import pandas as pd
import matplotlib.pyplot as plt

gap = pd.read_csv('gapminder.tsv', encoding='UTF-8', sep='\t')
print('shape:', gap.shape)

print('DataFrame의 앞쪽 데이터 5개를 출력')
print(gap.head())

print('DataFrame의 뒷쪽 데이터 5개를 출력')
print(gap.tail())

# 행 인덱스를 이용한 출력
# DataFrame.iloc[row index, column index]
# 만약 column 인덱스를 생략하면 선택한 row index의 모든 컬럼이 선택됨
print(gap.iloc[0:5])
print(gap.iloc[-5:])

# DataFrame.columns: pandas.Index 클래스 객체. 컬럼 이름들의  리스트를 가지고 잇음
print('DataFrame의 컬럼 이름들을 출력')
print(gap.columns)

print('DataFrame의 각 컬럼의 데이터타입들을 출력')
# pandas.read_csv() 함수는 파일의 문자열을 타입에 맞게끔 변환하는 기능을 갖고 있음
# pandas 데이터 타입: object(문자열), int64(64비트 정수), float64(64비트 실수)
print(gap.dtypes)

print("DataFrame에서 'country', 'lifeExp', 'gdpPercap' 컬럼들만 출력")
print(gap[['country', 'lifeExp', 'gdpPercap']])

print('DataFrame에서 행 인덱스가 0, 99, 999인 행들을 출력')
print(gap.iloc[[0, 99, 999]])

# DataFrame.iloc[row index, column index]
# DataFrame.loc[row label, column label]
# loc에서 범위 연산자(:)가 사용되면 이름(label)으로 취급되기 때문에 양쪽 숫자 모두 포함
# iloc에서 :이 사용되면 인덱스로 취급되기 때문에 뒤쪽 숫자는 미포함
print('DataFrame에서 행 레이블이 840~851인 행들의 나라이름, 기대수명, 1인당 GDP를 출력')
print(gap.loc[840:851, ['country', 'lifeExp', 'gdpPercap']])

print('DataFrame에서 연도(year)별 기대수명의 평균을 출력')
gap_by_year = gap.groupby('year')
print(gap_by_year)  # DataFrame 객체
print(gap_by_year['lifeExp'])  # Series 객체
print(gap_by_year['lifeExp'].mean())

print('DataFrame에서 연도(year)별, 대륙(continent)별 기대수명의 평균')
gap_by_year_continent = gap.groupby(['year', 'continent'])
print(gap_by_year_continent['lifeExp'].mean())

# 연도별 기대수명 그래프
year_lifeExp = gap.groupby('year')['lifeExp'].mean()
plt.plot(year_lifeExp)
plt.show()

# 연도별 전세계 인구수(pop)를 그래프
year_pop = gap.groupby('year')['pop'].sum()
print(year_pop)
plt.plot(year_pop)
plt.show()

