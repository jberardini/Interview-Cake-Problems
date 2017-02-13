def is_palindrome(word):
	#the counts of the letters all have to be even, except for one
	#create a dictionary, storing letter and count
	#make a flag, when you see an odd count, change to true
	#if you see an odd count and the flag is already true, return False

	char_count = {}
	one_odd = False
	for char in word:
		char_count[char] = char_count.get(char, 0) + 1

	for item in char_count:
		if char_count[item] % 2:

		 	if one_odd == False:
				one_odd = True
			else:
				return False

	return True




def is_palindrome2(word):

	uneven_chars = set()

	for char in word:
		if char not in uneven_chars:
			uneven_chars.add(char)
		else:
			uneven_chars.remove(char)

	if len(uneven_chars) > 1:
		return False

	return True

print is_palindrome2('civic')
print is_palindrome2('ivicc')
print is_palindrome2('civil')