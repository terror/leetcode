class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    best = Max = nums[0]
    for i in range(1, len(nums)):
      best = max(nums[i], nums[i] + best)
      Max = max(Max, best)
    return Max
