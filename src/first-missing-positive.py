# 41. First Missing Positive
#
# Solution:
#
# Filter out all positive numbers from `nums`, if we don't have
# any the lowest positive number is 1.
#
# Store each number in a lookup table, then for all (1, n + 1) if we
# don't have it stored, ouput it. Since we go from min -> max we're
# always guaranteed to output the smallest number.
#
# TC: O(n) time + O(n) space

class Solution:
  def firstMissingPositive(self, nums: List[int]) -> int:
    nums = list(filter(lambda x: x > 0, nums))

    if not nums:
      return 1

    d = defaultdict(bool)
    for num in nums:
      d[num] = True

    for i in range(1, len(nums) + 2):
      if not d[i]:
        return i
