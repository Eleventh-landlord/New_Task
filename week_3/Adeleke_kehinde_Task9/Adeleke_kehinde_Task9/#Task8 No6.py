#Task8 no 6
details = {}
details["Name"] = input("Enter Name: ")
details["Age"] = int(input("Enter Age: "))
details["Score"] = int(input("Enter UTME Score: "))
if details["Score"] >= 200:
      choice = input("Is UNILAG your first choice ('Yes/No'):")
else:
 print("Dosent reach requirement cant continue!")
olevel = input("Do you have 5 credit pass in WEAC/NECO imcluding Mathematics and English: ")
if olevel == "Yes":
   post_UTME = input("Did yoyu participate in Post UTME('Yes/No'): ")
else:
   print("Dosent reach requirement!")
details["Total"] = int(input("Enter total Score Calculation: "))
Final_admi = (200 <= details["Total"] <= 320) and (details["Age"] >=16 )
print(f"Student Result: \nName: {details['Name']} \nAge: {details['Age']} \nUTME Score: {details['Score']} \nTotal Score: {details['Total']} \nPassed: {Final_admi} ")