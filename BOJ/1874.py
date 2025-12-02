# 첫줄에 n을 입력하면 1부터 n이 들어감
# 두번째줄부터 1~n사이에 숫자를 입력해 스탭의 결과값을 적으면 됨
# 예 n = 3 이고 2 3 1을 넣으면 결과값은 + + - + - - 이다 (+ = push, - = pop)
# push 하는 순서가 오름차순임을 기억

n = int(input())
lst = []
for i in range(1, n+1):
    lst.append(int(input()))

stack = []
current = 1
result = []
possible = True

for top in lst:
    while current <= top:
        stack.append(current)
        result.append("+")
        current += 1
    
    if stack[-1] == top:
        stack.pop()
        result.append("-")
    else:
        possible = False
        break;

if possible == False:
    print("NO")
else:
    print((" ").join(result))