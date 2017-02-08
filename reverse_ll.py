class Node(object):
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

class LL(object):
	def __init__(self, head=None):
		self.head = head


	def reverse_ll(self):

		prev = None
		current = self.head

		while current:
			next = current.next
			current.next = prev
			prev = current
			current = next


		self.head = prev


	def print_nodes(self):

		current = self.head

		while current:
			print current.data
			current = current.next


node4 = Node(4)
node3 = Node(1, node4)
node2 = Node(2, node3)
node1 = Node(3, node2)


my_ll = LL(node1)

my_ll.print_nodes()
my_ll.reverse_ll()
my_ll.print_nodes()
