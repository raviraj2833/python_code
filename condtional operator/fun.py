def main():
    x=int(input("what's the value of x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")  
        
def is_even(n):
    return True if n % 2 ==0 else False
            
main()            