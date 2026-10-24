"""

list1=["Messi", "Neymar", "Anu"]
list2=["Anu", "Mbappe", "Messi"]
result=list(set(list1 + list2))
result.sort()
print(result)

"""

"""
var=(4,3,2,1,7,6,8,5,9)
x=list(var)
x.sort()
print(x)
print("Maximum number:",x[len(x)-1])
print("Minimum number:",x[0])
print("Difference:",x[len(x)-1]-x[0])

"""
"""

var=['Yes','No','Yes','Yes','No','Yes']
x=str(var)
x=x.replace('Yes','0')
x=x.replace('No','1')
print(x)
out={0:x.count('0'),1:x.count('1')}
print(out)

"""

units=int(input("ENTER THE UNIT VALUE: "))
if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = 200 + (units - 100) * 5
else:
    bill = 700 + (units - 200) * 8
if bill > 1000:
    electrici_bill = bill + bill * 10 / 100
else:
    electrici_bill = bill
print("Final electricity bill:", electrici_bill)