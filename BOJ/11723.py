import sys

input = sys.stdin.readline
n = int(input())
S = set()

for _ in range(n):
    raw = input().split()
    act = raw[0]

    if act in ("add", "check", "remove", "toggle"):
        num = int(raw[1])

    if act == "add":
        S.add(num)

    elif act == "check":
        sys.stdout.write("1\n" if num in S else "0\n")

    elif act == "remove":
        S.discard(num)

    elif act == "toggle":
        if num in S:
            S.remove(num)
        else:
            S.add(num)

    elif act == "empty":
        S.clear()

    elif act == "all":
        S = set(range(1, 21))