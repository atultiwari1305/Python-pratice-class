#set- store multiple values in single variable
#unordered
#unchangable/immutable
#duplicates not allowed
#non homogeneous

mySet1={"car", "boat", "train"}
mySet2={1,2,3,4}
mySet3={4,5,6,7} 
# mySet1.update(mySet2)
# mySet1.discard("car")
# mySet1.pop()
#del(mySet1)
#output=mySet2.union(mySet3)
#output=mySet2.intersection(mySet3)
output=mySet2.symmetric_difference(mySet3)

print(output)