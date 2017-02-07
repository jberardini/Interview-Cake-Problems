class Node(object):
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

class LL(object):
	def __init__(self, head=None):
		self.head = head



def contains_cycle(node):

	#find if there's a cycle
	#cycle: a node's next points back to a previous node
	#how will we know when there's a cycle?
	#maybe use another data structure to hold the nodes we've seen?
	# we'd need to look things up in this data structure, so maybe we'd use a set?
	# how do we know for sure that we've found the same node, and not just a node with the same data?
	# the set we create takes up O(n) space

	seen = set()
	while node:
		print node.data
		# if node in seen:
		# 	return True

		seen.add(node)
		node = node.next

	return False


def contains_cycle3(node):

	slow_runner = node
	fast_runner = node

	while fast_runner and fast_runner.next:
		slow_runner = slow_runner.next
		fast_runner = fast_runner.next.next
		print slow_runner.data
		print fast_runner.data

		if fast_runner is slow_runner:
			return True

	return False


node4 = Node(4)
node3 = Node(1, node4)
node2 = Node(2, node3)
node1 = Node(3, node2)
node4.next = node3

my_ll = LL(node1)

print contains_cycle3(node1)