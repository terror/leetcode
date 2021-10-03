class Solution:
  def sequentialDigits(self, low: int, high: int) -> List[int]:
    ans = []
    for i in range(1, 10):
      x = i
      for j in range(x + 1, 10):
        x = (x * 10) + j
        if self.check(x, low, high):
          ans.append(x)
    return sorted(ans)

  def check(self, n, l, h):
    return l <= n <= h
