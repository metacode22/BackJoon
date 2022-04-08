import sys, math

n = int(sys.stdin.readline())

num_list = list(range(1, n + 1))
prime_list = []

def is_prime_num(n):
    if n == 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

for i in num_list:
    if i == 1:
        continue

    if is_prime_num(i) == True:
        prime_list.append(i)

print(prime_list)