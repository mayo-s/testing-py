def add(x, y):
	return x + y

def subtract(x, y):
	return x - y

def multiply(x, y):
	return x * y

def divide(x, y):
	if(y == 0): 
		return 'Division by 0 is undefined'
	return x / y

def square(x):
	return x**2

def exp_n(x, y):
	return x**y

def sqroot(x):
	if(x < 0): 
		return 'Number is undefined'
	return exp_n(x, 0.5)

def root_n(x, y):
	if(x < 0 and y%2 == 0): 
		return 'Number is undefined'
	exp = 1/float(y)
	if(x < 0 and y%2 == 1):
		x = -x
		return -exp_n(x, exp)

	return exp_n(x, exp)
