class Solution(object):
  def twoSum(self, nums, target):
    d = {}
    for i, v in enumerate(nums):
      if v in d:
        return [i, d[v]]
      d[target - v] = i
