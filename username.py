username = ["suresh", "mahesh", "somu"]

for y in range(3):
    a = input("Enter ur username: ")
    if a in username:
        b= input("Enter Password:")
        if (a== "suresh" and b == "1234") or (a== "mahesh" and b == "3214") or (a== "somu" and b == "5412"):
            print("Congtrats  login successfull ")
            break
        else:
            print("Enter valid password")

    else:
        print("Enter valid username")
        continue
