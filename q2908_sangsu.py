import sys

num1, num2 = map(int, sys.stdin.readline().split())
num1 = list(str(num1))
num2 = list(str(num2))

num1_rev = num1.reverse()
num2_rev = num2.reverse()

num1 = ''.join(num1)
num2 = ''.join(num2)

print(max(num1, num2))