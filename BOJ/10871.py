n, num = map(int, input().split())

l = list(map(int, input().strip().split()))

for i in l:
    if i < num:
        print(i, end=" ")
