import sys, math
sys.stdin = open('input.txt')
input = sys.stdin.readline

strings = input().rstrip().lower()
res = 0

for string in strings:
    if string in ['a', 'b', 'c']:
        res += 3
        
    if string in ['d', 'e', 'f']:
        res += 4
        
    if string in ['g', 'h', 'i']:  
        res += 5
        
    if string in ['j', 'k', 'l']:
        res += 6
        
    if string in ['m', 'n', 'o']:
        res += 7
        
    if string in ['p', 'q', 'r', 's']:
        res += 8
        
    if string in ['t', 'u', 'v']:
        res += 9 
        
    if string in ['w', 'x', 'y', 'z']:
        res += 10

print(res)

# for string in strings:
#     res += math.ceil(((ord(string) - 96) // 3)) + 2
    
# print(res)
