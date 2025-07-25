# # how to prevent the print() function to print in new line
# print("a")
# print("b")
# print("c",end="")  
# print("d",end="")

def Display(name):
    print(f"{name}",end=" ")
n=3
while(n!=0):
    name=str(input("Enter the name: "))
    n=n-1    
Display(name)    
Display(name)    
Display(name)    
    
