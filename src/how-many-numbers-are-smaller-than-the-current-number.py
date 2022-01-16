class Solution:
  def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    return [len(list(filter(lambda x: x < num, nums))) for num in nums]
