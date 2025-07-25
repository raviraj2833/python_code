# Hello here we are using match-Case statement

x=int(input("Enter the value of x: "))

match x:
    case 0:
      print("x is zero")
    case 1:
      print("case is one")
      
    case _: print(x)  
            