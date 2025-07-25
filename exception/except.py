def get_in():
    while True:
            try:
           x=int(input("what's the x? "))
    except ValueError:
       print("x is not an integer")    
    else:
        break 
    
print(f"x is {x}") 