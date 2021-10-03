class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    if not s:
      return 0

    o = set()

    ans = i = j = 0

    while i < len(s) and j < len(s):
      if s[j] not in o:
        o.add(s[j])
        j += 1
        ans = max(ans, j - i)
        continue

      o.remove(s[i])
      i += 1

    return ans
