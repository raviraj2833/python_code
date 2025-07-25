class programer:
    company="Microsoft"
    def __init__(self,company,name ,salary,language): # dunder method which is automatically called 
        self.company=company
        self.name=name
        self.salary=salary
        self.language=language

p=programer("Microsoft","Ravi","50lakh","C++")
print(p.company,p.name,p.salary,p.language)
p=programer("Microsoft","Rahul","10lakh","C++")
print(p.company,p.name,p.salary,p.language)
        