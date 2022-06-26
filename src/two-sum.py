# 1. Two Sum
#
# Solution:
#
# Iterate over `nums`, at each iteration store the current index in a dict `d`
# at position `target - v` (the complement of v), if we find `v` at our current
# iteration in `d`, we know we have two numbers that add up to `target` -- so we
# output the current index and the index stored at `d[v]`.

class Solution(object):
  def twoSum(self, nums, target):
    d = {}
    for i, v in enumerate(nums):
      if v in d:
        return [i, d[v]]
      d[target - v] = i
