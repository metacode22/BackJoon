# DFS 방법이 바로 안 떠올라 BFS로 시도
# DP로 어떻게 비교해서 BFS를 빠르게 끝낼 지 모르겠음.(어떻게 바로 값이 반환될지)
# 36%에서 시간 초과
import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def BFS(start, end, cnt):
    q = deque()
    q.append((start, end, cnt))
    if cnt > visited[start][end]:
        visited[start][end] = cnt
        
    while q:
        x, y, cnt_now = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and bamboo[nx][ny] > bamboo[x][y]:
                if cnt_now + 1 > visited[nx][ny]:
                    visited[nx][ny] = cnt_now + 1
                    q.append((nx, ny, cnt_now + 1))
                
n = int(input())
bamboo = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        BFS(i, j, 1)
        
res = -sys.maxsize
for i in visited:
    if max(i) > res:
        res = max(i)
        
print(res)



# DFS, 미해결.
# import sys
# sys.stdin = open('input.txt')
# input = sys.stdin.readline

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# def DFS(start, end, cnt):
#     if bamboo[start][end] > 
    
#     x = start
#     y = end
    
#     for i in range(n):
#         nx = x + dx[i]
#         ny = y + dy[i]
        
#         if 0 <= nx < n and 0 <= ny < n and bamboo[nx][ny] > bamboo[x][y]:
#             DFS(nx, ny, cnt + 1)

# n = int(input())
# bamboo = [list(map(int, input().split())) for _ in range(n)]
# dp = [[0] * n for _ in range(n)]

# for i in range(n):
#     for j in range(n):
#         DFS(i, j, 0)