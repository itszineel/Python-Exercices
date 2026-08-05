x=float(input("enter an number: "))
y=float(input("enter an number: "))
if x>0 and y>0 or x<0 and y<0:
    temp=x
    x=y
    y=temp
else:
    temp=x+y
    y=x*y
    x=temp
print("The new value of x is: ",x)
print("The new value of y is: ",y)