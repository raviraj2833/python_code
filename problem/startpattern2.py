n=int(input("Enter the number: "))

for i in range(1,n+1):
    print("" * (n-2),end="")
    print("*" * i,end="")
    print("\n")
    
    """
    *
    **
    ***
     
    """