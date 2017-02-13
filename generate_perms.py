def generate_perms(word):
	if len(word) < 2:
		return set([word])

	all_chars_except_last = word[:-1]
	last_char = word[-1]

	permutations_of_all_chars_except_last = generate_perms(all_chars_except_last)

	permutations = set()

	for permutations_of_all_chars_except_last in permutations_of_all_chars_except_last:
		for position in range(len(all_chars_except_last) + 1):
			