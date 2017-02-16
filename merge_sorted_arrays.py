def merge_sorted_arrays(arr1, arr2):

	i = 0
	j = 0

	merged_array = []

	while i < len(arr1) and j < len(arr2):
		if arr1[i] < arr2[j]:
			merged_array.append(arr1[i])
			i +=1

		else:
			merged_array.append(arr2[j])
			j += 1

	merged_array.extend(arr1[i:])
	merged_array.extend(arr2[j:])

	return merged_array


print merge_sorted_arrays([1, 4, 7], [2, 3, 8])