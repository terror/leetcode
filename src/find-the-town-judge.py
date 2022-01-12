class Solution:
  def findJudge(self, n: int, trust: List[List[int]]) -> int:
    deg = [0] * n
    out = [0] * n
    for a, b in trust:
      deg[a - 1] += 1
      out[b - 1] += 1
    for candidate in range(n):
      if deg[candidate] == 0 and out[candidate] == n - 1:
        return candidate + 1
    return -1
