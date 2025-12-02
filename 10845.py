from collections import deque

n = int(input())

queue = deque()
front = 0
back = 0
output = []

for i in range(1, n+1):
    line = input().split()

    act = line[0]
    num = line[1] if len(line) == 2 else None

    if act == "push":
        queue.append(int(num))
    elif act == "pop":
        if queue:
            output.append(queue.popleft())
        else:
            output.append("-1")
    elif act == "size":
        output.append(len(queue))
    elif act == "empty":
        output.append(0 if queue else 1)
    elif act == "front":
        output.append(queue[0] if queue else -1)
    elif act == "back":
        output.append(queue[-1] if queue else -1)

print("\n".join(map(str, output)))