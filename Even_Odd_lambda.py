#  Create a lmbda function that returns "Even" if a number is even , and "Odd" if a number is odd

n=int(input("Enter a number to check even or odd :"))
x=lambda a : "EVEN" if a%2 ==0  else "ODD"
print(x(n))

Output:
Enter a number to check even or odd :7
ODD
