#Task8 no 5
store = {"Book": 10,"Pen": 20,"Bag": 5}
buy = input("Enter the item you want to buy: ").title()
if buy in store:
    quantity = int(input("Enter quantity: "))
else:
 print("We dont have in store!")
print(f"Before Purchase: {store}")
store[buy] = store.get(buy,0)
store[buy] -= quantity
store[buy] = max(0,store[buy])
print(f"After Purchase: {store}")