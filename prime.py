x = input("Enter number: ")
count = 0

if x==1:
	print "Neither prime nor composite"
else:	
	for i in range(1, (x+1)):
		if x%i == 0:
			count+=1
	
	if count == 2:
		print 'Prime number'
	else:

		print 'Not a prime number'