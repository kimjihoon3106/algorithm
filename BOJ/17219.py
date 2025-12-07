import sys
input = sys.stdin.readline

n, m = map(int, input().split())

table = {}
result = []

for _ in range(n):
    email, pw = input().split()
    table[email] = pw

for i in range(m):
    email = input().strip()
    result.append(table[email])

print("\n".join(result))
