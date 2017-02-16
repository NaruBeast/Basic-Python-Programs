n = input("Enter number of elements you want to enter: ")
print 'Enter elements you want to check...'
list = []
for i in range(n):
	list.append(input()) 
x = input("enter element to chek divisibility for: ")
for i in list:
	if i%x == 0:
		print i