def fastPower(a, n):
    if n > 1:
        if n % 2 == 0:
            return fastPower(a * a, n / 2)
        else:
            return a * fastPower(a, n - 1)
    return a


x = float(input())
y = float(input())
if y == 0:
    print(1)
else:
    print((fastPower(x, y)))
