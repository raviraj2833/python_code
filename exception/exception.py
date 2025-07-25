from enum import nonmember

x=input("Enter the number:")
y=input("Enter the number:")
try:
      z = int(x) / int(y)
except Exception as e:
     print("exception occured :",e)
     z=None
print("Division of number:",z)

`
