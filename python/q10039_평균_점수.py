import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

sum = 0
for _ in range(5):
    score = int(input())
    
    if score < 40:
        score = 40
        
    sum += score
    
print(int(sum//5))