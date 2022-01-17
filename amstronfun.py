def amstrong(x):
    s=0
    temp=x
    while (temp>0):
        a=temp%10
        s+=a*a*a
        temp=temp//10
    if(x==s):
        print("the number is amstrong")
        
    else:
        print("the number is not amstrong")


y=int(input("enter the number"))
amstrong(y)
    
        

