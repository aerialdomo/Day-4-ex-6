def custom_len(input_list):
	"""custom_len(input_list) imitates len(input_list)"""
	for i in input_list:
		count =0
		count += i
		return count

def custom_insert(input_list, index, value):
	"""custom_insert(input_list, index, value) imitates
	input_list.insert(index, value)
	"""
	list_length = custom_len(input_list)
	input_list[index:index] = [value]
	return input_list

# def custom_extend(input_list, values):
# 	"""custom_extend(input_list, values) imitates input_list.extend(values)"""
# 	return input_list + [value]
	
list = [0,1,2,3,4,5,6,7,8,9]
print custom_insert(list, 3, 455)

