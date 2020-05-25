# Return the root node of a binary search tree that matches the given preorder traversal.
# (Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val,
# and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first,
# then traverses node.left, then traverses node.right.)

# It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.

# Example 1:
# Input: [8,5,1,7,10,12]
# Output: [8,5,10,1,7,null,12]

# Constraints:
# 1 <= preorder.length <= 100
# 1 <= preorder[i] <= 10^8
# The values of preorder are distinct.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def newNode(val):
            return TreeNode(val, None, None)
        
        def constructor(preorder, size, pos, currNode, Min, Max):
            if pos == size or preorder[pos] < Min or preorder[pos] > Max:
                return pos     
            if preorder[pos] < currNode.val:
                currNode.left  = newNode(preorder[pos])
                pos += 1
                pos = constructor(preorder, size, pos, currNode.left, Min, currNode.val-1)
            if pos == size or preorder[pos] < Min or preorder[pos] > Max:
                return pos
            currNode.right = newNode(preorder[pos])
            pos += 1
            pos = constructor(preorder, size, pos, currNode.right, currNode.val+1, Max)
            return pos
                         
        size = len(preorder)
        if size == 0: return None
        if size == 1: return newNode(preorder[0])
        root = newNode(preorder[0])
        constructor(preorder, size, 1, root, float('-inf'), float('inf'))
        return root