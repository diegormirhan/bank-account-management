from models.client import Client
from models.account import Account

diego: Client = Client('Diego Mirhan', 'mirhan.diego@gmail.com', '520.510.078-88', '19/06/2004')
anna: Client = Client('Edileni Rodrilla', 'e.rodrilla@gmail.com', '068.209.758-64', '07/05/1967')

# print(diego)
# print(mae)

acc_diego: Account = Account(diego)
acc_anna: Account = Account(anna)

print(acc_diego)
print(acc_anna)
