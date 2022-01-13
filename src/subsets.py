class Solution:
  def subsets(self, nums: List[int]) -> List[List[int]]:
    return list(
      itertools.chain.from_iterable(
        itertools.combinations(nums, x) for x in range(len(nums) + 1)
      )
    )
