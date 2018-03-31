from binary_tree import BinaryTree
from queue import Queue
from binary_tree import TreeNode

class BST(BinaryTree):
    def add_node_to_tree(self, data):
        if self.root == None: 
            self.root = TreeNode(data)
        else:
            self._add_node_to_tree(self.root, data)
    
    def _add_node_to_tree(self, node, data):
        if data < node.data:
            if node.left:
                self._add_node_to_tree(node.left, data) 
            else:
                node.left = TreeNode(data)
                return
        else:
            if node.right:
                self._add_node_to_tree(node.right, data)
            else:
                node.right = TreeNode(data)
                return

    def print_inorder(self, node):
        if self.root == None:
            print "Tree is empty"
        else:
            if node != None:
                print node.data
                self.print_inorder(node.left)
                self.print_inorder(node.right)
    
    def find_node(self, data):
        if self.root == None:
            print "The tree is empty"
            return
        else:
            print "calling _find on :{}".format(data)
            return self._find_node(self.root, None, data)
    def _find_node(self, node, parent, data):
        if node == None:
            return None, None
        if node.data == data:
            return node, parent
        elif data < node.data:
            return self._find_node(node.left, node, data)
            #r, r_parent = self._find_node(node.left, node, data)
            #return r, r_parent
        elif data > node.data:
            return self._find_node(node.right, node, data)

    def find_min(self, node = None):
        if node == None:
            self._find_min(self.root)
        else:
            if type(node) is int:
                node, parent = self.find_node(node)
                self._find_min(node)
    
    def _find_min(self, node):
        print "yet to write this"




    def delete_node(self, data):
        if self.root == None:
            print "The tree is empty, can't delete node"
            return
        else:

            _delete_node(self, data)

    def _delete_node(self, data):
        node, parent = self.find_node(data)

    def isBST(self):
        if self.root == None:
            print " Tree is empty"
            return False
        else:
            return self._isBST(self.root)
    def _isBST(self, node):
        if node == None:
            return True
        else:
            left_is_bst =  self._isBST(node.left) if (node.left is None or node.left.data < node.data) else False
            right_is_bst =  self._isBST(node.right) if (node.right is None or node.right.data >= node.data) else False
    
        return left_is_bst and right_is_bst





def create_bst_from_sorted_array(b, s_l):
    if s_l:
        mid = len(s_l)/2
        b.add_node_to_tree(s_l[mid])
        #b.print_level_order()
        create_bst_from_sorted_array(b,s_l[0:mid])
        
        create_bst_from_sorted_array(b,s_l[mid+1:])







if __name__ == "__main__":
    a = BST()
    
    
    a.add_node_to_tree(20)
    a.add_node_to_tree(10)
    a.add_node_to_tree(30)
    a.add_node_to_tree(40)
    a.add_node_to_tree(50)
    a.add_node_to_tree(60)
    a.add_node_to_tree(70)
    node, parent = a.find_node(20)
    print node, parent
    a.find_min(20)
    print a.isBST()
    
    b = BST()
    create_bst_from_sorted_array(a, range(0,10))
    #a.print_level_order()
    #b.print_level_order()

    
