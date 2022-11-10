n = int(input("Enter a number: "))

def num_digits(n):
	digits = 0
	while n > 0:
		n = n//10
		digits += 1
	return digits

def rep_n(n, times):
	result = 0
	digits = num_digits(n)
	for i in range(1, times+1):
		result = result*(10**digits) + n
	return result

def calc_sum(n):
	total = 0
	for i in range(1, 4):
		total += rep_n(n, i)
	return total

print("The sum is", calc_sum(n))
