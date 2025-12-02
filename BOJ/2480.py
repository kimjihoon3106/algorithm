f, s, t = map(int, input().split())
l = [f, s, t]

if f == s == t:
    print(10000 + f * 1000)
    
elif ( f == s and f != t) :
    print(1000 + f * 100)
    
elif (f == t and f != s) :
    print(1000 + f * 100)

elif (s == t and s != f) :
    print(1000 + s * 100)

else:
    max = 0
    for i in l:
        if (max < i ):
            max = i
    
    print(max * 100)