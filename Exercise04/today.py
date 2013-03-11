numbers = [0]

# def today(i,b):
# 	#i = 0
# 	incrementor = 1
# 	while i < b:
# 		print "At the top i is %d" % i

# 		i = i + incrementor
# 		print "Numbers now: ", numbers
	# 	print "At the bottom i is %d" % i
	# 	numbers.append(i)
	# 	#print numbers
	# return numbers

def otherToday(x,y):
	for i in range(x,y):
		print "At the top i is %d" % i

		i = i + 1
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
		numbers.append(i)
		#print numbers
	return numbers	

otherToday(0,6)

print "PING"
print "The numbers: "

for num in numbers:
	print num