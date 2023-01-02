# try:
    #this block of code will run and throw errors if any

# except:
    #this will raise the errors

# else:
    #this will execute if there are no errors

# finally:
    #this will execute regardless the result of try and except


try:
    print(2/0)
except ZeroDivisionError:
    print("Bhai ye error aayega tbhi aaunga")
else:
    print("bhai error nhi aayega tbhi chalunga")
finally:
    print("Main toh hmesa chlunga")