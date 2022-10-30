#type1
cars = ["Nano","Ford","Tata","BMW","Thar"]

for i in cars:
    print(i)
    if i=="Tata":
        break

#type2
bikes = ["TVS","Hayabusa","Splendor","Pulsar","Yamaha","KTM","chetak"]

for v in bikes:
    if v=="Pulsar":
        continue
    print(v)

#type3
for i in range(2,11,2):
    print(i)