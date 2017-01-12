"""Reflection: 
The recursive solution technically takes O(2^n) time because we're making two recursive calls each time.

The iterative solution only takes 0(n) time

Can memoize here"""

def get_fib(n):
	"""Test cases

	>>> get_fib(4)
	3"""


	if n <= 2:
		return 1

	return get_fib(n-1) + get_fib(n-2)

def get_fib2(n):
	"""Test cases

	>>> get_fib2(4)
	3"""

	first_num = 1
	second_num = 1

	for i in range(3, n):
		first_num, second_num = second_num, first_num + second_num

	return first_num + second_num

class Fib(object):
	def __init__(self):
		self.memo = {}

	def get_fib(self, n):

		if n <= 2:
			return 1

		if n in self.memo:
			return self.memo[n]

		result = self.get_fib(n-1) + self.get_fib(n-2)

		self.memo[n] = result

		return result





if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
