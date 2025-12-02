def get_layer(n):
    if n == 1:
        return 1
    start, end = 2, 7
    value = 2
    add = 6
    while True:
        if start <= n <= end:
            return value
        value += 1
        start = end + 1
        add += 6
        end += add

def main():
    n = int(input())
    print(get_layer(n))

if __name__ == "__main__":
    main()

"""
1 ~ 1 = 1
(1+1) ~ (6+1) = 2
((6+1)+1) ~ ((6+1)+12) = 3
(((6+1)+12)+1) ~ (((6+1)+12)+18) = 4
((((6+1)+12)+18)+1) ~ (((6+1)+12)+18)+24) = 5
"""