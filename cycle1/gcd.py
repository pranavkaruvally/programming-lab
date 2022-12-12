def gcd(a, b):
    g = a if a>b else b
    l = a+b - g

    r = g%l

    while (r != 0):
        g, l = l, r
        r = g%l

    return l

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

print("GCD is", gcd(a, b))
