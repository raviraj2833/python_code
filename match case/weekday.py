n=int(input("Enter the number: "))
match n:
    case 0: 
        print("Monday")
    case 1:
        print("Tuesday")
    case 2:
        print("Wednesday")
    case 3:
        print("Thursday")   
    case 4:
        print("Friday")  
    case 5:
        print("Saturday")               
    case 6:
        print("Sunday")
    
    case _:
        print("Invalid day")    