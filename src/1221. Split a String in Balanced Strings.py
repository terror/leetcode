class Solution:
  def balancedStringSplit(self, s: str) -> int:
    # each time we encounter a balanced string we want it
    ans = x = 0
    for i in s:
      if i == 'L':
        x += 1
      else:
        x -= 1
      if not x:
        ans += 1
    return ans
