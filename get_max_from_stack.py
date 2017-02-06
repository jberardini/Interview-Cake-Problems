class Stack(object):
	def __init__(self):
		self.items = []
		self.maxs = []

	def is_empty(self):
		return not self.items

	def peek(self):
		if not self.items:
			return None

		return self.items[-1]

	def push(self, item):

		if not self.items or item > self.maxs[-1]:
			self.maxs.append(item)

		self.items.append(item)

	def pop(self):
		if not self.items:
			return None

		if self.items[-1] == self.maxs[-1]:
			self.maxs.pop()

		return self.items.pop()

class MaxStack(Stack):

	def get_max(self):
		return self.maxs[-1]

stack = MaxStack()

stack.push(1)
stack.push (10)
stack.push(4)

print stack.get_max()

stack.pop()
stack.pop()
print stack.get_max()