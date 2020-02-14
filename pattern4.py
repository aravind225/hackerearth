n=int(input())
i=1
j=1
m=0
while True:
    print(j,end=" ")
    if j+m==i:
        m=j
        i=1
        print("\n")
        j=j+1
        if j>n:
            break
    else:
        i=i+1
        
        
