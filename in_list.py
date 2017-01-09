""" Initial thoughts. Basically, doing to treat this like a binary search tree"""
def in_list(lst, n):

	half_length = len(lst) / 2


	if lst[half_length] == n:
		return True

	if len(lst) == 1:
		return False


	if n > lst[half_length]: 
		in_list(lst[half_length:], n)

	else:
		in_list(lst[:half_length], n)


in_list([1,2,3], 5)
