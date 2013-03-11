f = open("test_file.txt")
firstletter = f.read()
# reads the whole txt file
f.close()
count_list = [0] * 26
# making 26 spots in count_list

lower_letters = firstletter.lower()
# assign result of .lower to lower_letters
# what does .lower do? converts chr in string to lowercase

# what does this for loop do? loop through each chr in list lower_lettters
for  letter in lower_letters:
	if ord(letter) in range(ord('a'), ord('z') + 1): 
	# since ord('a') = 97, can use range function
		count_list[ord(letter) - ord('a')] += 1
		# using ord to find postion in list w/o lots of code or dictionary

print count_list