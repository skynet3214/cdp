from queue import Queue
#The aim is to create other types of trees and use python class concepts to inherit and blah blah
HEIGHT = 0
class BinaryTree(object):
	def __init__(self):
		self.root = None
		self.no_of_nodes = 0 

	def add_node_to_tree(self, data):       #if given a list, how to add all the elements in the list
		if self.root == None:
			self.root = TreeNode(data)
			self.no_of_nodes += 1
			#print "root: ",self.root.data
		else:
			q = Queue()
			node = self.root
			q.enqueue([node])
			while not q.IsQueueEmpty():
				node = q.dequeue()
				if node.left is None:
					node.left = TreeNode(data)
					self.no_of_nodes += 1
					#print node.left.data
					q.clear()
				elif node.right is None:
					node.right = TreeNode(data)
					self.no_of_nodes += 1
					#print node.right.data
					q.clear()
				else:
					q.enqueue([node.left, node.right])
	
	
	def print_level_order(self):
		if self.root == None:
			print " The tree is empty"
			return 
		else:
			node = self.root
			q1, q2 = Queue(), Queue()
			current_q, other_q = q1, q2
			current_q.enqueue([node])
			while not current_q.IsQueueEmpty() or not other_q.IsQueueEmpty():
				while not current_q.IsQueueEmpty():
					node = current_q.dequeue()
					print node.data,
					if node.left != None:
						other_q.enqueue([node.left])
					if node.right != None:
						other_q.enqueue([node.right])
				print "\n"
				other_q, current_q = current_q, other_q
	
	def height_of_tree(self, node, height):
		if self.root == None:
			return 0
		else:
			global HEIGHT
			if node == None:
				if height > HEIGHT:
					HEIGHT = height
				return
			else:
				height+=1
				self.height_of_tree(node.left, height)
				self.height_of_tree(node.right, height)

	def hasPathSum(self, node, sum):
		if self.root == None:
			print "Tree is Empty"
			return False
		else:
			if node == None:
				return True if sum == 0 else False
			else:
				hasSum = self.hasPathSum(node.left, sum-node.data) or self.hasPathSum(node.right, sum-node.data)
				return hasSum

	def printPaths(self):
		if self.root == None:
			print "The tree is empty"
			return 
		else:
			self._printPaths(self.root, [])
	def _printPaths(self, node, currentPath):
		if node == None:
			return
		if node.left == None and node.right == None:
			currentPath.append(node.data)
			print currentPath
			return
		else:
			currentPath.append(node.data)
			self._printPaths(node.left, currentPath)
			currentPath.pop()
			self._printPaths(node.right, currentPath)
			currentPath.pop()

	def hasPathSum2(self, node, sum):
		if self.root == None:
			print "Tree is empty"
			return True if sum == None else False
		else:
			_hasPathSum2(self.root, sum)
	def _hasPathSum2(node, sum):
		if node == None:
			return True if sum == 0 else False
		else:
			left_result = self.hasPathSum2(node.left, sum-node.data) 
			right_result = self.hasPathSum2(node.right, sum-node.data) 
			return left_result or right_result


def sameTree(node_a, node_b):
	if node_a == None and node_b == None:
		return True
	elif (node_a == None and node_b != None) or (node_a != None and node_b == None):
		return False
	elif node_a.data == node_b.data:
		return (sameTree(node_a.left, node_b.left) and sameTree(node_a.right, node_b.right))
	else: 
		return False

class TreeNode(object):
	def __init__(self, data):
		self.data = data
		self.right = None
		self.left = None
	
	def __str__(self):
		 return "Current node:{} right node:{} left node:{}".format([self.data, self.right,self.left])


if __name__ == "__main__":
	a = BinaryTree()
	#BinaryTree.add_node_to_tree(a, 10)
	a.add_node_to_tree(10)
	a.add_node_to_tree(20)
	a.add_node_to_tree(30)
	a.add_node_to_tree(40)
	a.add_node_to_tree(50)
	a.add_node_to_tree(60)
	a.add_node_to_tree(70)
	a.add_node_to_tree(80)
	a.add_node_to_tree(90)
	a.add_node_to_tree(100)
	a.add_node_to_tree(110)
	a.add_node_to_tree(120)
	a.add_node_to_tree(130)
	a.add_node_to_tree(140)
	a.add_node_to_tree(150)
	a.add_node_to_tree(160)
	a.add_node_to_tree(170)
	a.add_node_to_tree(180)
	a.add_node_to_tree(190)
	a.print_level_order()
	a.printPaths()
	print a.hasPathSum(a.root,0)

	'''
	b = BinaryTree()
	b.add_node_to_tree(10)
	b.add_node_to_tree(20)
	b.add_node_to_tree(30)
	b.add_node_to_tree(10)
	b.add_node_to_tree(20)
	b.add_node_to_tree(10)
	b.add_node_to_tree(10)

	a.add_node_to_tree(30)
	a.add_node_to_tree(10)
	a.add_node_to_tree(20)
	a.add_node_to_tree(30)
	a.add_node_to_tree(10)
	a.add_node_to_tree(20)
	a.add_node_to_tree(10)
	a.add_node_to_tree(20)
	a.add_node_to_tree(30)
	a.add_node_to_tree(10)
	a.add_node_to_tree(20)
	a.add_node_to_tree(10)
	a.add_node_to_tree(20)
	a.add_node_to_tree(30)
	a.add_node_to_tree(10)
	a.add_node_to_tree(20)
	a.add_node_to_tree(30)
	a.add_node_to_tree(10)
	a.add_node_to_tree(20)
	a.add_node_to_tree(30)
	a.add_node_to_tree(10)
	a.add_node_to_tree(20)
	a.add_node_to_tree(10)
	a.add_node_to_tree(20)
	a.add_node_to_tree(30)
	a.add_node_to_tree(10)
	a.add_node_to_tree(20)
	
	a.print_level_order()
	b.print_level_order()
	a.height_of_tree(a.root,0)
	hasSum = a.hasPathSum(a.root,50)
	print sameTree(a.root,b.root)
	'''

	#print hasSum
	#print HEIGHT



