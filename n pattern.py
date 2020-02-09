"""
N   N
NN  N
N N N
N  NN
N   N
"""
n=int(input("enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if (i==j) or (j==1)or (j==n):
            print("N",end="")
        else:
            print(" ",end="")
    print()
        
