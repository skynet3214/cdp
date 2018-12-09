from pprint import pprint 
from pprint import pformat

class ListNode(object): 
	def __init__(self, data):
		self.data = data
		self.next = None
	def __str__(self):
		return "val:{}".format(self.data)
	#def __repr__(self):
	#	return self.data

class SingleLinkedList(object):
	def __init__(self):
		self.head = None
		self.no_of_nodes = 0
	
	def add_node_to_list(self, data):
		if self.head == None:
			self.head = ListNode(data)
			self.no_of_nodes+=1
		else:
			self._add_node_to_list(data, self.head)
	
	def _add_node_to_list(self, data, node):
		while node.next != None:
			node = node.next
		else:
			node.next =  ListNode(data)
			self.no_of_nodes+=1

	def remove_node_from_list(self, data):
		if self.head == None:
			print "List is empty, node does't exist"
		else:
			self._remove_node_from_list(data)
	def _remove_node_from_list(self, data):
		initial_no_of_nodes = self.no_of_nodes
		previous_node = None
		current_node = self.head
		
		while self.head.data == data:
			current_node = self.head.next
			del self.head
			self.no_of_nodes-=1
			self.head = current_node 
			if current_node is None:break
		
		
		while current_node is not None:
			if current_node.data == data:
				previous_node.next = current_node.next
				del current_node
				self.no_of_nodes-=1
				current_node = previous_node.next				
			else:
				previous_node = current_node
				current_node = current_node.next
		
		deleted_nodes = initial_no_of_nodes - self.no_of_nodes
		if not deleted_nodes:
			print "Data not found in list"
		else:
			print "Deleted {} nodes containing {}".format(deleted_nodes, data)


			



	def __str__(self):
		if self.head == None:
			return "This linked list is empty"
		else:
			node = self.head
			list_elements = []
			while node is not None:
				list_elements.append(node.data)
				node = node.next
			return "No of elements:{}, list_elements: {}".format(self.no_of_nodes,list_elements) 


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        def get_no_nodes(head_node):
            no_of_nodes = 0
            while head_node is not None:
                no_of_nodes+=1
                head_node = head_node.next
            return no_of_nodes
        a_nodes = get_no_nodes(headA)
        b_nodes = get_no_nodes(headB)
        #print a_nodes, b_nodes
        short_list, long_list, steps =  (headA, headB, b_nodes-a_nodes) if a_nodes<b_nodes else (headB, headA, a_nodes-b_nodes)
        for every_step in range(steps):
            long_list = long_list.next
        
        while short_list is not None and long_list is not None:
            if short_list is long_list:
                return short_list
            else:
                short_list = short_list.next
                long_list = long_list.next
        return None
                
                
            
            
            
                
                
                
            
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
def mergelists(lists):
	listheads = []
	merged_list = SingleLinkedList()
	for l in lists:
		listheads.append(l.head)
	l1, l2, l3 = listheads[0], listheads[1], listheads[2]



	def _mergetwolists(l1, l2):
	(node_to_add, l1, l2) = (l1, l1.next, l2) if l1.data <= l2.data else (l2, l1, l2.next)
	merged_list.head, current_node = node_to_add, node_to_add

	while l1 is not None and l2 is not None:

		(node_to_add, l1, l2) = (l1, l1.next, l2) if l1.data <= l2.data else (l2, l1, l2.next)
		current_node.next, current_node = node_to_add, node_to_add
		#current_node.next = node_to_add
		#current_node = node_to_add
	current_node.next = l1 if l1 is not None  else l2

	return merged_list


class Solution(object):
	def mergeKLists(self, lists):
	    def merge2lists(l1, l2):
	        if l1 is None and l2 is None: return None
	        if l1 is None: return l2 
	        if l2 is None: return l1
	       
	        (node_to_add, l1, l2) = (l1, l1.next, l2) if l1.val <= l2.val else (l2, l1, l2.next)
	        merged_list_head, current_node = node_to_add, node_to_add
	        while l1 is not None and l2 is not None:
	            (node_to_add, l1, l2) = (l1, l1.next, l2) if l1.val <= l2.val else (l2, l1, l2.next)
	            current_node.next, current_node = node_to_add, node_to_add
	        current_node.next = l1 if l1 is not None  else l2
	        return merged_list_head
	    if not lists: return None 
	    merged_list, unmerged_lists = lists[0], lists[1:]
	    for each_list in unmerged_lists:
	        merged_list = merge2lists(merged_list, each_list)
	    return merged_list
	
	    










if __name__ == "__main__":
	
	

	l1, l2, l3 = SingleLinkedList(), SingleLinkedList(), SingleLinkedList()
	for num in [1,10,20,20,20,30,40]:
		l1.add_node_to_list(num)
	#[0,1,2,3,4,17,18,30,35,100,200]:
	for num in [0,1,2,3,4]:
		l2.add_node_to_list(num)
	for num in [0,11,22,31,49]:
		l3.add_node_to_list(num)

	print l1, l2, l3
	print mergelists([l1, l2, l3])

	
	#print a 
	#print a.__repr__()
	#eval(a.__str__())





