def is_letter(character):

	return character in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'	


def gen_cloud(phrase):

	word_dict = {}
	counter = 0
	current_word = ''

	while counter < len(phrase):
		if not is_letter(phrase[counter]):
			if current_word:
				if current_word.capitalize() in word_dict:
					word_dict[current_word.capitalize()] += 1

				elif current_word.lower() in word_dict:
					word_dict[current_word.lower()] += 1

				else:
					word_dict[current_word] = 1

				current_word = ''

		else:
			current_word += phrase[counter]

		counter += 1

	if current_word:
		if current_word.upper() in word_dict:
			word_dict[current_word.upper()] += 1

		elif current_word.lower() in word_dict:
			word_dict[current_word.lower()] += 1

		else:
			word_dict[current_word] = 1


	return word_dict


print gen_cloud('Add milk and eggs, then add flour and sugar')
print gen_cloud('After beating the eggs, Dana read the next step:')