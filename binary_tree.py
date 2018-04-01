from queue import Queue
#The aim is to create other types of trees and use python class concepts to inherit and blah blah
HEIGHT = 0

class TreeNode(object):
	def __init__(self, data):
		self.data = data
		self.right = None
		self.left = None
	
	def __str__(self):
		 return "node:{} ".format(self.data)

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

	def isBST(self):
		if self.root == None:
			return True
		else:
			return self._isBST(self.root)

	def _isBST(self, node):
		if node is not None:
			if self.__isBST(node.left, node.data, 0) and self.__isBST(node.right, node.data, 1):
				return self._isBST(node.left) and self._isBST(node.right)
			else:
				return False
		return True

	def __isBST(self, node, data):
		if node is None:
			return True
		else:
			if node.data > data and mode == 0:
				return False 
			elif node.data < data and mode == 1:
				return False
			else:
				return self.__isBST(node.left, data, mode) and self.__isBST(node.right, data, mode)


def sameTree(node_a, node_b):
	if node_a == None and node_b == None:
		return True
	elif (node_a == None and node_b != None) or (node_a != None and node_b == None):
		return False
	elif node_a.data == node_b.data:
		return (sameTree(node_a.left, node_b.left) and sameTree(node_a.right, node_b.right))
	else: 
		return False

def mergeTree(node_a, node_b):
	c.root = _mergeTree(node_a, node_b)
	return c.root

	
def _mergeTree(node_a, node_b):
	if node_a == None and node_b == None:
		return 
	else:
		if node_a != None and node_b != None:
			node_c =  TreeNode(node_a.data + node_b.data)
			node_c.left = _mergeTree(node_a.left, node_b.left)
			node_c.right = _mergeTree(node_a.right, node_b.right)
			return node_c
		elif node_a == None and node_b != None:
			#node_c =  TreeNode(node_b.data)
			#node_c.left = _mergeTree(None, node_b.left)
			#node_c.right = _mergeTree(None, node_b.right)
			return TreeNode(node_b.data)
		elif node_a != None and node_b == None:
			#node_c =  TreeNode(node_a.data)
			#node_c.left = _mergeTree(node_a.left, None)
			#node_c.right = _mergeTree(node_a.right, None)
			return TreeNode(node_a.data)


#Assume both the roots are not none

	

	


def mergeTreeNode(node_a, node_b):
	if node_a == None and node_b == None:
		return None
	elif node_a != None and node_b != None:
		return TreeNode(node_a.data + node_b.data)
		#node is still unconnected
	elif node_a == None and node_b != None:
		return TreeNode(node_b.data)
	elif node_a != None and node_b == None:
		return TreeNode(node_a.data)
'''
def mergeTrees(t1, t2):
	if t1 and t2:
	    root = TreeNode(t1.data + t2.data)
	    root.left = mergeTrees(t1.left, t2.left)
	    root.right = mergeTrees(t1.right, t2.right)
	    return root
	else:
	    return t1 or t2
'''
		        



if __name__ == "__main__":
	a = BinaryTree()
	#BinaryTree.add_node_to_tree(a, 10)
	
	a.add_node_to_tree(20)
	a.add_node_to_tree(10)
	a.add_node_to_tree(30)
	
	print "a  :{}".format('--'*20)
	a.print_level_order()
	
	'''
	a.add_node_to_tree(30)
	a.add_node_to_tree(4)
	a.add_node_to_tree(50)
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
	'''
	

	#print a.isBST()
	#a.printPaths()

	#print a
	
	#print a.hasPathSum(a.root,0)
	
	b = BinaryTree()
	b.add_node_to_tree(10)
	b.add_node_to_tree(20)
	b.add_node_to_tree(30)
	
	b.add_node_to_tree(10)
	print "b  :{}".format('--'*20)
	b.print_level_order()
	c = BinaryTree()
	c.root = mergeTree(a.root, b.root)
	print "c :{}".format('--'*20)
	print "c_root_id :{}".format(id(c.root))
	c.print_level_order()
	
	'''
	b.add_node_to_tree(30)
	b.add_node_to_tree(10)
	b.add_node_to_tree(20)
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



