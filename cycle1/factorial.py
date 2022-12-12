n = int(input("Enter a number: "))
prod = 1

if (n==0): n=1

for i in range(1, n+1):
    prod *= i

print(prod)
