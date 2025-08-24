#Task8 no 2
place = ()
name = input("Enter name: ")
Age = input("Enter age: ")
citizenship = "Nigeria"
citi = input("Enter country of citizenship: ").title()
if citi == citizenship:
  place = input("Enter the country you schooled in: ").title()
else:
  print("You are not a citizen of nigeria!")
while True:
 if place == citi:
    registered = input("Are you a registered full time undergraduate ('yes/no'): ").title()
 else:
    print("cannot continue with scholarship cause you are not a citizen of nigeria")
    break
 scholarship = input("Are you on any scholarship (yes/no): ").title()
 qualification = input("Do you have 5 distinctions in relevant subjects for WAEC inccluding maths and english (yes/no): ").title()
 eligibity = (citi == citizenship) and (place == citi) and (registered == "Yes") and (scholarship == "No") and (qualification == "Yes")
 print(f"Name: {name}\nAge: {Age}\nCitizenship: {citi}\nEligibity: {eligibity}")
 break