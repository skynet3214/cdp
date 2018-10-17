class List_Node(object):
	def __init__(self, data):
		self.data = data
		self.right = None
		self.left = None

class Linked_List(object):
	def __init__(self):
		self.head = None
		self.no_of_nodes = 1