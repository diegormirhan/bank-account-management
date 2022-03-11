from validate_email import validate_email
from validate_docbr import CPF
from datetime import date


def validation_email(mail):
    is_valid: str = validate_email(mail, verify=True)
    return is_valid


def validation_cpf(cpf):
    cpf_id = CPF()
    return cpf_id.validate(cpf)


def validation_birth(birth):
    today = date.today()
    imput_day, imput_month, imput_year = birth.split("/")

    year = today.year
    year_validation = year - int(imput_year)

    if year_validation >= 18:
        return True
    else:
        return False



