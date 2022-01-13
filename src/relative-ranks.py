class Solution:
  def findRelativeRanks(self, nums: List[int]) -> List[str]:
    x, y, r = nums.copy(), {}, 1
    heapq._heapify_max(x)

    for i in range(len(nums)):
      el = heapq._heappop_max(x)
      y[el] = r
      r += 1

    d = {1: "Gold Medal", 2: "Silver Medal", 3: "Bronze Medal"}

    return [
      d[y[nums[i]]] if y[nums[i]] in d else str(y[nums[i]])
      for i in range(len(nums))
    ]
