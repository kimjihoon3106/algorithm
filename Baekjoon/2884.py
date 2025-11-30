H, M = map(int, input().split())

if H<0 or H>23:
    print("잘못된값")
else:
    if M<45:
        H-1
        60-(45-M)
        if H<=0:
            print(23,60-(45-M))
        else:
            print(H-1,60-(45-M))
    else:
        print(H,M-45)