d={"Ravi":653483473,"Rahul":4359385,"raj": 4384364}

r=d["Ravi"]
print(r)
d["raju"]=65464646
print(d)

del d["Ravi"]
for i in d:
    print("name:",i,"phoneDir:",d[i])