#Task 7 no 5
#Store three names and their phone numbers in two separate tuples.
names = ("Adeleke","Dreshy","Kendel")
numbers = ("08107869063","09034212617","09158537780")
# - Create a dictionary from them using `dict(zip(...))`.
dict = dict(zip(names, numbers))
# - Ask the user for a name and display the corresponding number (or an error message).
user = input("Enter a name: ").title()
if user in names:
    phone_no = dict.get(user)
    print(f"{user}:{phone_no}")
else:
    print("An error message")