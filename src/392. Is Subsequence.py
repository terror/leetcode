class Solution:
  def isSubsequence(self, s: str, t: str) -> bool:
    a = b = 0

    while b < len(t) and a < len(s):
      if t[b] == s[a]:
        a += 1
      b += 1

    return a == len(s)
