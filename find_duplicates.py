def find_duplicates(arr):
	#naive way: two for loops
	#better way: dictionary, but that doesn't save space (actually, a set)
	#can't use bitwise or summing, because you'll end up with a sum, and won't be able to tell 
	#which integers it's made up of

	floor = 1
	ceiling = len(arr) - 1

	while floor > ceiling:

		midpoint = floor + ((ceiling - floor) /2)
		lower_range_floor, lower_range_ceiling = floor, midpoint
		upper_range_floor, upper_range_ceiling = midpoint+1, ceiling

		items_in_lower_range = 0
		for item in the_list:
			if item >= lower_range_floor and item <= lower_range_ceiling:
				items_in_lower_range += 1

		distinct_possible_integers_in_lower_range = lower_range_ceiling - lower_range_floor + 1

		if items_in_lower_range > distinct_possible_integers_in_lower_range:
			floor, ceiling = lower_range_floor, lower_range_ceiling

		else:
			floor, ceiling = upper_range_floor, upper_range_ceiling


		return floor