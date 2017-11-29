'''
Author: Fionn Mcguire
Date 29-11-2017
Description: Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node 
values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s
could also be considered as a subtree of itself.
'''
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def hasSameChildren(node1,node2):
            if node1.left == node2.left and node1.right == node2.right:
                if node2.left != None:
                    leftNode1 = node1.left
                    leftNode2 = node2.left
                    answer = hasSameChildren(leftNode1,leftNode2)
                    if answer == False:
                        return False
                if node2.right != None:
                    rightNode1 = node1.right
                    rightNode2 = node2.right
                    answer = hasSameChildren(rightNode1,rightNode2)
                    if answer == False:
                        return False
                return True
            return False    
        
        while 1:
            if t == None or s == None:
                return False
            
            if t.val == s.val:
                answer = hasSameChildren(t,s)
                return answer
            elif t.val > s.val:
                t = t.left
            elif t.val < s.val:
                t = t.right
                
                
        
