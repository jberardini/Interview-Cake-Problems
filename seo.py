class Trie(object):

	def __init__(self):
		self.root = {}

	def check_present_and_add(self, word):

		current_node = self.root

		is_new_word = False

		for char in word:
			if char not in current_node:
				is_new_word = True
				current_node[char] = {}
				print current_node
			current_node = current_node[char]
			print current_node

		if 'End of Word' not in current_node:
			is_new_word = True
			current_node['End of Word'] = {}

		print current_node

		return is_new_word


trie = Trie()

print trie.check_present_and_add('www.google.com')

"""Reflection

This was hard. I had no idea what to do. I've never used a trie before, and I still don't really have a grasp on 
it. But, I'm going to leave it for now with the hope that I'll get more practice in
a couple of problems"""
