#task5 no3
#Create a tuple of 5 Nigerian states entered by the user.
new = ()
state = input("Enter first state: ").title(),input("Enter second state: ").title(),input("Enter third state: ").title(),input("Enter fourth state: ").title(),input("Enter fifth state: ").title()
neww = new + state
#Print the first state and last state.
print(f"First state: {neww[0]}\nsecond state: {neww[-1]}")
#Check if "Lagos" is in the tuple and print "Yes" or "No".
if "Lagos" in neww:
    print("yes")
else:
    print("No lagos")
#Print the number of states entered.
print(len(state))