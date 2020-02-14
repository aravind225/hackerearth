n=input()
a=len(n)//2
b=len(n)//2+1
if len(n)%2==1:
    c=n[:a]
    d=n[a+1:]
else:
    c=n[:a]
    d=n[a:]
h=[i for i in c]
e=[i for i in d]
e.reverse()
if h==e:
    print("yes")
else:
    print("no")
