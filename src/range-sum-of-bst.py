# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
  def __init__(self):
    self.ans = 0

  def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:

    if not root:
      return

    def go(root, ans):
      if root:
        if self.check(root.val, low, high):
          self.ans += root.val

        if low < root.val:
          go(root.left, self.ans)

        if high > root.val:
          go(root.right, self.ans)

    go(root, self.ans)
    return self.ans

  def check(self, v, l, h):
    return l <= v <= h
