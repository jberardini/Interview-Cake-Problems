def find_largest(node):

	if not node:
		raise Exception('Tree must have at least 1 node')

	if not node.right:
		return node.data

	return find_largest(node.right)


def find_second(node):
	"""Find second largest item
	Going to have to keep track of the largest and the second largest item
	Maybe not: BSTs have specific shapes

	Test case 1:

	    5
	   2  7
	  1 3 6 8
	       10
	      9  11

	  6
	1   7

	  6
	1
	"""

	if not node or (not node.left and not node.right):
		raise Exception('Tree must have at least two nodes')	

	if node.right and not node.right.right and not node.right.left:
		return node.data

	if not node.right and node.left:
		return find_largest(node.left)

	return find_second(node.right)


class Node(object):
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


root = Node(5)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(8)
root.right.right.left = Node(7)
root.right.right.left.left = Node(4)
root.right.right.left.right = Node(11)

print find_second(root)


"""Reflection
Remember to use helper functions!

The second largest item in a binary tree is the parent of the rightmost item, unless
the parent has a left subtree, in which case the second largest item is the largest
item in the left subtree.

You can recursively walk through the left or right most branches by calling the recursive
function on node.left or node.right."""