hour, second = map(int, input().split())
time = int(input())
turn = 0

if(0<=hour and hour<=23) and (0<=second and 59 >= second):
    turn = int((second + time) / 60)
    r_hour = int(hour + turn)
    r_second = int(second + time - 60 * turn)
    
    if(r_hour < 24):
        print(r_hour, r_second)
    else:
        print(r_hour-24, r_second)
        