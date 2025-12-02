def get_lst(i):
    lst_str = list(str(i))
    lst = list(map(int, lst_str))
    return lst

def get_s(n):
    for i in range(1,n+1):
        if i + sum(get_lst(i)) == n:
            return i
        
def main():
    n = int(input())
    if get_s(n) is not None: print(get_s(n))
    else: print("0")


if __name__ == "__main__":
    main()