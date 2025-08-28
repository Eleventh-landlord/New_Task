#Task7 no 3
#Store days of the week in a tuple and ask the user to input an activity for three specific days.

days = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
# no = 3
# for i in range (no):
print("Enter three specific dates")
day1 = input("Enter first day: ").title()
day2 = input("Enter second day: ").title()
day3 = input("Enter third day: ").title()


if day1 in days:
      actvi1 = input(f"Enter actvity for {day1}: ")
else:
      print(f"{day1} isnt in days")
if day2 in days:
          actvi2 = (f"Enter actvity for {day2}: ")
else:
           print(f"{day2} is not in days")
if day3 in days:
          actvi3 = (f"Enter actvity for {day3}: ")
else:
           print(f"{day3} is not in days")
   