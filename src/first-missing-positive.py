class Solution:
  def firstMissingPositive(self, nums: List[int]) -> int:
    if len(nums) == 0: return 1

    # remove dups and negative numbers
    x = list(set(list(filter(lambda x: x > 0, nums))))

    # now we find first missing from 0 -> 2^31 - 1
    o = 1
    while o in x:
      o += 1
    return o
