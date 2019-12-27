# gapminder.tsv 파일을 읽어서 데이터프레임 생성
import pandas as pd

df = pd.read_csv('gapminder.tsv', sep='\t', encoding='UTF-8')
print(df.head())

# boolean indexing
# 컬럼의 값을 이용해서 특정 레코드(행, row)를 선택하는 방법
# DataFrame[컬럼의 값을 이용한 조건식]
# SQL: select * from DataFrame where column==''
df_afg = df[df['country'] == 'Afghanistan']
print(df_afg)

df_korea = df[df['country'] == 'Korea, Rep.']
print(df_korea)

# 대한민국(Korea, Rep.)의 인구(pop)와 1인당 GDP(gdpPercap]을 출력
print(df.loc[df['country'] == 'Korea, Rep.', ['pop', 'gdpPercap']])
# print(df[df['country'] == 'Korea, Rep.'][['pop', 'gdpPercap']])


# mpg.csv 파일을 읽어서 DataFrame 생성
# cty 컬럼의 값이 cty 평균보다 큰 자동차들의 model, cty, hwy를 출력
# cty 컬럼의 평균을 계싼
# cty 컬럼의 값이 평균보다 큰 레코드를 출력
# cty가 평균 이상인 자동차들의 model, cty, hwy 컬럼을 출력
mpg = pd.read_csv('../scratch08/mpg.csv', encoding='UTF-8')
print(type(mpg['cty']))  # mpg['cty']의 데이터타입: Series
print(type(mpg[['cty']]))  # mpg[['cty']]의 데이터타입: DataFrame


print(mpg['cty'].mean())
print(mpg.loc[mpg['cty'] > mpg['cty'].mean(), ['model', 'cty', 'hwy']])
