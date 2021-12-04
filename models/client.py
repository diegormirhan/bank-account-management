from datetime import date
from utils.helper import date_to_str, str_to_date


class Client:
    counter: int = 101

    def __init__(self: object, name: str, email: str, cpf: str, birth_date: str) -> None:
        self.__code: int = Client.counter
        self.__name: str = name
        self.__email: str = email
        self.__cpf: str = cpf
        self.__birth_date: date = str_to_date(birth_date)
        self.__register_date: date = date.today()
        Client.counter += 1

    @property
    def code(self) -> int:
        return self.__code

    @property
    def name(self) -> str:
        return self.__name

    @property
    def email(self) -> str:
        return self.__email

    @property
    def cpf(self) -> str:
        return self.__cpf

    @property
    def birth_date(self) -> str:
        return date_to_str(self.__birth_date)

    @property
    def register_date(self) -> str:
        return date_to_str(self.__register_date)

    def __str__(self) -> str:
        return f'Code: {self.code}\n' \
               f'Name: {self.name}\n' \
               f'Birth Date: {self.birth_date}\n' \
               f'Register Date: {self.register_date}'


