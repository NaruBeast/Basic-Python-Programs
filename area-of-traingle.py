s1 = input("Enter side 1: ")
s2 = input("Enter side 2: ")
s3 = input("Enter side 3: ")
s = float(s1 + s2 + s3)/2 #s is the semiperimeter

#This checks whether the traingle exists
def isValid(s1,s2,s3):
	if s1>s2:
		if s1>s3:
			largest = s1
		else:
			largest = s3
	else:
		if s2>s3:
			largest = s2
		else:
			largest = s3
	isvalid = largest < (s1+s2+s3)-largest
	return isvalid	


if (isValid(s1,s2,s3)): #Function is called
	area = (s*(s-s1)*(s-s2)*(s-s3))**0.5 #Taking square root
	print 'Area =', area
else:
	print 'Traingle does not exist'
	