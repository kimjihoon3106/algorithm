import math

n1, n2 = map(int, input().split())

result = 1

for i in range(n2):
    result *= n1
    n1 -= 1

print(int(result / (math.factorial(n2))))