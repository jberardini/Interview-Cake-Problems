def get_max_price(lst):

	"""

	>>> get_max_price([2, 3, 10, 5])
	8
	"""


	max_profit = lst[1] - lst[0]

	for i in range(len(lst)):
		for j in range(len(lst)):
			if j > i:
				print lst[j] - lst[i]
				max_profit = max(max_profit, lst[j] - lst[i])

	return max_profit

	"""Where is the unnecessary work?

	well, we're looping over a bunch of numbers that aren't even possibilities, 
	because, you can't sell for a price in the past

	Basically, you can only sell for prices in the future."""






if __name__ == "__main__":`
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
