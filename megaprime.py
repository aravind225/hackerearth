n=int(input("enter the number:"))
c=0
i=1
rev=0
p=1
u=0
while i<=n:
    r=n%i
    if r==0:
        c=c+1
    i=i+1
if c==2:
    print("prime")
    while n:
        r=n%10
        n=n//10
        #print(r)
        while p<=r:
            a=r%10
            if a==0:
                u=u+1
            p=p+1
            
        
        
