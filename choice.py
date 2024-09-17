choice=input("enter the choice(1/2/3/4):")
if choice=="1":
    a=int(input("enter the value  of a"))
    b=int(input("enter the value  of b"))
    print(a+b)
elif choice=="2":
    a=int(input("enter the value  of b"))
    b=int(input("enter the value  of b"))
    print(a-b)
elif choice=="3":
    a=int(input("enter the value  of a"))   
    b=int(input("enter the value  of b")) 
    print(a*b)
elif choice=="4":
    a=int(input("enter the value  of a"))
    b=int(input("enter the value  of b"))
    print(a/b)
else:
    print("not found")