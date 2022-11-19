def fib(n):
    a, b = 0, 1
    for i in range(n):
        print(b, end=' ')
        a, b = b, a+b

terms = int(input("No. of terms: "))
fib(terms)
print()
