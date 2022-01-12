class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    # If the string is empty, the longest substring is 0.
    if not s:
      return 0

    # If all the characters in the string are the same, the longest
    # substring is 1.
    if len(set(s)) == 1:
      return 1

    i = j = m = 0
    # Find the longest substring.
    while i < len(s) and j < len(s):
      # If we run into a duplicate, update our left pointer.
      if s[j] in s[i:j]:
        i += 1
      # Update our maximum substring length.
      else:
        j += 1
        m = max(m, j - i)

    return m
