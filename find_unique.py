def find_unique(arr, n):

	expected_sum = sum(range(n+1))
	actual_sum = sum(arr)

	duplicate_num = actual_sum - expected_sum

	return duplicate_num