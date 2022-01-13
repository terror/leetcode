# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def inorderTraversal(self, root: TreeNode) -> List[int]:
    if not root:
      return []

    ans = []

    def go(root, ans):
      if root:
        if root.left:
          go(root.left, ans)
        ans.append(root.val)
        if root.right:
          go(root.right, ans)

    go(root, ans)
    return ans
