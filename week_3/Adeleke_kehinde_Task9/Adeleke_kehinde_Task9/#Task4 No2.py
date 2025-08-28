#task4 
#Create an empty list.
list = []
print("\nList of items")
#Ask the user to enter 3 shopping items (one by one).
shopping = input("Enter first item: "),input("Enter second item: "),input("Enter third item: ")
#Add them to the list.
list.append(shopping)
# Display the list as a single string, separated by commas.
for item in shopping:
    print(f"1.{item}")