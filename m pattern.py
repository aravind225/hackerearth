"""
m   m
mm mm
m m m
m   m
m   m
"""
n=int(input())
row=1
col=n
k=n//2+1
if n%2!=0:
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==row and (j==col and i<=k):
                print("m",end=" ")
                row=row+1
                col=col-1
            elif j==1 or j==n:
                print("m",end=" ")
            elif (i==j and i<=k):
                print("m",end=" ")
            
            else:
                print(" ",end=" ")
        print()
else:
    print("even number is doesn't exist")
