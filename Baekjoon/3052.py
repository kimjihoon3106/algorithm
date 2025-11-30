values = []
cnt = 0

for i in range(10):
    num = int(input())
    values.append(num % 42)
    
values.sort()


for i in range(len(values) - 1):
    if values[i] == values[i+1]:
        values[i+1] = values[i]
    else:
        cnt = cnt + 1

print(cnt+1)          
            
            