# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        first_list = self.function(root1)
        second_list = self.function(root2)

        return first_list == second_list

    def function(self, root):
        list_of_leafs = []
        if root.left is None and root.right is None:
            list_of_leafs.append(root.val)

        if root.left is not None:
            list_of_leafs += self.function(root.left)

        if root.right is not None:
            list_of_leafs += self.function(root.right)

        return list_of_leafs
