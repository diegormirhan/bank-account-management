from validate_email import validate_email
from datetime import date

is_valid = validate_email('diegomirhan2@gmail.com', verify=True)
print(is_valid)

print(date.today())
