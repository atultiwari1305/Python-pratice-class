#if length of string is greater than 3 print ing as suffix else print as it is

word=input("Enter your word: ")
if len(word)>3:
    print(word+"ing")
else:
    print(word)