#task6 no2
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