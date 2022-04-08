def gcd(x, y):                      # x를 y로 나눠가려고 함.
    if y == 0:
        return x                    # 더 이상 나눌 y가 없으면 y를 나눠왔던 x를 반환.
    else:
        return gcd(y, x % y)        # x를 나눴으니 남은 나머지는 y보다 클 수 없다.
                                    # 따라서 다음부터는 x가 아닌 y를 나누어야 한다.
                                    # x를 y로 나누고 난 후 남은 나머지로 y를 나누려고 함.

x = 6
y = 3

print(gcd(x, y))