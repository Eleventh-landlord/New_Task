#task4 no6
#Ask the user to input a word.
word = input("Enter a word: ")
#Print the length of the word.
print(len(word))
#Check if it is all uppercase, all lowercase, or title case.
if word == word.upper():
    print(f"{word} is in upper case")
elif word == word.lower():
    print(f"{word} is in lower case")
elif word == word.title():
    print(f"{word} is in title case")
else:
    print("Enter better word jor")
#Reverse the word using slicing.
reverse = word[::-1]
print(reverse)
