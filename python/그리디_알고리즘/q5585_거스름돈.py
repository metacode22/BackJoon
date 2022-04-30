import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

change = 1000 - int(input())
coin = [500, 100, 50, 10, 5, 1]
cnt = 0

for i in range(len(coin)):
    if change // coin[i] != 0:
        cnt += change // coin[i]    
        change = change % coin[i]
    
print(cnt)
