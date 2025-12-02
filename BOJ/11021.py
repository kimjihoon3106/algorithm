import sys
a = int(sys.stdin.readline())
value = []

for i in range(a):
    x, y = map(int, sys.stdin.readline().split())
    value.append(x+y)

for i, value in enumerate(value):
    print(f"Case #{i+1}: {value}")