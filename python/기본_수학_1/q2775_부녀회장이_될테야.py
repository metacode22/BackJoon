import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    
    map = [[0] * n for _ in range(k + 1)]
    
    for l in range(n):
        map[0][l] = l + 1
        
    for i in range(1, k + 1):
        for j in range(n):
            map[i][j] = sum(map[i - 1][:j + 1])
            
    print(map[k][n - 1])
        
    