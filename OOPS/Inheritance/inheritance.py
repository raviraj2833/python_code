class employee:  # base class
    company="Google"
    def show(self):
        print(f"the name  {self.name} and the salary {self.salary}")


# class progammar:
#     company="Microsoft"
#     def show(self):
#         print(f"the name  {self.name} and the salary {self.salary}")
        
#     def showlangauge(self):
#         print(f"the name  {self.name} and the salary {self.language}")
         
class programer(employee): # derive or child class
    # company="Microsoft"
    def showlangauge(self):
         print(f"the name  {self.name} and the salary {self.language}")
             
         
         
a=programer()
b=employee()
print(a.company,b.company) 
