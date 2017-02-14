from random import randrange

def get_seven(start, end):
	result = randrange(start, end)
	return result

def get_five(start, end):
	#need to use a random function that returns one of seven nos. to return one of five
	#what if 1-5 all correspond to 1-5 on 7-side die
	#BUT 6-7 have a one in five chance of being 1-5
	#how can we randomly determine what to assign 6 and 7 to?
	#what if we just keep generating until we get a 1-5? That's random

	interim_result = get_seven(start, end)
	print interim_result

	while interim_result > 5:
		interim_result = get_seven(start, end)

	return interim_result

print get_five(1, 7)


