from random import randrange
def shuffle(arr):

	#get a random number
	#for the number at that index, switch with index 0
	# get a random number, switch that with 2

	if len(arr) <= 1:
		return arr

	for i in range(len(arr)-1):
		switch_index = randrange(i, len(arr)-1)

		if switch_index != i:
			arr[i], arr[switch_index] = arr[switch_index], arr[i]

	return arr


print shuffle([1, 2, 3, 4])

