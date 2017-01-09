class TempTracker(object):
	"""Creates a temptracker class"""

	def __init__(self):
		# self.temps = []
		self.min_temp = None
		self.max_temp = None
		self.total = 0
		self.length = 0

		self.occurences = [0] * 111
		self.max_occurences = 0
		self.mode = None

	def insert(self, new_temp):
		# self.temps.append(new_temp)
		self.max_temp = max(self.max_temp, new_temp)
		if self.min_temp is None or self.min_temp > new_temp:
			self.min_temp = new_temp
		self.total += new_temp
		self.length += 1

		self.occurences[new_temp] += 1
		if self.occurences[new_temp] > self.max_occurences:
			self.mode = new_temp
			self.max_occurences = self.occurences[new_temp]

	def get_max(self):
		# max_temp = self.temps[0]
		# for temp in self.temps:
		# 	max_temp = max(max_temp, temp)

		return self.max_temp

	def get_min(self):
		# min_temp = self.temps[0]

		# for temp in self.temps:
		# 	min_temp = min(min_temp, temp)

		return self.min_temp

	def get_mean(self):

		# total = 0
		# for temp in self.temps:
		# 	total += temp

		# mean = float(total) / len(self.temps)

		return float(self.total) / self.length


	def get_mode(self):
		# occurences = {}

		# for temp in self.temps:
		# 	occurences[temp] = occurences.get(temp, 0) + 1

		# max_occurence = 0
		# mode = None

		# for temp, occurence in occurences.iteritems():
		# 	if temp > max_occurence:
		# 		max_occurence = occurence
		# 		mode = temp

		return self.mode



current_temps = TempTracker()
current_temps.insert(95)
current_temps.insert(94)
current_temps.insert(95)

print current_temps.get_max()
print current_temps.get_min()
print current_temps.get_mean()
print current_temps.get_mode()

