def add_nums(args):
    return ' '.join(args)

def generate_multiples(n):
    return [str(n*x) for x in range(1, n+1)]

def generate_triangle(n):
    for i in range(1, n+1):
        print(add_nums(generate_multiples(i)))

steps = int(input("N: "))
generate_triangle(steps)
