x = input("Enter range: ")


for n in range(1,x+1):
	copy = n
	count = 0
	while copy != 0:
		count +=1 
		copy/=10

	copy = n
	d=0
	while copy!=0:
		d += ((copy%10)**count)
		copy/=10

	if d==n:
		print n
	
	
