# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def isValidBST(self,root):
		def _isBST(node):
			if node is not None:
				if __isBST(node.left, node.val, 0) and __isBST(node.right, node.val, 1):
					return _isBST(node.left) and _isBST(node.right)
				else:
					return False
			return True
		def __isBST(node, val, mode):
			if node is None:
				return True
			else:
				if node.val >= val and mode == 0:
					return False 
				elif node.val <= val and mode == 1:
					return False
				else:
					return __isBST(node.left, val, mode) and __isBST(node.right, val, mode)
		return _isBST(root)


class Solution(object):
	def isValidBST(self,root):
		def _isBST(node):
			if node is None:
				return True
			else:
				if node.left is not None:
					_isBST(node.left)
					left = __isBST(node, val, 0)
				if node.right is not None:
					_isBST(node.right)
					left = __isBST(node, val, 1)
				
			
		def __isBST(node, val, mode):
			if node is None:
				return True
			else:
				if node.val >= val and mode == 0:
					return False 
				elif node.val <= val and mode == 1:
					return False
				else:
					return __isBST(node.left, val, mode) and __isBST(node.right, val, mode)
		return _isBST(root)

		
		
		
		

			
		
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		