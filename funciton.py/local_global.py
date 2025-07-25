total=0 # it is global variable
def sum(a,b):
    print("a:",a)
    print("b:",b)

    total=a+b    # it is local variable
    print("total sum inside the function = " ,total)
    return a+b

r=int(sum(3,5))

print("total outside the function=",total)