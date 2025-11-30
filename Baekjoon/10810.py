n, m = map(int, input().split())
bucket = [0] * n

for i in range(m):
    st, lt, num = map(int, input().split())
    for i in range(st - 1, lt):
        bucket[i] = num


print(*bucket)