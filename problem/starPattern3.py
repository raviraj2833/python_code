n=int(input("Enter the number: "))

for i in range(1,n+1):
    print("" * (n-2),end="")
    if(i%2!=0):
        print("*" * n, end="")
    else:
        print("* " * (n-1),end="")
    print("\n")
    
    """
     ***
     * * n=3
     ***
     
    """
