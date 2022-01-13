class Solution:
  def maxPower(self, s: str) -> int:
    a = b = 0
    prev = None
    for i in s:
      if i == prev:
        a += 1
      else:
        prev = i
        a = 1
      b = max(a, b)
    return b
