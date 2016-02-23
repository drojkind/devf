# Factorial 
# n!
# n! = n * (n-1)!
# 0! = 1

def factorial(n):
	if n > 0:
		return n * factorial(n-1)
	else:
		return 1
print(factorial(80))


