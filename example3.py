a=[1,"a","b",5,True,6,9,10,"somu"]
s =[]
even = []
odd = []
string=[]
boolian=[]
for x in a:
    if type(x) == int:
        s.append(x**2)
    elif type(x)==bool:
        boolian.append(x)
    else:
        string.append(x)

print(s)
print(string)
print(boolian)
for y in s:
    if y%2 == 0:
        even.append(y)
    else:
        odd.append(y)

print(even)
print(odd)