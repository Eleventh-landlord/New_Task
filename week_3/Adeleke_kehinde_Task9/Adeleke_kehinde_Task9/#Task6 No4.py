#Task6  No4
#Ask for voter names and store in a set.
no = int(input("Enter no of voters: "))
set = set()
for i in range (no):
 name = input("Enter name: ")
 #If a voter tries to register twice, display a warning.
 if name in set:
    print("Error name has been entered")
 else:
   set.add(name)
#After registration, display the total number of unique voters.
print(len(set))