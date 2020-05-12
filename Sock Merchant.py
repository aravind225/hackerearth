def fn(n):
    return (n-1)//2
n=int(input())
ar=(list(map(int,input().split())))
b=sorted(set(ar))
c=0
for i in b:
    a=ar.count(i)
    if a%2==0:
        c=c+(a//2)
    elif a%2==1 and a!=1:
        c=c+fn(a)
print(c)
        
