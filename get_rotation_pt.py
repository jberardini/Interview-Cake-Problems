def get_rotation_pt(lst):
	"""Notes: 
	Goal: find the rotation point.
	What does this mean? Find the word that's first in the alphabet in the list
	But, finding something in a list is O(n). Sorting a list alphabetically is O(nlogn)
	Could we add to a dictionary based on first letter? 
	But, if there are multiple words that start with a, how would we get the first one

	Test case:
	xenophone
	yarmulke
	zenith
	apex
	buffoon

	>>> get_rotation_pt(['laconic', 'tacit', 'xenophone', 'yarmulke', 'zenith', 'apex', 'ascot', 'buffon', 'cocyx'])
	'apex'

	"""

	if len(lst) == 1:
		return lst[0]

	mid_point = len(lst) / 2
	

	if lst[mid_point][0] < lst[0][0]:
		return get_rotation_pt(lst[mid_point:])


	else:
		return get_rotation_pt(lst[:mid_point])


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print






