import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

k, n = map(int, input().split())
a = []
for i in range(k):
    a.append(int(input()))
a.sort()

def count(len):
    cnt = 0
    for i in a:
        cnt += i//len
    return cnt

lt = 1
rt = max(a)
res = 0
while lt <= rt:
    mid = (lt + rt)//2
    if count(mid) >= n:
        lt = mid + 1
        res = mid
    else:
        rt = mid - 1
        
print(res)