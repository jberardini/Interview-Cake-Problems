def validate_closers(phrase):
	#add every parenthesis to a stack
	#keep adding as long as you find an open paren
	#when you hit a closed paren, if it doesn't match the last item
	#in the stack, return False
	#if it does match, pop the last thing off the stack
	#if stack is not empty at the end of iterating through the string, 
	#return False
	#if the stack is empty, return True

	separators = []

	closers_to_openers = {')':'(', ']': '[', '}': '{'}

	openers = set(closers_to_openers.values())

	for char in phrase:
		if char in openers:
			separators.append(char)

		elif char in closers_to_openers:
			if not separators:
				return False

			if separators[-1] == closers_to_openers[char]:
				separators.pop()
			
			else:
				return False

	return not separators

print validate_closers('{ [ ] ( ) }')
print validate_closers('{ [ ( ] ) }')
print validate_closers('{[}')

print validate_closers('}[{}]')