import pandas as pd
import cx_Oracle

from scratch09.ex10 import select_all_from


def peak_to_peak(x):
    return x.max() - x.min()


if __name__ == '__main__':
    # with-as 구문을 사용해서 오라클 DB 서버에 접속
    dsn = cx_Oracle.makedsn('localhost', 1521, 'orcl')
    with cx_Oracle.connect('scott', 'tiger', dsn) as conn:
        # with-as 구문을 사용해서 Cursor 객체를 생성
        with conn.cursor() as cursor:
            # scratch09 패키지에서 테이블 전체 검색 함수를 사용해서 emp_df 데이터프레임을 생성
            emp_df = select_all_from('emp', cursor)
            print(emp_df)
            # emp_df를 csv 파일로 저장
            emp_df.to_csv('emp.csv', index=False)
            # emp_df에서 부서별 평균 급여를 출력
            mean = emp_df.groupby('DEPTNO')['SAL'].mean()
            print(mean)
            # emp_df에서 부서별 인원수를 출력
            count = emp_df.groupby('DEPTNO')['EMPNO'].count()
            print(count)
            # emp_df에서 부서별 급여 최솟값 출력
            min_sal = emp_df.groupby('DEPTNO')['SAL'].min()
            print(min_sal)
            # emp_df에서 부서별 급여 최댓값 출력
            max_sal = emp_df.groupby('DEPTNO')['SAL'].max()
            print(max_sal)
            # 위의 결과를 하나의 데이터프레임으로 출력
            dept_group_df = pd.DataFrame({
                'count': count,
                'mean': mean,
                'min': min_sal,
                'max': max_sal
            })
            print(dept_group_df)

            # agg(), aggregate(): 파라미터에 함수 이름(혹은 리스트)을 전달하면, GroupBy 객체에 함수를 적용함
            # sal_by_dept. mean() 와
            # sal_by_dept.agg('mean')은 동일한 동작
            # 함수가 집계 함수(pandas.Series 혹은 pandas.Dataframe 클래스가 갖고 있는 메소드: count, mean, sum, ...)인 경우
            # 함수 이름을 문자열로 전달함
            # 개발자가 작성한 함수는 함수 이름을 파라미터에 전달
            df = emp_df.groupby('DEPTNO')['SAL'].agg(['count', 'mean', 'min', 'max', peak_to_peak])
            print(df)

            # print(emp_df.groupby('DEPTNO')['SAL'].agg(pd.Series.mean)) 코드를 쉽게 사용할 수 있도록
            # print(emp_df.groupby('DEPTNO'))['SAL'].agg('mean')과 같은 호출 방식도 제공

            # 직책(job)별 직원 수, 급여 평균, 최소, 최댓값을 출력
            job_group_sal = emp_df.groupby('JOB')['SAL']
            # job_group_df = pd.DataFrame({
            #     'count': job_group_sal.count(),
            #     'mean': job_group_sal.mean(),
            #     'min': job_group_sal.min(),
            #     'max': job_group_sal.max()
            # })
            job_group_df = job_group_sal.agg(['count', 'mean', 'min', 'max', lambda x: x.max() - x.min()])
            print(job_group_df)
            # agg() 함수가 만드는 DataFrame의 컬럼 이름을 설정할 때는 keyword-argument 방식 또는 dict를 파라미터로 전달함
            print(job_group_sal.agg(Count='count', Average='mean', Minimum='min', Maximum='max',
                                    Range=lambda x: x.max() - x.min()))

            # 부서별, 직책별 직원 수, 급여 평균, 최소, 최댓값 출력
            dept_job_group_sal = emp_df.groupby(['DEPTNO', 'JOB'])['SAL']
            # dept_job_group_df = pd.DataFrame({
            #     'count': dept_job_group_sal.count(),
            #     'mean': dept_job_group_sal.mean(),
            #     'min': dept_job_group_sal.min(),
            #     'max': dept_job_group_sal.max()
            # })
            dept_job_group_df = dept_job_group_sal.agg({
                'count': 'count',
                'average': 'mean',
                'minimum': 'min',
                'maximum': 'max',
                'range': lambda x: x.max() - x.min()
            })
            # agg(), aggregate() 함수의 파라미터에 dict를 전달하는 방식은 pandas 패키지 업그레이드 시 없어질 수 있는 기능(deprecated)
            # dict 방식보다는 keyword-argument 방식을 사용하는 것이 안전함
            print(dept_job_group_df)
