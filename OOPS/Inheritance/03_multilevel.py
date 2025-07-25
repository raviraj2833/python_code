class clerk:
    salary=20000
    def salary_1(self):
        print(f"salary of clerk is {self.salary}")


class Employee(clerk):
    def salary_2(self):
        print(f"salary of Employee is {self.salary}")
                
class manager(Employee):
    def salary_3(self):
        print(f"salary of manager is {self.salary}")


a=clerk()
b=Employee()
c=manager()
c.salary_1()                
c.salary_2()                
c.salary_3()                