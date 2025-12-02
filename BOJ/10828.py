n = int(input())

stack = []
output = []

for i in range(1, n+1):
    line = input().split()


    act = line[0]
    num = line[1] if len(line) == 2 else None

    if act == "push":
        stack.append(num)
    elif act == "pop":
        if stack:
            output.append(stack[-1])
            stack.pop()
        else:
            output.append("-1")
    elif act == "size":
        output.append(len(stack))
    elif act == "empty":
        output.append(0 if stack else 1)
    elif act == "top":
        output.append(stack[-1] if stack else "-1")

print("\n".join(map(str, output)))