from datetime import date
from datetime import datetime


def date_to_str(dates: date) -> str:
    return dates.strftime('%d/%m/%Y')


def str_to_date(dates: str) -> date:
    return datetime.strptime(dates, '%d/%m/%Y')


def format_float_to_str(valor: float) -> str:
    return f'R$ {valor:,.2f}'
