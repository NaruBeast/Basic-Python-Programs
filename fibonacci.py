a, b = 0, 1
n = input("Enter number of terms: ")

if n==1:
	print a
else:	
	for i in range(n):
		print a
		a, b = b, b+a 