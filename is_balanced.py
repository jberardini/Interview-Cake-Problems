# def is_balanced(BinaryTreeNode):
# 	""" Node
# 	     /\
# 	   Node
# 	   /\
# 	 Node Node"""

# 	 depths = []

# 	 nodes = []

# 	 nodes.append((tree_root, 0))

# 	 while len(nodes):

# 	 	node, depth = nodes.pop()

# 	 	if (not node.left) and (not node.right):

# 	 		if depth not in depths:
# 	 			depths.append(depth)


# 	 			if (len(depths) > 2) or \
# 	 				(len(depths) == 2 and abs(depths[0] - depths[1]) > 1):

# 	 				return False
		
# 		else:
# 			if node.left:
# 				nodes.append((node.left, depth + 1))

# 			if node.right:
# 				nodes.append((node.right, depth + 1))

# 	return True

def is_balanced2(Node):

	if not Node:
		return 0;

	left_height = is_balanced2(Node.left)
	if left_height == -1:
		return -1

	right_height = is_balanced2(Node.right)
	if right_height == -1:
		return -1

	diff = left_height - right_height

	if abs(diff) > 1:
		return -1;

	return 1 + max(left_height, right_height)

class Node(object):

	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

root = Node(5)
root.left = Node(10)
root.right = Node(15)
root.left.left = Node(20)
root.left.right = Node(25)
root.right.left = Node(30)
root.right.right = Node(35)

print is_balanced2(root)





