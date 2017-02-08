
def reverse_string(word):

	chars_lst = [char for char in word]

	length = len(chars_lst)

	for i in range(length/2):

		chars_lst[i], chars_lst[length - i - 1] = chars_lst[length - i - 1], chars_lst[i]

	word = ''.join(chars_lst)

	return word

print reverse_string('Jill')