import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

a, b = map(int, input().split())
print(a + b)