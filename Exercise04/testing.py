def custom_len(input_list):
	"""custom_len(input_list) imitates len(input_list)"""
	for i in input_list:
		count = 0
		count = count + i
	print count
	return count

def custom_append(input_list,value):
	"""custom_append(input_list, value) imitates input_list.append(value)"""
	list_length = custom_len(input_list) + 1
	input_list[list_length:list_length] = [value]
	return input_list

	
list = [0,1,2,3,4,5,6,7,8,9]
print custom_append(list, 455)

