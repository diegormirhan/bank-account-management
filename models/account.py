from models.client import Client
from utils.helper import format_float_to_str


class Account:
    acc_code: int = 1001

    def __init__(self: object, client: Client) -> None:
        self.__number: int = Account.acc_code
        self.__client: Client = client
        self.__balance: float = 0.0
        self.__limit: float = 100.0
        self.__total_balance: float = self._calculate_total_balance
        Account.acc_code += 1

    @property
    def number(self) -> int:
        return self.__number

    @property
    def client(self) -> Client:
        return self.__client

    @property
    def balance(self) -> float:
        return self.__balance

    @balance.setter
    def balance(self, value) -> None:
        self.__balance = value

    @property
    def limit(self) -> float:
        return self.__limit

    @limit.setter
    def limit(self, value) -> None:
        self.__limit = value

    @property
    def total_balance(self) -> float:
        return self.__total_balance

    @total_balance.setter
    def total_balance(self, value) -> None:
        self.__total_balance = value

    @property
    def _calculate_total_balance(self) -> float:
        return self.balance + self.limit

    def deposit(self, value: float) -> None:
        if value > 0:
            self.balance = self.balance + value
            self.total_balance = self._calculate_total_balance
            print('Successful deposit!')
        else:
            print('Error when making the withdrawal!')

    def withdraw(self, value) -> None:
        if 0 < value <= self.total_balance:
            if self.balance >= value:
                self.balance = self.balance - value
                self.total_balance = self._calculate_total_balance
            else:
                remaining: float = self.balance - value
                self.limit = self.__limit + remaining
                self.balance = 0
                self.total_balance = self._calculate_total_balance
            print('Successful withdrawal!')
        else:
            print('Withdrawal not performed. Try again!')

    def transfer(self, destiny, value: float) -> None:
        if 0 < value <= self.total_balance:
            if self.balance >= value:
                self.balance = self.balance - value
                self.total_balance = self._calculate_total_balance
                destiny.balance = destiny.balance + value
                destiny.total_balance = destiny._calculate_total_balance
            else:
                remaining: float = self.balance - value
                self.balance = 0
                self.limit = self.limit + remaining
                self.total_balance = self._calculate_total_balance
                destiny.balance = destiny.balance + value
                destiny.total_balance = destiny._calculate_total_balance
            print('Successful Transfer')
        else:
            print('Transfer not performed. Try again!')

    def __str__(self) -> str:
        return f'Account Number: {self.number}\n' \
               f'Client: {self.client.name}\n' \
               f'Total Balance: {format_float_to_str(self.total_balance)}'
