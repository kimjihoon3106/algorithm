values = []
non_values = []

for i in range(28):
    num = int(input())
    values.append(num)
    
for i in range(1, 31):
    if i not in values:
        non_values.append(i)

non_values.sort()

print(non_values[0])
print(non_values[1])

"""
values = []
non_values = []
min = 100
for i in range(1,29) :
    num = int(input())
    values.append(num)
for i in range(1,30) :
    check = 0
    for value in values:
        if(i == value):
            check = 1
    if(check == 0):
        non_values.append(i)
for n_v in non_values:
    if n_v < min:
        min = n_v
print(min)
index_num = non_values.index(min)
del non_values[index_num]
min = 100
for n_v in non_values:
    if n_v < min:
        min = n_v
print(min)
"""