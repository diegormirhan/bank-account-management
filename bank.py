from typing import List
from time import sleep
from models.client import Client
from models.account import Account
from validation import validation_email, validation_cpf, validation_birth


accounts: List[Account] = []


def menu() -> None:
    print('--------------------------------------------\n'
          '----------------- ATM ----------------------\n'
          '------------- Supreme Bank -----------------\n'
          '--------------------------------------------')

    print('Select an option:\n'
          '1 -> Create Account\n'
          '2 -> Make Withdraw\n'
          '3 -> Make Deposit\n'
          '4 -> Make Transference\n'
          '5 -> List Accounts\n'
          '6 -> Exit')

    option: int = int(input('=> '))

    if option == 1:
        create_acc()
    elif option == 2:
        make_withdraw()
    elif option == 3:
        make_deposit()
    elif option == 4:
        make_transfer()
    elif option == 5:
        list_acc()
    elif option == 6:
        sleep(2)
        exit(0)
    else:
        menu()


def main() -> None:
    menu()


def create_acc() -> None:
    print('Inform the customer data: ')

    name: str = input('Client Name: ')

    email: str = input('Client E-mail: ')
    print("Checking E-mail...")
    validate_1 = validation_email(email)
    if validate_1:
        pass
    else:
        print("The E-mail must be valid. Try again...\n")
        sleep(2)
        create_acc()

    cpf: str = input('Client CPF: ')
    print("Checking CPF...")
    validate_2 = validation_cpf(cpf)
    if validate_2:
        sleep(1)
    else:
        print("The CPF must be valid. Try again...\n")
        sleep(2)
        create_acc()

    birth_date: str = input('Client Birth Date: ')
    print("Checking Birth date...")
    validate_3 = validation_birth(birth_date)
    if validate_3:
        sleep(1)
    else:
        print("You must be over 18 years old. Try again later...\n")
        sleep(2)
        exit()

    client: Client = Client(name, email, cpf, birth_date)
    account: Account = Account(client)
    accounts.append(account)

    print('Account created successfully!\n\n'
          'Account Data:\n'
          '-------------')

    print(account)
    sleep(2)
    menu()


def make_withdraw() -> None:
    if len(accounts) > 0:
        number: int = int(input('Inform your account number: '))
        acc: Account = search_acc_by_number(number)

        if acc:
            value: float = float(input('Inform the withdraw amount: '))
            acc.withdraw(value)

        else:
            print(f'The account with number {acc} was not found!')

    else:
        print('There are no registered accounts yet!')

    sleep(2)
    menu()


def make_deposit() -> None:
    if len(accounts) > 0:
        number: int = int(input('Inform your account number: '))
        acc: Account = search_acc_by_number(number)

        if acc:
            value: float = float(input('Inform the deposit amount: '))
            acc.deposit(value)

        else:
            print(f'The account with number {acc} was not found!')

    else:
        print('There are no registered accounts yet!')

    sleep(2)
    menu()


def make_transfer() -> None:
    if len(accounts) > 0:
        number_o: int = int(input('Inform your account number: '))
        acc_o: Account = search_acc_by_number(number_o)

        if acc_o:
            number_d: int = int(input('Inform the destiny account number'))
            acc_d: Account = search_acc_by_number(number_d)

            if acc_d:
                value: float = float(input('Inform the transfer amount: '))
                acc_o.transfer(acc_d, value)

            else:
                print(f'The account with number {acc_d} was not found!')

        else:
            print(f'The account with number {acc_o} was not found!')

    else:
        print('There are no registered accounts yet!')

    sleep(2)
    menu()


def list_acc() -> None:
    if len(accounts) > 0:
        print('Accounts List')

        for acc in accounts:
            print(acc)
            print('---------')
    else:
        print('There are no registered accounts!')

    sleep(2)
    menu()


def search_acc_by_number(number: int) -> None:
    c: Account = None

    if len(accounts) > 0:
        for acc in accounts:
            if acc.number == number:
                c = acc

    return c


if __name__ == '__main__':
    main()
