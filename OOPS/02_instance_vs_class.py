class Employee:
    language="python" # this is class attribute
    salary=1200000
    
    
Ravi=Employee()
Ravi.language="C++" # This is instance attribute
print(Ravi.language,Ravi.salary)   # print language--> C++ due to instance attribute take preference over class attributes during assignment & retrieval
