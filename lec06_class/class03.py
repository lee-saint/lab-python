"""
클래스 작성, 객체 생성, 메소드 사용 연습
"""


class Employee:
    """
    field: empno, ename, salary, deptno
    method: raise_salary(self, pct)
    """
    def __init__(self, empno, ename, salary, deptno):
        self.empno = empno
        self.ename = ename
        self.salary = salary
        self.deptno = deptno

    def raise_salary(self, pct):
        """
        인상된 급여를 리턴
        :param pct: 급여 인상율(0.1 = 10%, 0.5 = 50%, ...)
        :return:
        """
        # return self.salary * (1 + pct)
        self.salary *= 1 + pct

    def __repr__(self):
        return f'(사번: {self.empno}, 이름: {self.ename}, 급여: {self.salary}, 부서번호: {self.deptno})'


scott = Employee(7788, 'SCOTT', 1000, 10)
print(scott.__repr__())
scott.raise_salary(0.1)
print(scott.__repr__())

king = Employee(7834, 'KING', 10000, 20)
print(king.__repr__())
king.raise_salary(-0.1)
print(king.__repr__())


ohssam = Employee(1012, '오쌤', 500, 30)

employees = [ohssam, king, scott]
print(employees)

print(sorted(employees, key=lambda x: x.empno))
print(sorted(employees, key=lambda x: x.salary))
print(sorted(employees, key=lambda x: x.ename))
