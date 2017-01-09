def is_valid(node):

	if not node:
		return True

	if node.left.data > node.data or node.right.data < node.data:
		return False

	is_valid(node.left)
	is_valid(node.right)


class Node(object):

	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

root = Node(5)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)

print is_valid(root)