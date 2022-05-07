import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
idx = 2

# def is_prime_number(x):
#     for i in range(2, x):
#         if x % i == 0:
#             return False
            
#     return True

# while n != 1:
#     if n % idx == 0:
#         print(idx)
#         n = n // idx
#     else:
#         idx += 1
#         while not is_prime_number(idx):
#             idx += 1

while n != 1:
    if n % idx == 0:
        print(idx)
        n = n // idx
    else:
        idx += 1