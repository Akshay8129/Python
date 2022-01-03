x=int(input("enter the value"))
n=1
c=0
while(n<=x):
    if(x%n==0):
        c=c+1
    n=n+1
if(c==2):
    print("the number is prime")
else:
    print("the number is not prime")
