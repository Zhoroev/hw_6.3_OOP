class Borrower:
    def __init__(self, credit_amount, commission, percent):
        self.credit_amount = credit_amount
        self.commission = commission
        self.percent = percent

    def hello(self):
        self.hi = 'hi'
        
    def get_data(self):
        return f'Сумма кредита - {self.credit_amount}\n' \
               f'Cумма всех комиссий (разовых и ежемесячных) - {self.commission}\n' \
               f'Проценты по кредиту - {self.percent} %'

    @property
    def credit_calc(self):
        return self.credit_amount + self.commission + self.percent


john = Borrower(10, 10, 10)
print(john.get_data())
print(john.credit_calc)

# при вызове метода hello появляется атрибут hi, если метод не вызывался, то атрибута hi не будет существовать
john.hello()
print(john.hi)

