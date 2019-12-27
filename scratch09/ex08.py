"""
lec08_database 패키지의 내용을 참고, 오라클 데이터베이스에서 emp 테이블의 모든 레코드를 검색 -> 2차원 리스트
csv 모듈을 사용해서 csv 파일(emp.csv)로 저장
"""
import cx_Oracle
import csv
# import scratch09.oracle_config as cfg
#
# with cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn) as conn:
#     with conn.cursor() as cursor:
#         cursor.execute('select * from emp')
#         with open('emp.csv', 'w', encoding='UTF-8', newline='') as f:
#             writer = csv.writer(f)
#             for row in cursor:
#                 writer.writerow(row)

if __name__ == '__main__':
    # DSN: Data Source Name(접속할 오라클 서버(호스트) 정보)
    dsn = cx_Oracle.makedsn('localhost', 1521, 'orcl')
    # 오라클 데이터베이스에 접속(connection)
    with cx_Oracle.connect('scott', 'tiger', dsn) as connection:
        # cursor 객체(SQL문을 데이터베이스 서버에서 실행) 생성
        with connection.cursor() as cursor:
            # SQL 문장 작성
            sql_select_emp = 'select * from emp'
            # SQL 문장을 DB 서버에서 실행
            cursor.execute(sql_select_emp)
            # SQL 실행 결과 처리
            emp = [row for row in cursor]
            print(emp[:2])
            print(len(emp))

    # 리스트 emp의 내용을 파일에 csv 형식으로 저장
    file_path = 'emp.csv'
    # 파일을 쓰기 모드로 읽기
    with open(file_path, mode='w', encoding='UTF-8', newline='') as f:
        writer = csv.writer(f)  # csv writer 객체를 생성
        for item in emp:
            writer.writerow(item)  # 각 아이템을 csv 파일에 한줄씩 쓱

