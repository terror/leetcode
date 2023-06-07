class Solution:
  def findMatrix(self, nums: List[int]) -> List[List[int]]:
    c = Counter(nums)
    ans = []
    while sum(c.values()) > 0:
      curr = []
      for k in c:
        if c[k]:
          curr.append(k)
          c[k] -= 1
      ans.append(curr)
    return ans
