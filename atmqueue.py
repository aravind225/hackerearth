n=int(input())
l=list(map(int,input().split()))
c=1
for i in range(len(l)-1):
    if l[i+1]<l[i]:
        c=c+1
print(c)
        
