def max_duffel_haul(lst, duffel_weight):
	"""Test case

	>>> max_duffel_haul([(7, 160), (3, 90)], 10)
	270

	>>> max_duffel_haul([(7, 160), (6, 100)], 2)
	0

	>>> max_duffel_haul([(7, 160), (6, 100)], 2)
	0

	IC insight:
	We need to factor in the weight AND the value

"""
	# max_val = 0
	# for weight, value in lst:
	# 	value_per_kilo = value / weight
	# 	if value > max_val:
	# 		max_val = value
	# 		highest_value_cake = (weight, value)

	# duffel_weight_d = duffel_weight

	# while duffel_weight_d > 0:
	# 	duffel_weight_d -= highest_value_cake[0]


def max_duffel_bag_value_with_capacity_1(cake_tuples):

	max_val = 0

	for cake_weight, cake_value in cake_tuples:
		if (cake_weight == 1):
			max_val = max(max_val, cake_value)






