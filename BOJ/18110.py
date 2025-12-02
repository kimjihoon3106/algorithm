n = int(input())
lst = [int(input()) for _ in range(n)]
lst.sort()

d = int((n * 0.15) + 0.5)

lst = lst[d:n-d]

average = 0

if len(lst) == 0:
    average = 0
else:
    average = int(sum(lst) / len(lst) + 0.5)

print(average)