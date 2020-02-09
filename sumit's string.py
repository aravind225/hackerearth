
t=int(input())
for _ in range(t):
    l=list(input())
    f=0
    for i in range(len(l)-1):
        a=ord(l[i])
        b=ord(l[i+1])
        if(a==b+1):
            f=0
        elif(a==b-1):
            f=0
        elif(a==122 and b==97):
            f=0
        elif(a==97 and b==122):
            f=0
        else:
            f=1
            break
    if(f==1):
        print("NO")
    else:
        print("YES")
