from math import sqrt
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))
delta = b**2 - 4*a*c
if delta > 0:
    x1 = (-b + sqrt(delta)) / (2*a)
    x2 = (-b - sqrt(delta)) / (2*a)
    print("The solutions are ", x1, "and", x2)
elif delta == 0:
    x = -b / (2*a)
    print("The solution is ", x)   
else:
    print("There are no real solutions")