x = int(input("Enter the value of x: "))
while x == 0 or x < 0:
    x = int(input("Enter a non-zero positive value for x: "))
    if x != 0 and x > 0:
        break
factorial = 1
for i in range(1, x + 1):
    factorial *= i
print("The factorial of", x, "is :", factorial)