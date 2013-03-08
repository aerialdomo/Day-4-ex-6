
def replace_head(input_list):
	"""Remove the third and seventh elements of the input list."""
	input_list[2] = []
	input_list[7] = []
	print input_list
	
list = [0,1,2,3,4,5,6,7,8,9,10]
print replace_head(list)

