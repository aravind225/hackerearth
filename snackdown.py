t=int(input())
z=[]
for _ in range(t):
    n=int(input())
    ml=list(map(int,input().split()))
    fl=list(map(int,input().split()))
    ml.remove(ml[0]),fl.remove(fl[0])
    ol=[i for i in range(1,n+1)]
    for i in ol:
        if i in ml or i in fl:
            p="YES"
        else:
            p="NO"
            break
    z.append(p)
for j in z:
    print(j)
