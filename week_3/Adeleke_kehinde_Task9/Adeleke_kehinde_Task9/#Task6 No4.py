#Task6  No4
no = int(input("Enter no of voters: "))
set = set()
for i in range (no):
 name = input("Enter name: ")
 if name in set:
    print("Error name has been entered")
 else:
   set.add(name)
print(len(set))