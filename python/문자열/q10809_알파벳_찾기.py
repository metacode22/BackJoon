import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

s = input().rstrip()
alphabets = 'abcdefghijklmnopqrstuvwxyz'
data = dict()

for alphabet in alphabets:
    data[alphabet] = -1
    
for idx, x in enumerate(s):
    if data[x] == -1:
        data[x] = idx
    
for j in data.values():
    print(j, end = ' ')

    