n = float(input("Enter the value of n: "))
S = 0
for i in range(1, int(n) + 1):
    S += 10**i
print("The sum of the series is:", S)