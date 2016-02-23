# 0, 1, 1
# Fib(n) = Fib(n-1) + Fib(n-2)
# Fib(3) = Fib(2) + Fib(1) = 1 + 0 = 1
# Fib(4) = Fib(3)

def fib(n):
	if n > 2:
		return fib(n-1) + fib(n-2)
	else:
		return n - 1
print(fib(39))