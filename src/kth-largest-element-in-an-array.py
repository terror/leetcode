class Solution:
  def findKthLargest(self, nums: List[int], k: int) -> int:
    ans = 0
    heapq._heapify_max(nums)
    for _ in range(k):
      ans = heapq._heappop_max(nums)
    return ans
