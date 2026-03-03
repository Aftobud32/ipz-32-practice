class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Внесено: {amount}")
        else:
            print("Некоректна сума депозиту")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Знято: {amount}")
        else:
            print("Недостатньо коштів або некоректна сума")

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
print(f"Поточний баланс: {account.get_balance()}")

account.deposit(500)
account.withdraw(200)
print(f"Кінцевий баланс: {account.get_balance()}")


try:
    print(account.__balance)
except AttributeError:
    print("Помилка: Неможливо отримати прямий доступ до приватного атрибуту '__balance'.")