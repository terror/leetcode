class Solution:
  def strStr(self, haystack: str, needle: str) -> int:
    if not needle:
      return 0

    i = 0
    while i < len(haystack):
      if haystack[i] == needle[0]:
        # If the remaining length of the string is less than the length of
        # `needle`, `needle` is not part of `haystack`
        if len(haystack) - i < len(needle):
          return -1
        # Check the next i + len(needle) tokens
        if haystack[i:i + len(needle)] == needle:
          return i
      i += 1

    return -1
