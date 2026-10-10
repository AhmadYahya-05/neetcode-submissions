# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def findMinNode(self, root: Optional[TreeNode]):
        
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr


    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if not root: return 
        
        if key < root.val:              #searching for key (simple recuresive search)
            root.left = self.deleteNode(root.left,key)
        elif key > root.val:
            root.right = self.deleteNode(root.right,key)

                        # else case means we have found the node we need to delete
        else:
            if not root.right:
                return root.left            #cases where node has 1 or 0 children
            elif not root.left:
                return root.right
            
            else:# if two childeren we use the min value in right subtree (this works)
                minNode = self.findMinNode(root.right)          
                root.val = minNode.val
                root.right = self.deleteNode(root.right, minNode.val)

        return root
