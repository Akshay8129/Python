def sum(x):
    s=0
    while x>0:
        a=x%10
        s=s+a
        x=x//10
    print(s)


y=int(input("enterr the number"))
sum(y)
    

