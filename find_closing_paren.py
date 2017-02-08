def find_closing_paren(str, k):

	open_paren_count = 0

	for i in range(k, len(str)):
		if str[i] == '(':
			open_paren_count += 1

		if str[i] == ')':
			open_paren_count -= 1

		if open_paren_count == 0:
			return i

print find_closing_paren("Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing.", 10)