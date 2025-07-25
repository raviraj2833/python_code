class Employee:
    language="python" # this is class attribute
    salary=1200000
    
    def __init__(self,name ,salary,language): # dunder method which is automatically called 
        self.name=name
        self.salary=salary
        self.language=language
        print("I am Ravi")
    
    def getinfo(self):
        print(f"language is {self.language}\nsalary is {self.salary}")
        
    def greet(self):    
        print("good morning!!")
        
    
    
Ravi=Employee("Ravi",1000000,"java") # This is instance attribute
print(Ravi.name,Ravi.salary,Ravi.language)