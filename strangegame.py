t=int(input())
h=[]
for _ in range(t):
    a,b=map(int,input().split())
    l=list(map(int,input().split()))
    la=list(map(int,input().split()))
    c=max(la)+1
    z=[]
    for i in range(len(l)):
        if l[i]<c:
            d=c-l[i]
            z.append(d*b)
    h.append(sum(z))
for j in h:
    print(j)

            
