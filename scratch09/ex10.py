import cx_Oracle
import pandas as pd


def get_column_names_of(table, cursor):
    # cursor.execute(f"select column_name from user_tab_columns \
    # where table_name = '{table.upper()}' order by column_id")
    sql = """select column_name from user_tab_columns 
    where table_name = :tbl_name 
    order by column_id"""
    cursor.execute(sql, tbl_name=table.upper())  # data binding
    # cursor가 sql 문장의 :변수 위치에 데이터 타입에 맞게끔 값을 치환해 줌
    # 값이 문자열이면 '문자열' 형태로 :변수 위치에 치환됨
    return [row[0] for row in cursor]


def select_all_from(table, cursor):
    cursor.execute(f'select * from {table}')
    # from 구문에서 테이블 이름은 ''로 감싸면 안되기 때문에 데이터바인딩 방식을 사용할 수 없다.
    df = pd.DataFrame(cursor)
    df.columns = get_column_names_of(table, cursor)
    return df


def get_salgrade(sal_series, salgrade_df):
    grades = []
    for sal in sal_series:
        for index, row in salgrade_df.iterrows():
            if row['LOSAL'] <= sal <= row['HISAL']:
                grades.append(row['GRADE'])
                break
    return grades


if __name__ == '__main__':
    # 오라클 DB 서버에 접속
    dsn = cx_Oracle.makedsn('localhost', 1521, 'orcl')
    with cx_Oracle.connect('scott', 'tiger', dsn) as connection:
        # cursor 객체 생성
        with connection.cursor() as cursor:
            emp_columns = get_column_names_of('emp', cursor)
            print(emp_columns)  # ['empno', 'ename', 'job', ...]

            emp_df = select_all_from('emp', cursor)  # DataFrame
            print(emp_df)

            dept_df = select_all_from('dept', cursor)
            print(dept_df)

            salgrade_df = select_all_from('salgrade', cursor)
            print(salgrade_df)

            # DataFrame에 새로운 컬럼을 추가
            # DataFrame['컬럼 이름'] = list, pandas.Series
            # emp_df에 salgrade 컬럼을 추가
            # emp_df['sal'] 갯수만큼 반복:
            # 선택된 sal 값이 salgrade_df 어느 grade에 속하는지를 찾음
            # -> salgrade_df의 행 갯수만큼 반복하면서 LO, HI와 비교
            # -> DataFrame.iterrows() 함수 이용?

            emp_df['SALGRADE'] = get_salgrade(emp_df['SAL'], salgrade_df)
            print(emp_df)

            # SQL join - pandas.merge
            emp_dept = pd.merge(emp_df, dept_df, on='DEPTNO')
            print(emp_dept)

            # pandas.merge(left, right, how, on, left_on, right_on, ...)
            # left, right: 조인할 데이터프레임
            # how: 조인 방식(inner, left, right)
            # on: 조인할 때 기준이 되는 컬럼 이름
            # 조인의 기준이 되는 컬럼 이름이 서로 다르면:
            #   left_on='left 데이터프레임 컬럼', right_on='right DF column'

            # emp_df, dept_df 데이터프레임의 left, right join 결과 비교
            emp_dept_left = pd.merge(emp_df, dept_df, 'left', on='DEPTNO')
            print(emp_dept_left)
            emp_dept_right = pd.merge(emp_df, dept_df, 'right', on='DEPTNO')
            print(emp_dept_right)

            # emp 테이블에서 mgr과 empno가 일치하는 join
            # 1) inner, 2) left, 3) right join
            emp_self = pd.merge(emp_df, emp_df, left_on='MGR', right_on='EMPNO')
            print(emp_self)
            emp_self_left = pd.merge(emp_df, emp_df, 'left', left_on='MGR', right_on='EMPNO')
            print(emp_self_left)
            emp_self_right = pd.merge(emp_df, emp_df, 'right', left_on='MGR', right_on='EMPNO')
            print(emp_self_right)
            print(emp_self_right[['EMPNO_x', 'ENAME_x', 'MGR_x', 'EMPNO_y', 'ENAME_y']])
