import sys

prime_list = [True for _ in range(10001)]

for i in range(2, 101):
    if prime_list[i] == True:
        for j in range(i*i, 10001, i):
            prime_list[j] = False

t = int(sys.stdin.readline())

for k in range(t):
    n = int(sys.stdin.readline())

    a = n // 2
    b = a
    for j in range(5000):
        if prime_list[a] and prime_list[b]:
            print(a, b)
            break
        a -= 1
        b += 1


                    


