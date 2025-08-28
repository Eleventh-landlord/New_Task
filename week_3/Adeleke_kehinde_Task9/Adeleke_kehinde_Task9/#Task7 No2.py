#Task7 no 2
#Create a program that stores items and their prices in a dictionary.
price = {}
#Items should come from a list.
items = ["Gun","Bomb","Knife","Book"]
for item in items:
#Prices are entered by the user.
   price[item] = float(input(f"Enter price for {item}: "))
for item, price in price.items():
#Display all items and prices, then allow the user to update the price of an item.
 print(f"{item}:{price}")
update_i = input("Enter item you want to update the price: ")
if update_i in items:
      price[update_i] = float(input(f"Enter new price of {update_i}: "))
      print(f"{price}")
else:
 print("Error! Enter another item")