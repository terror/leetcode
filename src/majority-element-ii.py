class Solution:
  def majorityElement(self, nums: List[int]) -> List[int]:
    d, ans = collections.Counter(nums), []

    for key, val in d.items():
      if val > len(nums) / 3:
        ans.append(key)

    return ans
