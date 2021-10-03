class Solution:
  def minSubArrayLen(self, s: int, nums: List[int]) -> int:
    ans = int(2e5)
    i = curr = 0
    for j in range(len(nums)):
      curr += nums[j]
      while curr >= s:
        curr -= nums[i]
        ans = min(ans, j + 1 - i)
        i += 1
    return 0 if ans == int(2e5) else ans
