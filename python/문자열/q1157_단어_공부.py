import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

strings = input().rstrip().lower()
alphabets = 'abcdefghijklmnopqrstuvwxyz'
data = dict()
max_key = ''
max_value = -sys.maxsize
res = list()
cnt = 0

for alphabet in alphabets:
    data[alphabet] = 0
    
for string in strings:
    data[string] += 1
    
    if data[string] > max_value:
        max_value = data[string]
        max_key = string
    
for x in data.values():
    if x == max_value:
        cnt += 1

if cnt > 1:
    print('?')
else:
    print(max_key.upper())
