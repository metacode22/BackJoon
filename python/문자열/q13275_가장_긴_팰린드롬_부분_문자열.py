import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def expand(lt, rt):
    while lt >= 0 and rt <= len(s) - 1 and s[lt] == s[rt]:
        lt -= 1
        rt += 1
        
    return s[lt + 1:rt]

s = input().rstrip()

# 예외 처리
if len(s) < 2 or s == s[::-1]:
    print(len(s))

else:  
    res = -sys.maxsize
    for i in range(len(s)):
        res = max(res, len(expand(i, i + 1)), len(expand(i, i + 2)))
        
    print(res)