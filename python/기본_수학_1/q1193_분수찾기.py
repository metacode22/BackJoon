import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
line = 1

while n > line:
    n -= line
    line += 1
    
if line % 2 == 0:
    x = n
    y = line - n + 1
else:
    x = line - n + 1
    y = n
    
print(f'{x}/{y}')