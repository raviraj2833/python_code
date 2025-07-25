from operator import truediv


tup= (3,4,6,7,2,"Green",truediv)
print(len(tup))
print(tup[-2])
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[4])
print(tup[5])

if 300 in tup:
    print("Yes it is found in tupple")
else:
    print("Not found")

tup2=tup[0:4]
print(tup2)    