def calculate(exp):
    total=0
    for i in exp:
       total=total+i
    return total

list1_exp = [1,2,3,4]
list2_exp = [2,3,4,5]

list1_total=calculate(list1_exp)
list2_total=calculate(list2_exp)

print(list1_total)
print(list2_total)
