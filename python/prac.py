import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = input().rstrip()
a = sorted(n, reverse=True)
b = int(''.join(a))
print(b)