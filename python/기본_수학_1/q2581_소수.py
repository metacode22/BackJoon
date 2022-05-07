import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

res = list()
m = int(input())
n = int(input())

for i in range(m, n + 1):
    if i == 1:
        continue
    
    if i == 2:
        res.append(i)
        continue
    
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        res.append(i)
            
if not res:
    print(-1)
else:
    print(sum(res))
    print(min(res))