import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
nums = [[0] + list(map(int, input().split())) for _ in range(n)]
for k in range(n):
    nums[k] = nums[k] + [0] * (n - 1 - k)
nums.insert(0, [0] * (n + 1))
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + nums[i][j]
        
print(max(dp[-1]))