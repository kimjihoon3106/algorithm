n = int(input())
result = []

# dp[1] = dp[0] + 1
# dp[2] = dp[1] + 1, dp[0] + 2
# dp[3] = dp[2] + 1, dp[1] + 2, dp[0] + 3

# n = 3
# dp = [0, 0, 0]
# 1 : dp[1] = dp[1] + dp[0] = 0 + 1 = 1
# 2 : dp[2] = dp[2] + dp[1] + dp[0] = 0 + 1 + 1 = 2
# 3 : dp[3] = dp[3] + dp[2] + dp[1] + dp[0] = 0 + 2 + 1 + 1 = 4

for i in range(n):
    num = int(input())

    dp = [0] * (num + 1)
    dp[0] = 1

    for j in range(1, num + 1):
        if j - 1 >= 0:
            dp[j] += dp[j - 1]
        if j - 2 >= 0:
            dp[j] += dp[j - 2]
        if j - 3 >= 0:
            dp[j] += dp[j - 3]

    result.append(dp[num])

print("\n".join(map(str, (result))))
