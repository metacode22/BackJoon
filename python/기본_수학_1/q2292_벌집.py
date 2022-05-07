import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
tmp = n
n -= 1
idx = 1
cnt = 0

while n >= 0:
    cnt += 1
    
    n = n - 6 * idx
    idx += 1
    
    if n <= 0:
        break
    
if tmp == 1:
    print(1)
elif tmp <= 7:
    print(2)
else:
    print(cnt + 1)