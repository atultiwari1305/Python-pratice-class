# f = open("ghost2.jpg","rb")
# # print(f.read())

# f1 = open("ghost2_copy.png","wb")



# for i in f:
#     f1.write(i)

import os

if os.path.exists("demo3.txt"):
    os.remove("demo3.txt")
else:
    print("File doesn't exists")