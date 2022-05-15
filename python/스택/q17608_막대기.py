import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())

sticks = list()
for _ in range(n):
    sticks.append(int(input()))
highest_stick = -sys.maxsize

stack = list()
cnt = 0

for x in sticks:
    while stack and x >= stack[-1]:
        stack.pop()
    stack.append(x)
    
print(len(stack))
        
    
