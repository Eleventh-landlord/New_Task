#task4 no 4
#Ask the user to enter 5 names (separated by spaces)
#Convert all names to lowercase.
name = input("Enter 5 names seperated by spaces: ").lower()
#Sort the list alphabetically.
#Display them one name per line.
split = name.split()
sort = sorted(split)
for name in sort:
    print(name)