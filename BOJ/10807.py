a = int(input())
sum = 0

asdf = list(map(int, input().strip().split()))

cn = int(input())

for i in asdf:
    if cn == i:
        sum += 1

print(sum)