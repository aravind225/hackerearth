n=int(input("enter the number:"))
j=1
s=n-1
for i in range(1,n+1):
    for l in range(1,s+1):
        print(" ",end=" ")
    for k in range(1,j+1):
        if (i%2==0 and (i==k)):
            print("+",end=" ")
        else:
            print("*",end=" ")
    print(end="\n")
    j=j+2
    s=s-1

"""
    *
   *+*
  *****
 ***+***
*********"""
        
       

                  
