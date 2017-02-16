n = input("Enter n: ")
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
	print "Armstrong"
else:
	print "Not Armstrong"
	
	