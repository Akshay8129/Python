def neon(x):
    a=0
    sq=x*x
    print(sq)
    while(sq>0):
        a=a+sq%10
        sq=sq//10
    print(a)

    if(x==a):
         print("the number is neon number")
    else:
        print("the number is not a neon")



y=int(input("enter the number"))
neon(y)
