# import sys
# sys.stdin = open('input.txt')
# input = sys.stdin.readline

# n = int(input())
# dp = [0] * (n + 1)

# for i in range(2, n + 1):
#     tmp = list()
#     tmp.append(dp[i - 1] + 1)
    
#     if i % 2 == 0:
#         tmp_2 = dp[i // 2] + 1
#         tmp.append(tmp_2)
    
#     if i % 3 == 0:
#         tmp_3 = dp[i // 3] + 1
#         tmp.append(tmp_3)
        
#     dp[i] = min(tmp)
    
# print(dp[-1])



# 리팩토링
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1)

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1
    
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
        
print(dp[-1])