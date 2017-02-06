class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None

class LL(object):
	def __init__(self):
		self.head = None


	def delete_node(self, node):

		temp = node.next
		node.data = temp.data
		node.next = temp.next

	def print_nodes(self):
		current = self.head

		while current:
			print current.data
			current = current.next


my_ll = LL()


node_one = Node(4)
node_two = Node(3)
node_three = Node(2)
node_four = Node(1)


my_ll.head = node_one	
my_ll.head.next = node_two	
my_ll.head.next.next = node_three
my_ll.head.next.next.next = node_four




# my_ll.print_nodes()

my_ll.delete_node(node_two)
my_ll.print_nodes()