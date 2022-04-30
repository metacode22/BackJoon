import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()
m = int(input())
b = list(map(int, input().split()))

lt = 0
rt = n - 1

for i in b:
    lt = 0
    rt = n - 1
    while lt <= rt:
        mid = (lt + rt)//2
        if a[mid] == i:
            print(1, end = ' ')
            break
        elif a[mid] < i:
            lt = mid + 1
        else:
            rt = mid - 1
        
    else:
        print(0, end = ' ')
        