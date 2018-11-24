# a= "Welcome to python"
# for x in a:
#     print(x)

# a= [10,20,21,22,36,85,74,99,87,88,45,25,36]
# Even = []
# Odd = []
# for x in a:
#     if x%2 == 0:
#         if x%5 ==0:
#             Even.append(x)
#     else:
#         Odd.append(x)
# print(Even)
# print(Odd)
a=1
b=eval(input("Enter yor VALUE: "))
while a <= b:
    print(a)
    a=b*a
    b=b-1
