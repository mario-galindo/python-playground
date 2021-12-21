price = input("how much did you pay? ")
price = float(price)

if price >= 1.00:
    tax = 0.7
    print("Tax rate is: " + str(tax))
else:
    tax = 0
    print("Tax rate is: " + str(tax))


price = input("how much did you pay? ")
price = float(price)

if price >= 1.00:
    tax = 0.7
else:
    tax = 0
print("[refactor]Tax rate is: " + str(tax))

country = input("Enter the name of you home country: ")
if country.lower() == "canada":
    print("So you must like hockey!")
else:
    print("You are not from Canada")
