#  Write a program to find the factorial of a given number using recursion.


def rfact(n):
	if n == 0:
		return 1
	else:
		return n*rfact(n-1)
a=int(input("Enter a number :"))
if a < 0:
	print("Factorail does not exists for negative numbers")
else:
	print("Factorial of ",a, " is :",rfact(a))

Output:
Enter a number : 5
Factorial of 5 is : 120
