#tuple- store multiple items in a single variable 
#non homogeneous
#ordered
#unchangble/ immutable
#allows duplicate values

tuple1= ("car","bike","boat","jet")
list1=list(tuple1)
list1.insert(2,"atul")
tuple2=tuple(list1)
print(tuple2)