# try:
#     f = open("demo.txt")
#     #your code goes here
# finally:
#     f.close()


# with open("demo.txt") as f:
#     f.read()

f=open("demo.txt","r")
print(f.read(4))
print(f.tell())