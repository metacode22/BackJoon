import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def DFS(x):
    if x == 0:
        return 0
        
    if x == 1 or x == 1:
        return 1
        
    else:
        return DFS(x - 1) + DFS(x - 2)
        
    
n = int(input())
print(DFS(n))