from Account import *



usd = Currency("United States Dollar", "$", "usd")


client = Client("Jane", "Doe", "Female", 1985, 3, 11, 17890193225, "aaa@bbb.com")

account = Account(client, usd)

print(len(Client.clientList))
