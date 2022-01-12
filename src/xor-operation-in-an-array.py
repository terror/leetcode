class Solution:
  def xorOperation(self, n: int, start: int) -> int:
    return functools.reduce(lambda a, b: a ^ b, [start + 2 * i for i in range(n)])
