a=int(input("enter the 1st number:"))
b=int(input("enter the 2nd number:"))
print("Add:1 sub:2 div:3 mul:4 exit:0")
while True:
    c=int(input("enter the required operation:"))
    if c==1:
        print(a+b)
    if c==2:
        print(a-b)
    if c==3:
        print(a/b)
    if c==4:
        print(a*b)
    if c==0:
        print("exit")
        break
    
