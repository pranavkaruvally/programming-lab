def is_everydigit_even(n):
    while n > 0:
        digit = n%10
        if digit%2 != 0:
            return False
        n //= 10
    return True

def is_square(n):
    '''The logic of this function is that since every number
    can be expressed as the product of its prime factors and since
    (a*b)^2 is (a^2)*(b^2), for a perfect square every factor would
    be present in it even number of times'''
    i = 2
    factors = 0
    while n > 1:
        while n%i == 0:
            factors += 1
            n = n//i
        if factors%2 != 0:
            return False
        i += 1
    return True

def has_4_digits(n):
    digits = 0
    while n>0:
        digits += 1
        n //= 10
    return digits

def generate_nums(start, stop):
    if (not has_4_digits(start)) or (not has_4_digits(stop)):
        print("Not 4 digits")
        return

    for i in range(start+1 if start%2 else start, stop+1, 2):
        if is_everydigit_even(i) and is_square(i):
            print(i)

start = int(input("Start: "))
stop = int(input("Stop: "))
generate_nums(start, stop)


#A pythonista's way of writing the code is given below
'''
from functools import reduce

is_square = lambda x: x**0.5 == int(x**0.5)
is_everydigit_even = lambda x: reduce(lambda a, b: a*b, [x+1 for x in list(map(int, str(x)))]) % 2 == 1 #only product of odd numbers are odd. 1+even = odd
generate_digits = lambda a, b: [x for x in range(start, stop) if is_square(x) and is_everydigit_even(x)] 

start, stop = int(input("Start: ")), int(input("Stop: "))
print(generate_digits(start, stop))
'''
