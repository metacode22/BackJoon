# <나의 풀이> : n이 1일 경우를 예외처리함.
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    
    if n == 1:
        print(1)
    
    else:
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 1
        
        for i in range(3, n + 1):
            dp[i] = dp[i - 2] + dp[i - 3]
            
        print(dp[n])



# dp 공간을 처음부터 아예 크게 만듦.     
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    
    dp = [0] * 101
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    
    for i in range(4, n + 1):
        dp[i] = dp[i - 2] + dp[i - 3]
        
    print(dp[n])