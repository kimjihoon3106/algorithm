import sys
input = sys.stdin.readline

n, k = map(int, input().split())

cnt = 0
nums = set()

for _ in range(n):
    nums.add(int(input().strip()))

lst = sorted(nums)

while k > 0:
    used = False
    for i in range(len(lst)-1, -1, -1):
        if lst[i] <= k:
            cnt += 1
            k -= lst[i]
            used = True
            break

    if not used:
        break

print(cnt)