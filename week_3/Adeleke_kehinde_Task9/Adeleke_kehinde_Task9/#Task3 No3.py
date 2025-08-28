#Task3 no3
#Check if a given string starts with "https://".
word = input("Enter a URL: ")
if (word[0:8]) == "https://":
    print(word)
else:
    print("word dosent start with https://")
#OR
#Check if a given string starts with "https://".
while word.startswith("https://"):
    print("Correct")
    break
#OR
#Check if a given string starts with "https://".
while True:
    word = input("enter a string: ")
    if word.startswith("https://") :
        print(word)
    else:
        print("error")
    break