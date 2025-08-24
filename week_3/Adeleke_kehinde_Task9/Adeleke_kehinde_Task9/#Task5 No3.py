#task5 no3
new = ()
state = input("Enter first state: "),input("Enter second state: "),input("Enter third state: "),input("Enter fourth state: "),input("Enter fifth state: ").title()
neww = new + state
print(f"First state: {neww[0]}\n second state: {neww[-1]}")
if "Lagos" in neww:
    print("yes")
else:
    print("No lagos")
print(len(state))