class Solution:
  def kLengthApart(self, nums: List[int], k: int) -> bool:
    n, c = len(nums), k
    for i in range(n):
      if nums[i]:
        if c < k:
          return 0
        c = 0
      else:
        c += 1
    return 1
