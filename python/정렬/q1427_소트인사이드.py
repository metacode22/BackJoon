import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = input().rstrip()

a = ''.join(sorted(n, reverse=True))
print(int(a))