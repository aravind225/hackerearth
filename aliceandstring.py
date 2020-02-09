s=str(input())
s1=str(input())
c=0
for i in range(len(s)):
    if len(s)!=len(s1):
        print('NO')
        break
    if s[i]>s1[i]:
        print('NO')
        break
    else:
        c=c+1
if c==len(s):
    print('YES')
