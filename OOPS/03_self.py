class Employee:
    language="python" # this is class attribute
    salary=1200000
    
    def getinfo(self):
        print(f"language is {self.language}\nsalary is {self.salary}")
        
    def greet(self):    
        print("good morning!!")
        
    
    
Ravi=Employee()
Ravi.language="C++" # This is instance attribute
Ravi.greet()
Ravi.getinfo()
# Employee.getinfo(Ravi)