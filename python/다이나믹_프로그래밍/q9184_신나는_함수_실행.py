import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
        
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
        
    # 입력값 a, b, c가 음수 혹은 20 이상일 수 있으므로 DP 구문을 여기에 넣어줘야 한다.
    if dp[a][b][c] != 0:
        return dp[a][b][c]
        
    if a < b < c:
        dp[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return dp[a][b][c]
        
    else:
        dp[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
        return dp[a][b][c]
        
while True:
    x, y, z = map(int, input().split())
    
    if x == y == z == -1:
        break
    
    dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]
    w(x, y, z)
    
    print(f'w({x}, {y}, {z}) = {w(x, y, z)}')