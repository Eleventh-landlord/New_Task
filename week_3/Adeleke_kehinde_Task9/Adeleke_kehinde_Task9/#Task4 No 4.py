#task4 no 4
name = input("Enter 5 names seperated by spaces: ").lower()
split = name.split()
sort = sorted(split)
for name in sort:
    print(name)