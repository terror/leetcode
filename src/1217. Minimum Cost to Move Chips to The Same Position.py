class Solution:
  def minCostToMoveChips(self, position: List[int]) -> int:
    a = b = 0
    for i in position:
      if i % 2 == 0:
        a += 1
      else:
        b += 1

    if a == len(position) or b == len(position):
      return 0

    return min(a, b)
