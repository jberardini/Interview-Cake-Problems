stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

def get_max_price(prices):

	max_price = lst[0]
	min_price = lst[0]

	for i in range(len(lst)):
		if i == 0:
			continue

		max_price = max(max_price, lst[i])

		current_profit 