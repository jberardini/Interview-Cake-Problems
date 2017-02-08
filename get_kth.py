class Node(object):
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

class LL(object):
	def __init__(self, head=None):
		self.head = head

	def get_kth(self, k):

		first_pointer = self.head
		counter = 0
		second_pointer = self.head

		while first_pointer:

			if counter >= k:
				second_pointer = second_pointer.next
			counter += 1
			first_pointer = first_pointer.next

		return second_pointer.data



node4 = Node(4)
node3 = Node(1, node4)
node2 = Node(2, node3)
node1 = Node(3, node2)

my_ll = LL(node1)
print my_ll.get_kth(3)