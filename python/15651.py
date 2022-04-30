import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())

def DFS(level):
    if level == m:
        print(*res)
        return
    else:
        for i in range(1, n + 1):
            res[level] = i
            DFS(level + 1)
            res[level] = 0
            
res = [0] * (m)
DFS(0)