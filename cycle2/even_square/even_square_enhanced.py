def is_everydigit_even(n):
	while n>0:
		if (n%10)%2 != 0:
			return False
		n //= 10
	return True

def floored_sqrt(n):
	if n==0 or n==1:
		return n
	start, stop = 1, n//2
	while start < stop: 
		mid = (start + stop) // 2
		if mid*mid == n:
			return mid
		elif mid*mid < n:
			if start == mid:
				return mid
			start = mid
		else:
			if stop == mid:
				return mid
			stop = mid
	return mid

def even_square_generator(start, stop):
	start = floored_sqrt(start)
	i = start+1 if start%2 else start
	sq_i = i*i
	while sq_i < stop:
		if is_everydigit_even(sq_i):
			print(sq_i)
		i += 2
		sq_i = i*i

start = int(input("Start: "))
stop = int(input("Stop: "))
even_square_generator(start, stop)

