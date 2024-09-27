#  Write a program to find the GCD of two numbers using recusion.

def gcd(a,b):
	if b == 0:
		return a
	else:
		return gcd(b,a%b)
print(" GCD of given two numbers  is : ",gcd(48,18))


Output:
GCD of given two numbers  is : 6
