import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
visited = [0] * (n + 1)
res = [0] * n
def DFS(level):
    if level == n:
        for j in range(level):
            print(res[j], end = ' ')
        print()
        return
    
    else:
        for i in range(1, n + 1):
            if visited[i] == 0:
                visited[i] = 1
                res[level] = i
                DFS(level + 1)
                visited[i] = 0
        
DFS(0)