#Task 7 no 5
names = ("Adeleke","Dreshy","Kendel")
numbers = ("08107869063","09034212617","09158537780")
dict = dict(zip(names, numbers))
user = input("Enter a name: ").title()
if user in names:
    phone_no = dict.get(user)
    print(f"{user}:{phone_no}")
else:
    print("An error message")