class employee:
    a=1
    @classmethod # decorator
    def show(cls):
        print(f"the class attribute of a: {cls.a}")
        
    @property # abstraction means that we have hidden the implementation details
    def name(self):
        return f"{self.fname} {self.lname}" 
    
    @name.setter  # Encapsulation means that you can't see the implementation details
    def name(self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]

e=employee()
e.a=45 # instance attribute
e.name="Ravi yadav"
print(e.fname,e.lname)
e.show()     