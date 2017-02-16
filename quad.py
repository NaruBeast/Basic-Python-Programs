print "For a quadratic equation ax^2 + bx + c"
a = input("Enter a: ")
b = input("Enter b: ")
c = input("Enter c: ")

d = b**2 - 4*a*c
if d>=0:
	x1 = float(-b + d**0.5)/2*a
	x2 = float(-b - d**0.5)/2*a
	print 'x1 =', x1, 'x2 =', x2 #x1 and 'x2 ='
else:
	print 'No real roots'