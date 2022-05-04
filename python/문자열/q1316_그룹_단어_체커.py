import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
cnt = 0

for _ in range(n):
    string = input().rstrip()
    tmp = list()
    
    for i in range(len(string)):
        if string[i] not in tmp:
            tmp.append(string[i])
            
        elif string[i] in tmp and string[i] == string[i - 1]:
            continue
        
        else:
            break
    else:
        cnt += 1
        
print(cnt)