# BFS 
# O(n) time, O(n) space
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = deque()
        q.append(root)

        parentq = deque()
        parentq.append(None)

        xFound = False
        yFound = False
        xParent = None
        yParent = None 

        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                currParent = parentq.popleft()

                if curr.val == x:
                    xFound=True 
                    xParent = currParent

                if curr.val == y:
                    yFound=True 
                    yParent = currParent

                if curr.left:
                    q.append(curr.left)
                    parentq.append(curr)

                if curr.right:
                    q.append(curr.right)
                    parentq.append(curr)

            if xFound and yFound:
                return xParent != yParent
            if xFound or yFound:
                return False 

        return False


# DFS
# O(n) time, O(h) space
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.xLevel = -1
        self.yLevel = -1
        self.xParent = None
        self.yParent = None 

    def helper(self, node, level, parent):
        if not node:
            return 

        if node.val == x:
            self.xLevel=level 
            self.xParent=parent 

        if node.val == y:
            self.yLevel=level 
            self.yParent=parent 

        helper(node.left,level+1,node)
        helper(node.right,level+1,node)

    return self.xLevel == self.yLevel and self.xParent != self.yParent






