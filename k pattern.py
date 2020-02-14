"""
K  K
K K
KK
K K
K  K"""
n=int(input("enter the rows:"))
p=n//2+1
k=n-2
h=k
b=p
o=b-1
row=1
if n%2!=0:
    for i in range(1,n+1):
        for j in range(1,k+1):
            if ( i==row and j==h and i<=p):
                print("K",end="")
                row=row+1
                h=h-1
            elif i==b and j==o:
                print("K",end="")
                b=b+1
                o=o+1
            elif j==1:
                print("K",end="")
            else:
                print(" ",end="")
        print()
else:
    print("one  and even number doesn't print")
