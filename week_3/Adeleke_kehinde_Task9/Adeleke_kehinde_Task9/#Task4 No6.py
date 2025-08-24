#task4 no6
word = input("Enter a word: ")
print(len(word))
if word == word.upper():
    print(f"{word} is in upper case")
elif word == word.lower():
    print(f"{word} is in lower case")
elif word == word.title():
    print(f"{word} is in title case")
else:
    print("Enter better word jor")
