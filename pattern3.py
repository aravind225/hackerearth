n=int(input("enter the number:"))
i=1
j=1
while j<=n:
    print(i,end=" ")
    if i==n:
        print(end="\n")
        j=j+1
        i=1
    else:
        i=i+1
    
    
