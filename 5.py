# f(x) = 4x^2+2x+9
coeff = [4, 2, 9]

n = int(input("Enter value of n: "))

degree = len(coeff) - 1
result = 0

for c in coeff:
    result += c * (n ** degree)
    degree -= 1

print("Value of polynomial =", result)