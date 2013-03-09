def custom_len(input_list):
	"""custom_len(input_list) imitates len(input_list)"""
	count = 0
	for i in input_list:
		count += 1
	return count

def custom_pop(input_list):
	"""custom_pop(input_list) imitates input_list.pop()"""
	b = input_list[-1]
	return b


def custom_reverse(input_list):
	"""custom_reverse(input_list) imitates input_list.reverse()"""
	# new_list = []
	# for i in input_list:
	# 	# print 'b4 pop' + str(input_list)
	# 	pop_num = input_list.pop()
	# 	# print "input_list" + str(input_list)
	# 	new_list.append(pop_num)
	# 	print new_list	
	# return new_list
	# 	# print new_list

	thing = custom_len(input_list)
	for i in range(thing/2):
		hold = input_list[i]
		input_list[i] = input_list[-1]
		input_list[-1] = hold
	print input_list

	# return input_list[::-1]
	



# list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
list = [1, 2, 3, 4, 5, 6, 7]
more_list = [0, 1, 2, , 3, 5, 6]
# list = ['a','b','c','d','e','f','g']
# custom_reverse(list)
print custom_reverse(list)
# print custom_len([1, 2, 3])
print "PING"



