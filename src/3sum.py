class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    ret = set()
    for i, v in enumerate(nums):
      j, k = i + 1, len(nums) - 1
      while j < k:
        if nums[j] + nums[k] == -v:
          ret.add((v, nums[j], nums[k]))
        if nums[j] + nums[k] > -v:
          k -= 1
        else:
          j += 1
    return list(map(lambda x: list(x), ret))
