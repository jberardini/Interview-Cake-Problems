def find_drone(arr):
	drones = set()
	counter = 0
	ideal_counter = 0

	for item in arr:
		if item not in drones:
			drones.add(item)
			ideal_counter += item * 2

		counter += item


	missing_drone = ideal_counter - counter
	return missing_drone


#with bit manipulation
def find_drone2(arr):

	unique_delivery_id = 0

	for item in arr:
		unique_delivery_id ^= item
		print unique_delivery_id

	return unique_delivery_id

print find_drone2([1, 2, 3, 3, 2, 1, 4, 4, 5, 6, 7, 6, 7])
