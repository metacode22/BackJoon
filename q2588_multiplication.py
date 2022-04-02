import sys

num1 = int(sys.stdin.readline())
num2 = list(map(int, sys.stdin.readline().rstrip()))
num3 = num2.reverse()

for i in num2:
    print(num1*i)

print(num1*num2[0] + num1*num2[1]*10 + num1*num2[2]*100)

