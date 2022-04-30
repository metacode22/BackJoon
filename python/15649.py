import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(range(1, n + 1))
visited = [0] * m

# def DFS(level):
#     if level == m:
#         for i in range(0, m):
#             if visited[i] != 0:
#                 print(num[i], end = '')
#                 print()
#         return
        
#     else:
#         visited[level] = 1
#         DFS(level + 1)
#         visited[level] = 0
#         DFS(level + 1)

def DFS(level):
    if level == m:
        for i in range(0, m):
            if visited[i] != 0:
                print(num[i], end='')
                print()
        return
        
    else:
        for i in range(1, n + 1):
            visited[level] = 1
            DFS(level + 1)
            
DFS(0)

