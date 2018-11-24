a = eval(input("Enter your Value: "))
if a < 40000:
    if a <= 10000:
        print("Samsung mobiles are available")
    elif a<= 20000:
        print("Lg mobiles are available")
    elif a<= 30000:
        print("Vivo mobiles are available")
    elif a<= 40000:
        print("Iphone mobiles are available")

else:
    print("Please Enter Valid Amount")