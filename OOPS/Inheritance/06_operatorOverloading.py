class number:
    def __init__(self,n):
        self.n=n
    
    def __add__(self,num):
        return self.n + num.n 
    
    def __mul__(self,num):
        return self.n * num.n
    
    def __sub__(self,num):
        return self.n - num.n

n=number(0)
m=number(12)
print(n*m)
print(n+m)
print(n-m)
        