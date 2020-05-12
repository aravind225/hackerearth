for _ in range(int(input())):
    a=int(input())
    if a>37:
        b=a
        while b%5!=0:
            b=b+1
        if b-a<3:
            print(b)
        else:
            print(a)
    else:
        print(a)
