import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
time = list(map(int, input().split()))
time.sort()
res = 0
tmp = 0

for i in range(n):
    tmp += time[i]    
    res += tmp
    
print(res)
