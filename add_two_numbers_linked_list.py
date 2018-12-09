class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry, digit_sum = 0, 0
        head3, previous_node , current_node  = None, None, None
        
        while l1 is not None and l2 is not None:
            digit_sum = l1.val+l2.val+carry
            val, carry = (digit_sum%10, digit_sum/10) if digit_sum>=10 else (digit_sum,0)
            if head3 == None:
                head3 = ListNode(val)
               
                head3.next = None
                previous_node = head3
            else: 
                current_node = ListNode(val)
                previous_node.next = current_node
                
                current_node.next = None
                previous_node = current_node
            l1, l2 = l1.next, l2.next
        
        longer_number = l1 if l1 is not None else l2
        
        while longer_number is not None:
            digit_sum = carry + longer_number.val
            val, carry = (digit_sum%10, digit_sum/10) if digit_sum>=10 else (digit_sum,0)
            current_node = ListNode(val)
            previous_node.next = current_node 
            current_node.next = None
            previous_node = current_node
            longer_number = longer_number.next
            
        if carry > 0:
            current_node = ListNode(carry)
            previous_node.next = current_node
            current_node.next = None
        return head3
            
            
            
            
                
            
        
        
                
                
            
                
            
             
            
        
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        