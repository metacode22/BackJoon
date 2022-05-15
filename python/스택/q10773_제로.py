import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

k = int(input())
stack = list()

for _ in range(k):
    x = int(input())
    if x != 0:
        stack.append(x)
    else:
        stack.pop()
        
print(sum(stack))