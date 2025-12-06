import sys
input = sys.stdin.readline

n, m = map(int, input().split())

n_set = set()
result = set()

for _ in range(n):
    n_set.add(input().strip())

for _ in range(m):
    name = input().strip()
    if name in n_set:
        result.add(name)

print(len(result))
print("\n".join(sorted(result)))
