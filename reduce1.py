from functools import reduce

list = [1, 2, 3, 4, 5, 6]

output= reduce(lambda a,b:a+b,list)
print(output)