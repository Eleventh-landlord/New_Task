#Task3 no3
word = input("Enter a URL: ")
if (word[0:8]) == "https://":
    print(word)
else:
    print("word dosent start with https://")
#OR
while word.startswith("https://"):
    print("Correct")
    break
#OR
while True:
    word = input("enter a string: ")
    if word.startswith("https://") :
        print(word)
    else:
        print("error")
    break