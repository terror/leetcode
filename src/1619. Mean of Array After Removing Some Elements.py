class Solution:
  def trimMean(self, arr: List[int]) -> float:
    x = int(len(arr) * 0.05)
    arr.sort()
    return sum(arr[x:len(arr) - x]) / len(arr[x:len(arr) - x])
