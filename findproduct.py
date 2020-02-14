n=int(input())
l=list(map(int,input().split()))
ans=1
for i in l:
    ans=(ans*i)%(10**9+7)
print(ans)
