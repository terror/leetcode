class Solution:
  def thirdMax(self, nums: List[int]) -> int:
    if len(set(nums)) < 3:
      return max(nums)

    nums = list(set(nums))
    heapq._heapify_max(nums)

    i, seen = 0, set()
    while i < 2:
      elem = heapq._heappop_max(nums)
      if elem in seen:
        continue
      seen.add(elem)
      i += 1

    return heapq._heappop_max(nums)
