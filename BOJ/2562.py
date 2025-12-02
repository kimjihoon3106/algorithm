
values = []

for i in range(9) :
    num = int(input())
    values.append(num)

print(f"{max(values)} \n{(values.index(max(values)))+1}")