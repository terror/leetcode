class Solution:
  def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
    ans = numBottles
    if numExchange > numBottles:
      return ans
    while numExchange <= numBottles:
      n = numBottles // numExchange
      numBottles = n + (numBottles % numExchange)
      ans += n
    return ans
