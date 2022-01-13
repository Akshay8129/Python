def sum_of_three(x,y,z):
    sum1=x+y+z
    if(x==y==z):
    
        sum=sum1*3
        print(sum)
    else:
        print("the numbers are not equal",sum1)
    


a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=int(input("enter the third number"))
sum_of_three(a,b,c)

