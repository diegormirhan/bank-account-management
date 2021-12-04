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

    @property
    def _calculate_total_balance(self) -> float:
        return self.balance + self.limit

    def deposit(self, value: float) -> float:
        pass

    def withdraw(self, value: float) -> None:
        pass

    def transfer(self, destiny: object, value: float) -> None:
        pass

    def __str__(self) -> str:
        return f'Account Number: {self.number}\n' \
               f'Client: {self.client.name}\n' \
               f'Total Balance: {format_float_to_str(self.total_balance)}'
