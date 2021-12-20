x=int(input("enter the value"))

while(x>0):
     for i in range(1,x+1):
        if(x%i==0):
            print("it is not a prime")
        else:
            print("number is prime")
            
