import sys

input = sys.stdin.readline
n = int(input())

def factorial(x):
    global n

    if n == 0:
        return 1

    if x == 1:
        return 1

    else:
        return x * factorial(x - 1)

print(factorial(n))