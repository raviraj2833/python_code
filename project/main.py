import random

computer=random.choice([1,-1,0])

youstr=input("Enter your choice: ")
dic={"s":1,"w":-1,"g":0}
reversedic={1:"snake",-1:"water",0:"gun"}

you=dic[youstr]
print(f"you choose: {reversedic[you]}\nComputer choose: {reversedic[computer]}")

if(computer==you):
    print("It's draw")
else:
    if(computer==-1 and you==0):
        print("You loose")
    elif(computer==-1 and you==1):
        print("You win") 
    elif(computer==1 and you==0):
        print("You win") 
    elif(computer==1 and you==-1):
        print("You loose")     
    elif(computer==0 and you==-1):
        print("You win")
    elif(computer==0 and you==1):
        print("You loose")   
    else:
        print("Something wrong")           
                          