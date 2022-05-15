import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

t = int(input())

def check(brackets):
    stack = list()
    
    for x in brackets:
        if x == '(':
            stack.append(x)
        
        else:
            if not stack:
                return False
            else:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
    return stack
                
for _ in range(t):
    brackets = list(input().rstrip())
    result = check(brackets)
    
    if result or result == False:
        print('NO')
    else:
        print('YES')