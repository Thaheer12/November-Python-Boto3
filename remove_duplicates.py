duplicate_list=[1,2,3,4,5,1,"f",3,5,8,7,8,"f",9]
list=[]
for x in duplicate_list:
    if x not in list:
        list.append(x)
print(list)
