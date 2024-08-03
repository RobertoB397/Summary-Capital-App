import requests
3
request_url = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/eur.json"
# Get data from web API
response = requests.get(request_url)
#Convert json data object to a python format
data = response.json()
#Save currencies dictionary in other dictionary
currencies = data["eur"]

#1. How many accounts do you have
#2. Select accounts currency
#3. Ask for amount in accounts
#5. Add every amount and print the result

print("WELCOME TO YOUR SUMMARY CAPITAL APP (MXN/EUR)")
print("---------------------------------------------")
accounts_qty = input("How many accounts do you have? ")

#Function to define accounts currencies
def account_currency():
  currency_options = {"1": "mxn", "2": "eur"}
  print("Account currency")
  print("1. mxn")
  print("2. eur")
  account_currency = input("Type the number of the currency desired: ")
  return currency_options.get(account_currency, 0)


#Function to define accounts amount
def account_amount():
  account_amount = input("Enter the amount in the account: ")
  return account_amount


#List for save details of accounts
accounts_currency = account_currency()
accounts_values = []
account_details = []
print("\nAccounts details")

#Loop to store accounts amount
if accounts_currency != 0:
  for i in range(0, int(accounts_qty)):
    print("Account ", i + 1)
    try:
      accounts_values.append(float(account_amount()))
    except Exception as error:
      print("Input should be a number")
      accounts_values.append(float(account_amount()))
    print("------------------------------------\n")
else:
  print("Invalid option")
  print("Run again and select a correct option")
  exit()

total_mxn = 0
total_eur = 0

#Conversion mxn/eur and eur/mxn
if accounts_currency == "mxn":
  for value in accounts_values:
    total_mxn += value
    total_eur += value / round(data["eur"]["mxn"], 2)

elif accounts_currency == "eur":
  for value in accounts_values:
    total_eur += value
    total_mxn += value * round(data["eur"]["mxn"], 2)

#Print Results
print("----------------SUMMARY------------------")
print("-----------------------------------------")
print("1 EUR =", round(data["eur"]["mxn"], 2), "MXN")
print("Total amount in MXN : ", round(total_mxn, 2))
print("Total amount in EUR : ", round(total_eur, 2))