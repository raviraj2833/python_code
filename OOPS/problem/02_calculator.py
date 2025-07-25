class calculator:
    def __init__(self,n):
        self.n=n
    
    def square(self):
       print(f"the square is {self.n*self.n}")
    
    def cube(self):
         print(f"the cube is {self.n*self.n*self.n}")
    
    def sqrt(self):
        print(f"The sqrt is {self.n**1/2}") 
        
p=calculator(4)
p.square() 
p.cube()     
p.sqrt()  
        
        