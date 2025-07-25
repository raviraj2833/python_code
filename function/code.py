from curses.ascii import isupper, islower

a=input("Enter something: ")
if a.isdigit():
   print(f"{a} is a number")
elif a.isalpha():
    if a.isupper():
        print(f"{a} is in Uppercase character..")
    else:
        print(f"{a} is in Lowercase character...")
else:
    print("Neither char nor number...")



