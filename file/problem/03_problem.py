def generateTable(n):
    table=" "
    for i in range(1,20):
        table+=f"{n} X {i} ={n*i}\n"
        
        
    with open(f"table/table_{n}.txt","w") as f:
        f.write(table) 
      
      
        
for i in range(2,21):
    generateTable(i)    
            