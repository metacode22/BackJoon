import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

string = input().rstrip()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
res = 0
i = 0

while i < len(string):
    if ''.join(string[i:i+2]) in croatia:
        res += 1
        i += 2
    
    elif ''.join(string[i:i+3]) in croatia:
        res += 1
        i += 3
        
    else:
        res += 1
        i += 1
        
print(res)
        
    