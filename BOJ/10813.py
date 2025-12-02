bucket_num, changes = map(int, input().split())

values = [1, 2, 3, 4, 5]

for i in range(changes):
    change_1, change_2 = map(int, input().split())
    yet = values[change_1-1]
    values[change_1-1] = values[change_2-1]
    values[change_2-1] = yet

print(*values)