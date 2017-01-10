def get_time(flight_length, movie_lengths):


	"""
	My first attempt. Note, this doesn't work. I originally wrote the solution 
	without the second part of the if statement, but this gives a false positive if 
	there is one movie that is exactly half the flight length.

	>>> get_time(60, [30, 30, 15, 60])
	True

	>>> get_time(60, [30, 15, 60])
	False
	"""


	for movie_length in movie_lengths:
		possible_movie_length = flight_length - movie_length
		if possible_movie_length in movie_lengths and possible_movie_length is not movie_length:
			return True

	return False


def get_time2(flight_length, movie_lengths):

	"""

	My second solution. , but isn't the IC solution using a set. This is pretty messy
	looking though.

	>>> get_time2(60, [30, 30, 15, 60])
	True

	>>> get_time2(60, [30, 15, 60])
	False
	"""

	movie_catalogue = {}
	for movie_length in movie_lengths:
		movie_catalogue[movie_length] = movie_catalogue.get(movie_length, 0) + 1

	for movie_length in movie_lengths:

		if (flight_length - movie_length == movie_length and 
			movie_catalogue.get(flight_length - movie_length, 0)) > 1:
			return True


		elif (movie_catalogue.get(flight_length - movie_length, 0) ==1 and
			  flight_length - movie_length != movie_length):
			return True

		return False



def get_time3(flight_length, movie_lengths):
	"""This is the IC solution

	>>> get_time3(60, [30, 30, 15, 60])
	True

	>>> get_time3(60, [30, 15, 60])
	False
	"""

	movie_lengths_seen = set()

	for first_movie_length in movie_lengths:

		matching_second_movie_length = flight_length - first_movie_length
		if matching_second_movie_length in movie_lengths_seen:
			return True

		
		movie_lengths_seen.add(first_movie_length)


	return False

get_time3(60, [30, 30, 15, 60])




if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print

