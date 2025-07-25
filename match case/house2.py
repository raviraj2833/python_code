name =input("what's your name? ")

match name:
    case "Ravi" | "Vishal" | "Monu" | "Sonu" | "Vishal":
        print("Yadav' house")
    case "rohan":
        print("Gupta's house") 
    case _:
        print("who? ")                   