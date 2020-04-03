def gcd(a, b):
    if b % a != 0:
        return gcd(b % a, a % (b % a))
    return a


x = int(input())
y = int(input())

print(gcd(min(x, y), max(x, y)))
