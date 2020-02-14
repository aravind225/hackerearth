"""
 6666
6
66666
6   6
66666
"""
n=int(input("enter the odd number:"))
k=n//2+1
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or j==1 or i==n or i==k:
            print("6",end="")
        elif j==n and i>k :
            print("6",end="")
        else:
            print(" ",end="")
    print()
