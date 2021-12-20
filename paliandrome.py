x=int(input("enter the number"))
temp=x
rev=0
while x>0:
    num=x%10
    rev=(rev*10)+num
    x=x//10
    if temp==rev:
     print("the number is paliandrome")
    else:
        print("the number is not paliandrome")
              
