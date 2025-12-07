n = int(input())
time_lst = list(map(int, input().split()))

time_lst.sort()

result = 0 
t_sum = 0

for t in time_lst:
    t_sum += t
    result += t_sum

print(result)