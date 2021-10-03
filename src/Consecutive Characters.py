class Solution:
  def maxPower(self, s: str) -> int:
    ans = 0
    for i in range(len(s)):
      j = i
      c = 0
      while j >= 0 and s[j] == s[i]:
        c += 1
        j -= 1
      ans = max(ans, c)
    return ans
