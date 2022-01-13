class Solution:
  def isIsomorphic(self, s: str, t: str) -> bool:
    if not s:
      return 1

    if len(set(s)) != len(set(t)):
      return 0

    d = {}

    for i in range(len(s)):
      if s[i] in d:
        if d[s[i]] != t[i]:
          return 0
      else:
        d[s[i]] = t[i]

    return 1
