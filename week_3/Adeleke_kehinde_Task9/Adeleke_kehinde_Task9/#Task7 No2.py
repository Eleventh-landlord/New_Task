#Task7 no 2
price = {}
items = ["Gun","Bomb","Knife","Book"]
for item in items:
   price[item] = float(input(f"Enter price for {item}: "))
for item, price in price.items():
 print(f"{item}:{price}")
update_i = input("Enter item you want to update the price: ")
if update_i in items:
      price[update_i] = float(input(f"Enter new price of {update_i}: "))
      print(f"{price}")
else:
 print("Error! Enter another item")