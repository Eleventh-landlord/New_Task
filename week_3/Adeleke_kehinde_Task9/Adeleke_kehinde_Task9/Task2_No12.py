
# Task2 No12
while True:
    name = input("Enter name (type exit to quit): ")
    if name.lower() == "exit":
        print("Goodbye")
        break
    print(f"Hello: {name}")
for num in range (1,10):
    if num == 5:
        break
    print(num)
for num in range (1,10):
    if num == 3:
        continue
    print(num)
while True:
    print("\nMenu:")
    print("1. Say Hello")
    print("2. say Goodbye")
    print("3, exit")
    choice = input("Chose an option: ")
    if choice == "1":
        print("Hello")
    elif choice == "2":
        print("Goodbye")
    elif choice == "3":
        print("Exit")
        break
    else:
        print("Invalid choice. try again")
