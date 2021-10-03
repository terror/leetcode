class Solution:
  def minOperations(self, logs: List[str]) -> int:
    curr = 0
    for i in logs:
      if i == "./":
        continue
      if i == "../":
        curr -= 1
      else:
        curr += 1
      curr = max(0, curr)
    return curr
