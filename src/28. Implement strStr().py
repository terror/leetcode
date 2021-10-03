class Solution:
  def strStr(self, haystack: str, needle: str) -> int:
    if not needle:
      return 0

    if needle not in haystack:
      return -1

    for i in range(0, len(haystack)):
      if haystack[i:i + len(needle)] == needle:
        return i
