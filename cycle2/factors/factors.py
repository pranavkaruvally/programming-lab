def factors(n):
    return [x for x in range(1, n//2 + 1) if n%x == 0]

num = int(input("Num: "))
print("Factors are", factors(num))
