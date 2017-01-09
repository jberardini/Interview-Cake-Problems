"""Reflection: ok, so the main problem is that it's not clear what the underlying
principle is

If you're given 1, then with [1,2,3], there is 1 way to make change: 1

If you're given 2, then there are 2 ways to make change, (1,1) and (2)

If you're given 3, then there are 3 ways to make change, (1, 1, 1), (1, 2), (3)
If you're given 4, then there are 4 ways to make change (1,1,1,1), (1,1,2), (2,2), (3,1)


Given 5 and [1,2,3,4]:
(2,3)
(1,1,3)

Give 6 and [1,2,3,4]:

(4, 2)
(4, 1, 1)
(3, 3)
(3, 2, 1)
(3, 1, 1, 1)
(2, 2, 1, 1)
(1,1,1,1,2)
(1,1,1,1,1,1)


"""



"""Solution with memoization"""
class Change:
	def __init__(self):
		self.memo = {}

	def make_change(self, denom, amt, index=0):

		memo_key = str((amt, index))
		if memo_key in self.memo:
			return self.memo[memo_key]

		if amt == 0:
			return 1

		if amt < 0:
			return 0

		if index == len(denom):
			return 0


		current_coin = denom[index]

		ways = 0

		while amt >= 0:
			ways += self.make_change(amt, denom, index + 1)
			amount_left -= current_coin

		self.memo[memo_key] = ways

		return ways


def make_change(amt, denom):

	ways = [0] * (amt + 1)
	ways[0] = 1

	for coin in denom:
		for higher in xrange(coin, amt +1):
			higher_remainder = higher - coin
			ways[higher] += ways[higher_remainder]

	return ways[amt]


print make_change(4, [1,2,3])

def make_change2(amt, denom):
