n, m = map(int, input().split())
board = []
rewrite = []

for _ in range(n):
    board.append(input())


"""
BWB # w_f + 1, w_f + 1, w_f + 1
WBW # w_f + 1, w_f + 1, w_f + 1
BWB # w_f + 1, w_f + 1, w_f + 1
b_f = 0, w_f = 9
min => 0
"""

for i in range(n - 7):
    for j in range(m - 7):
        b_f = 0 # B
        w_f = 0 # W

        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:
                    if board[a][b] != 'B':
                        b_f += 1
                    if board[a][b] != 'W':
                        w_f += 1
                else:
                    if board[a][b] != 'W':
                        b_f += 1
                    if board[a][b] != 'B':
                        w_f += 1
        rewrite.append(b_f)
        rewrite.append(w_f)

print(min(rewrite))