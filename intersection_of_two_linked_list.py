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