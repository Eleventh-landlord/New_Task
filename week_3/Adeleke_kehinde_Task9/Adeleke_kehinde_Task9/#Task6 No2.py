#task6 no2
#Write a program that collects the names of people attending a seminar (no duplicates allowed) and displays them in alphabetical order.
no = int(input("Enter the no of people attending the seminar: "))
set = set()
for i in  range(no):
    name = input("Enter name: ")
    if name in set:
        print("error")
    else:
        set.add(name)    
sort = sorted(set)
for sort in sort:
    print(sort)