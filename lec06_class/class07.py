class Account:
    """ 은행 계좌 클래스
    field(데이터): 계좌번호(accountno), 잔액(balance)
    method(기능): 입금(deposit), 출금(withdraw), 이체(transfer)
    """
    def __init__(self, accountno, balance):
        self.accountno = accountno
        self.balance = balance
        try:
            temp = balance + 1
        except Exception:
            raise TypeError()

    def __repr__(self):
        return f'Account(account no.: {self.accountno}, balance: {self.balance})'

    def deposit(self, amount):
        self.balance += amount
        print(f'{amount} 입금 완료. 거래 후 잔액: {self.balance}')

    def withdraw(self, amount):
        if self.balance < amount:
            print(f'잔액 부족! 현재 잔액: {self.balance}')
        else:
            self.balance -= amount
            print(f'{amount} 출금 완료. 거래 후 잔액: {self.balance}')

    def transfer(self, other, amount):
        if self.balance >= amount:
            self.withdraw(amount)
            other.deposit(amount)
        else:
            print(f'잔액 부족! 현재 잔액: {self.balance}')


if __name__ == '__main__':
    acc1 = Account(1234, 50000)
    acc2 = Account(5678, 5000)
    print(acc1)
    print(acc2)

    acc1.deposit(100000)
    acc1.withdraw(150000)
    acc1.withdraw(5000)

    acc2.transfer(acc1, 5000)
    print(acc1)
    acc2.transfer(acc1, 5000)

