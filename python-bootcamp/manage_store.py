
# Prices dictionary with 5 items
Prices = {
    "rice": 60,
    "sugar": 45,
    "milk": 30,
    "bread": 40,
    "soap": 25
}

out_of_stock = {"milk", "bread"}

Order = ["rice", "milk", "soap", "sugar", "bread"]

total = 0

for item in Order:
    if item in out_of_stock:
        print(item, "is unavailable")
    else:
        total = total + Prices[item]
        print(item, "price:", Prices[item])

print("Final order value:", total)
