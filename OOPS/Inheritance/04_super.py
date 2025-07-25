class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a=1
    
class programar(Employee):
    def __init__(self):
        print("Constructor of Programar") 
    b=2


class manager(programar):
    def __init__(self):
        super().__init__() # CALL THE PARENT CLASS
        print("Constructor of manager")
    c=3 
    
    
o=manager()
print(o.a,o.b,o.c)                             