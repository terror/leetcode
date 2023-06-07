class Solution:
  def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
    arr.sort(); diff = None
    for i in range(1, len(arr)):
      d = arr[i] - arr[i - 1]
      if diff == None: diff = d
      else:
        if d != diff: return False
    return True
