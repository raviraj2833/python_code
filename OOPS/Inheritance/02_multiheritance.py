class employee:  # base class
    company="Google"
    salary=920000
    def show(self):
        print(f"the company-name  {self.company} and the salary {self.salary}")


class coder:
    language="python"
    def language_1(self):
        print(f"Out of all languages {self.language} is very famous")     
     
     
     
     
class programer(employee,coder): # derive or child class or here multiple inheritance is happen
    # company="Microsoft"
    def showlangauge(self):
         print(f"the company-name  {self.company} and the salary {self.salary}")
             
         
         
a=employee()
b=programer()
b.show()
b.showlangauge()
b.language_1()

