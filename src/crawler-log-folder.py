class Solution:
  def minOperations(self, logs: List[str]) -> int:
    ans = 0
    for log in logs:
      if log == "./":
        continue
      ans = max(0, ans + (1, -1)[log == "../"])
    return ans
