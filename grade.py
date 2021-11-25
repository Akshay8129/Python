x1=int(input("enter the mark of first subject"))
x2=int(input("enter the mark of second subject"))
x3=int(input("enter the mark of third subject"))
x4=int(input("enter the mark of fourth subject"))
x5=int(input("enter the mark of fifth subject"))
       
total=x1+x2+x3+x4+x5
avg=total/5
print(f"the average mark is{avg}")
if avg>80:
       print("A grade")
elif avg>60:
       print("B grade")
elif avg>40:
       print("C grade")
else:
       print("Failed")
       
       
       
