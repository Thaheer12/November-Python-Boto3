a = ['a','b',"c",1,'z',3,'w']
list=[]
for x in a:
    if type(x) == str:
        continue
    list.append(x)
print(list)