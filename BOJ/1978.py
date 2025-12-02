n = int(input())
lst = list(map(int, input().split()))
lst = lst[:n]
sum = 0

def get_s(n):
    s_lst = []
    for i in range(2, n+1):
        if n % i == 0:
            s_lst.append(i)
    
    return s_lst


for i in lst:
    if len(get_s(i)) == 1:
        sum += 1

print(sum)