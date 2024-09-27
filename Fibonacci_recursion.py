#  Write a program to print fibonacci sequence using recursion

def rfib(n):
	if n <=1:
		return n
	else:
		return (rfib(n-1) + rfib(n-2))
a=int(input("Enter a number :"))
if a <= 0:
	print("please enter a positive number.")
else:
	print("Fibnocci series is :")
	for i in range(a):
		print(rfib(i))

Output:
Enter a number :3
Fibnocci series is :
0
1
1
